from random import randint
from fastapi import FastAPI

from src.settings import NEW_ORDERS_TOPIC
from src.logger import logger
from src.producer import producer
from src.schemas import OrderIn, OrderOut


async def lifespan(app: FastAPI):
    logger.info('Starting producer')
    await producer.start()
    yield
    await producer.stop()
    logger.info('Stopped producer')


app = FastAPI(lifespan=lifespan)


@app.post('/orders/', response_model=OrderOut)
async def create_order(order: OrderIn) -> OrderOut:
    logger.info('Creating a new order')
    new_order = OrderOut(
        id=randint(1, 100),
    )
    logger.info(f'Send Order №{new_order.id} in {NEW_ORDERS_TOPIC} topic')
    try:
        await producer.send_and_wait(NEW_ORDERS_TOPIC, new_order.model_dump_json().encode('utf-8'))
    except Exception as e:
        logger.error(str(e))
    return new_order