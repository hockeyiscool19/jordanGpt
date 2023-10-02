import firebase_admin
from firebase_admin import credentials
import pandas as pd
import firebase_admin
from firebase_admin import credentials, db
from PUBLIC_VARIABLES import DATABASE_URL
from app.utils.firebase import Firebase


CRED = credentials.Certificate("postmanServiceAccount.json")
firebase_admin.initialize_app(CRED)


class Firebase:
    def __init__(self):
        self.database_url = DATABASE_URL
        self.cred = CRED

    def load_dict(self, data, path='/', url=DATABASE_URL):
        """
        Load a dictionary to Firebase.
        :param data: Dictionary to load
        :param path: Path to load the dictionary to. Default is root.
        """
        ref = db.reference(path=path,url=url)
        print(f"Loading data to Firebase")
        ref.push(data)
        print(f"Loaded data to Firebase")

    def read_dict(self, path='/', url=DATABASE_URL):
        """
        Load a dictionary to Firebase.
        :param data: Dictionary to load
        :param path: Path to load the dictionary to. Default is root.
        """
        ref = db.reference(path=path,url=url)
        print(f"Reading data from Firebase")
        print(f"Read data from Firebase")
        return ref.get()

    def delete_dict(self, path='/', url=DATABASE_URL):
        """
        Load a dictionary to Firebase.
        :param data: Dictionary to load
        :param path: Path to load the dictionary to. Default is root.
        """
        ref = db.reference(path=path,url=url)
        print(f"Deleting data")
        ref.delete()
        print(f"Deleted data")
