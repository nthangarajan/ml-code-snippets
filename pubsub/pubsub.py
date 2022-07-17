from google.cloud import pubsub
import json

publish_client = pubsub.PublisherClient()
topic = f"projects/{GOOGLE_CLOUD_PROJECT}/topics/{PUBSUB_TOPIC}"
data = {"num_epochs": 3, "learning_rate": 1e-2}
message = json.dumps(data)

_ = publish_client.publish(topic, message.encode())