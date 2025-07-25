from kafka import KafkaProducer
import time
import os
from kafka.errors import KafkaError

KAFKA_TOPIC = 'new_emails'
KAFKA_SERVER = 'localhost:9092'
EMAIL_FILE = 'valid_emails.txt'


def send_to_kafka():
	producer = KafkaProducer(
		bootstrap_servers=KAFKA_SERVER,
		value_serializer=lambda v: v.encode('utf-8')
	)
	print(f"Producing emails to topic '{KAFKA_TOPIC}'...")

	seen_emails = set()

	while True:
		if os.path.exists(EMAIL_FILE):
			with open(EMAIL_FILE, 'r') as file:
				for line in file:
					email = line.strip()
					if email and email not in seen_emails:
						try:
							producer.send(KAFKA_TOPIC, value=email)
							print(f"Sent email: {email}")
							seen_emails.add(email)
						except KafkaError as e:
							print(f"Kafka error: {e}")
		else:
			print(f"{EMAIL_FILE} does not exist. Waiting for it to be created.")

		print("Waiting for new emails...")
		time.sleep(5)

if __name__ == "__main__":
	send_to_kafka()
