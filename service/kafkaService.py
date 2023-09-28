from functools import lru_cache
from confluent_kafka import Producer
from config import Settings
import socket

@lru_cache()
def get_settings():
    return Settings()


conf = {'bootstrap.servers': Settings().broker,
        'client.id': socket.gethostname()}

producer = Producer(conf)