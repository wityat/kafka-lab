import base64
import json
import io

from PIL import Image
from confluent_kafka import Consumer, KafkaError


class DataPreprocessConsumer(Consumer):
    def __init__(self, consumer_config: dict, topic: str):
        super().__init__(consumer_config)
        self.subscribe([topic])

    def consume_data(self):
        while True:
            msg = self.poll(1000)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            data = base64.b64decode(json.loads(msg.value())["value"])
            image = Image.open(io.BytesIO(data))
            return image
