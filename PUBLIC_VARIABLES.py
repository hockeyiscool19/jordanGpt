import os
import json

# # Print all environmental variables
# dev_env_file = 'dev.env'

# # Read the dev.env file and extract the environmental variables
# with open(dev_env_file, 'r') as file:
#     for line in file:
#         line = line.strip()
#         # Ignore empty lines and comments
#         if line and not line.startswith('#'):
#             key, value = line.split('=', 1)
#             os.environ[key] = value


OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
DATABASE_URL = os.environ.get('DATABASE_URL')
FINE_TUNING_JOB = os.environ.get('FINE_TUNING_JOB')
GCLOUD_AUTH = json.loads(os.environ.get('GCLOUD_AUTH'))

gcloud_auth_str = os.environ.get('GCLOUD_AUTH')
if not gcloud_auth_str:
    raise ValueError("GCLOUD_AUTH environment variable is not set or is empty.")
GCLOUD_AUTH = json.loads(gcloud_auth_str)
