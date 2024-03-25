import json
import logging

from confluent_kafka import Consumer, KafkaError


class VisualizationConsumer(Consumer):
    def __init__(self, consumer_config: dict, topic: str):
        super().__init__(consumer_config)
        self.subscribe([topic])

    def consume_data(self):
        while True:
            msg = self.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    logging.error(msg.error())
                    break

            return json.loads(msg.value().decode('utf-8'))
