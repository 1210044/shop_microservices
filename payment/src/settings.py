from os import getenv


SERVICE_NAME = 'payment'
KAFKA_BOOTSTRAP_SERVERS = getenv('KAFKA_BOOTSTRAP_SERVERS')
NEW_ORDERS_TOPIC = getenv('NEW_ORDERS_TOPIC')
PAYED_ORDERS_TOPIC = getenv('PAYED_ORDERS_TOPIC')