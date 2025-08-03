from us_visa.logger import logging
from us_visa.Exception import USvisaException
import sys

try:
    a = 1/'10'
except Exception as e:
    logging.info(f'An error occurred: {e}')
    raise USvisaException(e, sys) from e
