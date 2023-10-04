# FROM python:3.10.11

# WORKDIR /code

# COPY ./requirements.txt /code/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY . .

# CMD ["python", "run.py", "--host", "0.0.0.0", "--port", "7860"]


FROM python:3.10.11

WORKDIR /code

# Copy only requirements first to cache it
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Now copy all files
COPY . .

# Run tests. If tests fail, the Docker build process will stop, and the image won't be created.
RUN pytest tests.py

# Default command
CMD ["python", "run.py", "--host", "0.0.0.0", "--port", "7860"]
