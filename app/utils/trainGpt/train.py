from PUBLIC_VARIABLES import OPENAI_API_KEY
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader
import os


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

FILES = [
    r"app\utils\data\resume.txt",
    r"app\utils\data\roleDescriptions.txt",
]


if __name__ == "__main__":
    loader1 = TextLoader(FILES[0])
    loader2 = TextLoader(FILES[1])
    index = VectorstoreIndexCreator(vectorstore_kwargs={
                                    "persist_directory": r"app\utils\data\langchainModel"}).from_loaders([loader1, loader2])
