import base64
import io
import json
import torch

from confluent_kafka import Consumer, KafkaError


class MLConsumer(Consumer):
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
                    print(msg.error())
                    break

            data = base64.b64decode(json.loads(msg.value().decode("utf-8"))["value"])
            image = io.BytesIO(data)
            image.seek(0)
            return image
