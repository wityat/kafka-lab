import ast
import logging
import os

from producer import DataPreprocessProducer
from consumer import DataPreprocessConsumer
from data_processor import preprocess_image

producer = DataPreprocessProducer(
    ast.literal_eval(os.environ.get("DATA_PREPROCESS_PRODUCER_CONFIG")),
    os.environ.get("DATA_PREPROCESS_TOPIC")
)
consumer = DataPreprocessConsumer(
    ast.literal_eval(os.environ.get("DATA_PREPROCESS_CONSUMER_CONFIG")),
    os.environ.get("RAW_DATA_TOPIC")
)


def main():
    while True:
        image = consumer.consume_data()
        logging.info("Preprocessing new data!")
        image = preprocess_image(image)
        producer.produce_data(image)


if __name__ == '__main__':
    main()
