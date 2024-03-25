FROM python:3.10-slim AS service

WORKDIR /code/
COPY ./visualization_consumer/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./visualization_consumer ./

CMD ["watchmedo", "auto-restart", "--directory=/code/", "--pattern=*.py", "--recursive", "--", "streamlit", "run", "/code/src/main.py"]
