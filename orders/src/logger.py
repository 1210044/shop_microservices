import logging

from src.settings import SERVICE_NAME


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        ],
    )

logger = logging.getLogger(SERVICE_NAME)