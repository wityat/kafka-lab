FROM python:3.10-slim AS service

WORKDIR /code/
COPY ./ML_processor/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ML_processor ./

CMD ["watchmedo", "auto-restart", "--directory=/code/", "--pattern=*.py", "--recursive", "--", "python3", "/code/src/main.py"]
