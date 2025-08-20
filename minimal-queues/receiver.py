import pika
from os import getenv


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

channel.queue_declare(queue="queue")


def callback(ch, method, properties, body):
    print(body)


channel.basic_consume(queue="queue", auto_ack=True, on_message_callback=callback)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
