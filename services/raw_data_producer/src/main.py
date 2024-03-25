import ast
import logging
import os
import random
import time
from producer import RawDataProducer

producer = RawDataProducer(
    ast.literal_eval(os.environ.get("RAW_DATA_PRODUCER_CONFIG")),
    os.environ.get("RAW_DATA_TOPIC"),
    os.environ.get("DATASET_PATH"),
)


def produce_raw_data():
    while True:
        producer.produce_data()
        time.sleep(1)


if __name__ == '__main__':
    produce_raw_data()
