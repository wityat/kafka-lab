import json
import os
import random
import uuid
import base64

from confluent_kafka import Producer


class RawDataProducer(Producer):
    def __init__(self, producer_config: dict, topic: str, dataset_path: str):
        super().__init__(producer_config)
        self.topic = topic
        self.dataset_path = dataset_path

    def produce_data(self):
        filename = random.choice(os.listdir(self.dataset_path))
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filepath = os.path.join(self.dataset_path, filename)
            with open(filepath, 'rb') as f:
                self.produce(self.topic, value=json.dumps({
                    "id": str(uuid.uuid4()),
                    "value": base64.b64encode(f.read()).decode('utf-8')
                }))
            self.flush()
