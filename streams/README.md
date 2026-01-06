Using python rstream with RabbitMQ Streams

Sample test from [RabbitMQ tutorials](https://www.rabbitmq.com/getstarted.html).


Running RabbitMQ in a docker container
```sh
docker run -it --rm --name rabbitmq -p 5552:5552 -p 15672:15672 -p 5672:5672  \
    -e RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS='-rabbitmq_stream advertised_host localhost' \
    rabbitmq:4-management

```

Enabling rabbitmq stream
```sh
docker exec rabbitmq rabbitmq-plugins enable rabbitmq_stream rabbitmq_stream_management

```

Running sample scripts that sends and receivers messages (Use venv and install requirements)
```py
# Send message to stream
python3 send.py

# Receive messages from stream
python3 receive.py
```
