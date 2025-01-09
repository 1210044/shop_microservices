import json
from aiokafka import AIOKafkaConsumer

from src.logger import logger
from src.settings import KAFKA_BOOTSTRAP_SERVERS, SENT_ORDERS_TOPIC


consumer = AIOKafkaConsumer(
    SENT_ORDERS_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id='notifications_group',
)


async def consume_messages():
    try:
        async for msg in consumer:
            order = json.loads(msg.value.decode('utf-8'))
            logger.info(f'Received order №{order['id']} for notification')
            await send_notification_order(order)
    except Exception as e:
        logger.error(str(e))


async def send_notification_order(order):
    logger.info(f'Sending notification order №{order['id']}')
    order['status'] = 'delivered'
    logger.info(order)