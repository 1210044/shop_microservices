from aiokafka import AIOKafkaProducer

from src.settings import KAFKA_BOOTSTRAP_SERVERS


producer = AIOKafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS
    )