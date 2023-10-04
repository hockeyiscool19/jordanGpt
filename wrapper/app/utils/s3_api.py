from io import BytesIO
import boto3.session
import awswrangler
import pandas

from PUBLIC_VARIABLES import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY
# https://www.gormanalysis.com/blog/connecting-to-aws-s3-with-python/

s3 = dict({
    "service_name": "s3",
    "region_name": "us-east-1",
    "aws_access_key_id": AWS_ACCESS_KEY,
    "aws_secret_access_key": AWS_SECRET_ACCESS_KEY,
    "bucket_name": "jordan-gpt"
})


class ReadWriteApi:
    def __init__(self, s3: dict):
        self.s3 = boto3.resource(
            service_name=s3["service_name"],
            region_name=s3["region_name"],
            aws_access_key_id=s3["aws_access_key_id"],
            aws_secret_access_key=s3["aws_secret_access_key"]
        )
        self.client = boto3.client(
            "s3",
            region_name=s3["region_name"],
            aws_access_key_id=s3["aws_access_key_id"],
            aws_secret_access_key=s3["aws_secret_access_key"]
        )
        self.session = boto3.Session(
            region_name=s3["region_name"],
            aws_access_key_id=s3["aws_access_key_id"],
            aws_secret_access_key=s3["aws_secret_access_key"]
        )
        self.bucket_name = s3["bucket_name"]
        self.secret_key = AWS_SECRET_ACCESS_KEY
        self.access_key = AWS_ACCESS_KEY

    def get_bucket_names(self):
        for bucket in self.s3.buckets.all():
            print(bucket.name)

    def get_object_names(self):
        for obj in self.s3.Bucket(self.bucket_name).objects.all():
            print(obj)

    @staticmethod
    def dataframe_to_parquet(dataframe: pandas.DataFrame):
        buffer = BytesIO()
        dataframe.to_parquet(buffer, compression="snappy", index=False)
        buffer.seek(0)
        return buffer.read()

    def valid_file(self, path: str) -> bool:
        '''
        Folder should exists.
        Folder should not be empty.
        '''
        if path == "":
            return True
        if not path.endswith('/'):
            path = path + '/'
        resp = self.client.list_objects(
            Bucket=self.bucket_name, Prefix=path, Delimiter='/', MaxKeys=1)
        return 'Contents' in resp or path == ""

    def upload_df(self, dataframe, path, filename, extension, mode):
        """
        :param dataframe: data
        :param path: path to file in s3... DOES NOT END WITH "/"
        :param filename: name of file
        :param extension: parquet, csv,
        :param mode: append or overwrite
        """
        awswrangler.s3.to_parquet(
            df=dataframe,
            path=f"s3://{self.bucket_name}/{path}{filename}.{extension}",
            boto3_session=self.session,
            dataset=True,
            mode=mode
        )
        print(f"{filename} uploaded to {path}")

    def upload_txt(self, txt_file, path):
        with open(txt_file, 'r') as file:
            training_data = file.read()
        training_bytes = training_data.encode('utf-8')

        self.client.put_object(
            Bucket=self.bucket_name,
            Key=path,
            Body=training_bytes
        )
    def upload_file(self, file, path):
        self.client.upload_file(file, self.bucket_name, path)
        print(f"{file} uploaded to {path}")

    def read_txt(self, path):
        response = self.client.get_object(
            Bucket=self.bucket_name,
            Key=path
        )
        return response['Body'].read().decode('utf-8')
    
    def delete(self, path, key, extension):
        """
        :param path: path to file
        :param key:
        :param extension: parquet or csv
        :return:
        """
        if path == "":
            self.client.delete_object(
                Bucket=self.bucket_name, Key=f"{path}/{key}.{extension}")

    def read_parquet(self, path):
        """
        :param path:
        :return: dataframe
        """
        return awswrangler.s3.read_parquet(f"s3://{self.bucket_name}/{path}", boto3_session=self.session)


FILES = [
    (r"trainGpt\data\resume.txt", "training_data/resume.txt"),
    (r"trainGpt\data\roleDescriptions.txt", "training_data/roleDescriptions.txt")
]

READ_WRITE_API = ReadWriteApi(s3)


def main():
    for file in FILES:
        print(file)
        READ_WRITE_API.upload_txt(file[0], file[1])


if __name__ == "__main__":
    main()
