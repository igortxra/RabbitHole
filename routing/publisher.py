import pika
from os import getenv
import time


def load_env(env_name: str) -> str:
    env_value = getenv(env_name)
    if env_value is None:
        raise Exception(f"{env_name} not set")
    return env_value


RABBITMQ_HOST = load_env("RABBITMQ_HOST")
RABBITMQ_USER = load_env("RABBITMQ_USER")
RABBITMQ_PASS = load_env("RABBITMQ_PASS")


credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials)
)

channel = connection.channel()
channel.exchange_declare("logs", exchange_type="direct")

msg_count = 0
while True:
    msg_count += 1
    channel.basic_publish(
        exchange="logs", 
        routing_key="info_logger", 
        body=f"Hello World {msg_count}!"
    )
    print("Message", msg_count, "published")
    time.sleep(5)

# connection.close()
