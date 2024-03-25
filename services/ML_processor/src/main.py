import ast
import logging
import os
import time

from producer import MLProducer
from consumer import MLConsumer
from predictor import predict_image_labels

producer = MLProducer(
    ast.literal_eval(os.environ.get("DATA_PREPROCESS_PRODUCER_CONFIG")),
    os.environ.get("ML_PROCESSOR_TOPIC")
)
consumer = MLConsumer(
    ast.literal_eval(os.environ.get("DATA_PREPROCESS_CONSUMER_CONFIG")),
    os.environ.get("DATA_PREPROCESS_TOPIC")
)


def main():
    while True:
        image = consumer.consume_data()
        st_time = time.perf_counter()
        logging.info("Predicting new data!")
        labels = predict_image_labels(image)
        elapsed_time = time.perf_counter() - st_time
        logging.info(f"elapsed time: {elapsed_time}")
        producer.produce_data(image.read(), labels, elapsed_time)


if __name__ == '__main__':
    main()
