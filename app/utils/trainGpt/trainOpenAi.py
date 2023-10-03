from PUBLIC_VARIABLES import OPENAI_API_KEY
import os
import openai


openai.api_key = OPENAI_API_KEY
res = openai.File.create(file=open(r"app\utils\data\trainData.jsonl", "r"), purpose='fine-tune')
file_id = res["id"]
res = openai.FineTuningJob.create(training_file=file_id, model="gpt-3.5-turbo",n_epochs=3)
job_id = res["id"]
openai.FineTuningJob.retrieve(job_id)