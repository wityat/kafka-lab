FROM python:3.10-slim AS service

WORKDIR /code/
COPY ./data_preprocessor/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./data_preprocessor ./

CMD ["watchmedo", "auto-restart", "--directory=/code/", "--pattern=*.py", "--recursive", "--", "python3", "/code/src/main.py"]
