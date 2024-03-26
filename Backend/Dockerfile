FROM python:3.9-slim-buster AS builder
WORKDIR /code
ADD . /code
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]


