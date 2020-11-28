FROM python:3.6
ADD ./ ./orange-classifier-api-upload
WORKDIR ./orange-classifier-api-upload
RUN pip install -r requirements.txt
RUN export FLASK_APP=main.py
