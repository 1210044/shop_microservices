import json, asyncio
from aiokafka import AIOKafkaConsumer

from src.logger import logger
from src.settings import KAFKA_BOOTSTRAP_SERVERS, PAYED_ORDERS_TOPIC
from src.producer import send_order_in_sent_orders_topic


consumer = AIOKafkaConsumer(
    PAYED_ORDERS_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id='shipping_group',
)


async def consume_messages():
    try:
        async for msg in consumer:
            order = json.loads(msg.value.decode('utf-8'))
            logger.info(f'Received order №{order['id']} for shipping')
            await shipping_order(order)
    except Exception as e:
        logger.error(str(e))


async def shipping_order(order):
    logger.info(f'Shipping order №{order['id']}')
    await asyncio.sleep(10)
    order['status'] = 'shipped'
    logger.info(order)
    await send_order_in_sent_orders_topic(order)
