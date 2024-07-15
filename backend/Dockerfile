# choose a base image
FROM python:3.9-slim


# set up the woking directory
WORKDIR /app


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
