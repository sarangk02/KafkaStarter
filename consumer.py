from kafka import KafkaConsumer

KAFKA_TOPIC = 'new_emails'
KAFKA_SERVER = 'localhost:9092'

def consume_from_kafka():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda v: v.decode('utf-8')
    )

    print(f"Listening for new emails on topic '{KAFKA_TOPIC}'...")

    try:
        for message in consumer:
            print(f"Received email: {message.value}")
    except Exception as e:
        print(f"Kafka error: {e}")

if __name__ == "__main__":
	consume_from_kafka()
