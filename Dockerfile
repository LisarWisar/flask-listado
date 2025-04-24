FROM python:3.12-slim
RUN apt-get update && apt-get install -y build-essential gcc
WORKDIR /app
COPY . ./app
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
CMD ["python", "./src/app.py"]

