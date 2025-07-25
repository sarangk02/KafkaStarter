

# KafkaStarter

Welcome to KafkaStarter—a hands-on, beginner-friendly project designed to kickstart your journey into the world of Apache Kafka! Built with the help of AI, this project is perfect for anyone eager to learn Kafka fundamentals through practical Python examples. You'll validate email addresses, stream them with Kafka, and visualize everything with a modern UI—all powered by Docker for easy setup. Whether you're new to event streaming or just want a fun way to experiment, KafkaStarter is your launchpad.

---
**Credit:** This project was inspired by and built with guidance from [Apache KAFKA | M Prashant](https://youtu.be/QI5WRCdp0vs?feature=shared).
---

## Project Structure

- `main.py`: Validates user-input email addresses and saves valid ones to `valid_emails.txt`.
- `producer.py`: Reads new emails from `valid_emails.txt` and sends them to a Kafka topic.
- `consumer.py`: Listens to the Kafka topic and prints received emails.
- `Dockerfile.kafka-server`: Dockerfile for the local Kafka server.
- `Dockerfile.kafka-ui`: Dockerfile for the Kafka UI.
- `valid_emails.txt`: Stores validated email addresses.

## Prerequisites

- Python 3.10.0
- Docker

## Setup

1. **Create a Python virtual environment and install dependencies:**

   ```sh
   python3.10 -m venv .venv
   .venv\Scripts\activate
   pip install kafka-python==2.2.15
   ```

2. **Build and run the Kafka server:**

   ```sh
   docker build -t my-kafka-server -f Dockerfile.kafka-server .
   docker run --name kafka -p 9092:9092 -p 9094:9094 my-kafka-server
   ```

3. **Build and run the Kafka UI:**

   ```sh
   docker build -t my-kafka-ui -f Dockerfile.kafka-ui .
   docker run --name kafka-ui --link kafka -p 8080:8080 my-kafka-ui
   ```

## Usage

1. **Create the Kafka topic**
   - Use the Kafka UI at [http://localhost:8080](http://localhost:8080) to create a topic named `new_emails`.

2. **Validate and store emails**
   - Run the email validator:
     ```sh
     python main.py
     ```
   - Enter email addresses. Valid emails are appended to `valid_emails.txt`.

3. **Start the Kafka producer**
   - Run:
     ```sh
     python producer.py
     ```
   - This sends new emails from `valid_emails.txt` to the Kafka topic `new_emails`.

4. **Start the Kafka consumer**
   - Run:
     ```sh
     python consumer.py
     ```
   - This prints emails received from the Kafka topic.

## Notes

- Kafka topic: `new_emails`
- Kafka server: `localhost:9092`
- Kafka UI: [http://localhost:8080](http://localhost:8080)

## License

For educational purposes only.