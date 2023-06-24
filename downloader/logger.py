import logging


logging.basicConfig(
    format='%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
