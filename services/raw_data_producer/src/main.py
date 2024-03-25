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
        logging.info("Starting raw data producer again...!")
        logging.info("Produced new data!")
        producer.produce_data()
        time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    logging.info("Starting raw data producer...!")
    produce_raw_data()
