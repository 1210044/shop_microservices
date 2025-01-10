import json
from aiokafka import AIOKafkaConsumer

from src.logger import logger
from src.settings import KAFKA_BOOTSTRAP_SERVERS, NEW_ORDERS_TOPIC
from src.producer import send_order_in_paid_orders_topic


consumer = AIOKafkaConsumer(
    NEW_ORDERS_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest', 
    enable_auto_commit=False,
    group_id='payment_group',
)


async def consume_messages():
    try:
        async for msg in consumer:
            order = json.loads(msg.value.decode('utf-8'))
            logger.info(f'Received order №{order['id']} for payment')
            await payment_order(order)
            await consumer.commit()
    except Exception as e:
        logger.error(str(e))


async def payment_order(order):
    logger.info(f'Payment order №{order['id']}')
    order['status'] = 'paid'
    logger.info(order)
    await send_order_in_paid_orders_topic(order)
