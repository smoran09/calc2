# importing module
import logging

# Create and configure logger
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

# Creating an object
logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("This is a debug log")
logger.error("Division by zero error")
