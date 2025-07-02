from us_visa.logger import logging
from us_visa.exceptions import USVisaException
import sys

try:
    a = 1/'10'
except Exception as e:
    logging.info(f'An error occurred: {e}')
    raise USVisaException(e, sys) from e
