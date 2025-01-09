import json
from aiokafka import AIOKafkaProducer

from src.logger import logger
from src.settings import KAFKA_BOOTSTRAP_SERVERS, PAYED_ORDERS_TOPIC


producer = AIOKafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS
    )


async def send_order_in_paid_orders_topic(order):
    logger.info(f'Send Order №{order['id']} in {PAYED_ORDERS_TOPIC} topic')
    try:
        await producer.send_and_wait(PAYED_ORDERS_TOPIC, json.dumps(order).encode('utf-8'))
    except Exception as e:
        logger.error(str(e))