import os
import json
# from dotenv import load_dotenv

load_dotenv("dev.env")

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')
FINE_TUNING_JOB = os.environ.get('FINE_TUNING_JOB')
GCLOUD_AUTH = os.environ.get('GCLOUD_AUTH')
GCLOUD_AUTH = json.loads(GCLOUD_AUTH)
