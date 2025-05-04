import functools
import logging

# Configure basic logging
# This will print logs to the console by default
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Get a logger for this module
logger = logging.getLogger(__name__)

def log_function_call(func):
    @functools.wraps(func) # This preserves the original function's metadata
    def wrapper(*args, **kwargs):
        logger.info(f"Entering {func.__name__} function...")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Exiting {func.__name__} function...")
            return result
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
            raise # Re-raise the exception after logging
    return wrapper

