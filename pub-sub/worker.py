import pika
from os import getenv

from pika.adapters.blocking_connection import BlockingChannel


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
channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="logs", queue=queue_name)

def callback(ch: BlockingChannel, method, properties, body):
    print(body)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
