import base64
import json
import uuid

from confluent_kafka import Producer


class MLProducer(Producer):
    def __init__(self, producer_config: dict, topic: str):
        super().__init__(producer_config)
        self.topic = topic

    def produce_data(self, value: bytes, labels: list, elapsed_time: float):
        self.produce(self.topic, value=json.dumps({
            "id": str(uuid.uuid4()),
            "value": base64.b64encode(value).decode('utf-8'),
            "labels": labels,
            "elapsed_time": elapsed_time
        }))
        self.flush()
