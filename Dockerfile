FROM python:3.12-slim
WORKDIR /app
COPY . ./app
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
CMD ["python", "./src/app.py"]
EXPOSE 3000

