FROM python:3.10-slim AS service

WORKDIR /code/
COPY ./services/raw_data_producer/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./services/raw_data_producer ./
COPY ./dataset/seg_pred/seg_pred /dataset/seg_pred/seg_pred

CMD ["watchmedo", "auto-restart", "--directory=/code/", "--pattern=*.py", "--recursive", "--", "python3", "/code/src/main.py"]
