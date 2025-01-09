from asyncio import create_task
from fastapi import FastAPI

from src.logger import logger
from src.producer import producer
from src.consumer import consumer, consume_messages


async def lifespan(app: FastAPI):
    logger.info('Starting producer')
    await producer.start()
    logger.info('Starting consumer')
    await consumer.start()
    consumer_task = create_task(consume_messages())
    yield
    consumer_task.cancel()
    await producer.stop()
    logger.info('Stopped producer')
    await consumer.stop()
    logger.info('Stopped consumer')


app = FastAPI(lifespan=lifespan)


@app.get('/')
def main():
    logger.info('Payment service is running')
    return {'message': 'Payment service is running'}