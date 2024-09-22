import os
import sys
import datetime
import logging
from pytz import timezone

LOGGER_NAME = 'GENERAL_LOGGER'

LOG_FORMAT = f"%(asctime)s - %(levelname)s | %(message)s"
# LOG_FORMAT = f"%(levelname)s | %(message)s"



def custom_converter(*args):
    log_timezone =  os.getenv("SITE_TIMEZONE", "Asia/Singapore")
    return datetime.datetime.now(timezone(log_timezone)).timetuple()

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    format = LOG_FORMAT

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        formatter.converter = custom_converter
        return formatter.format(record)


class InfoFilter(logging.Filter):
    def filter(self, log_record):
        return log_record.levelno == logging.INFO or log_record.levelno == logging.DEBUG

class Logging:
    def __init__(self, logger_name:str = LOGGER_NAME):
        self.logger = self._get_logger(logger_name)

    def _create_handler(self,handler_type, handler_name, handler_level):
        try:
            handler = logging.StreamHandler(handler_type)
            handler.name = handler_name
            handler.setLevel(handler_level)
            handler.setFormatter(CustomFormatter())


            return handler
        except Exception as e:
            raise Exception(f"Error occured in 'create_handler'. Inner_Exception:'{e}'.")

    def _get_logger(self, logger_name : str):
        try:

            pylogger = logging.getLogger(logger_name)
            pylogger.setLevel(logging.DEBUG)
            # create handlers for standard outputs and errors
            stream_handler_out = self._create_handler(sys.stdout, "StandardOutput", logging.DEBUG)
            stream_handler_out.addFilter(InfoFilter())

            stream_handler_err = self._create_handler(sys.stderr, "StandardError", logging.WARNING)
            # To avoid duplication
            # remove handler and set propagate to False
            pylogger.removeHandler(stream_handler_out)
            pylogger.removeHandler(stream_handler_err)
            pylogger.propagate = False
            # add default handlers
            if not pylogger.handlers:
                pylogger.addHandler(stream_handler_out)
                pylogger.addHandler(stream_handler_err)
            return pylogger
        except Exception as e:
            raise Exception(f"Error occured in 'get_logger'. Inner_Exception:'{e}'.")

    def info(self, msg):
        return self.logger.info(msg)

    def debug(self, msg):
        return self.logger.debug(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def error(self, msg):
        return self.logger.error(msg)

    def critical(self, msg):
        return self.logger.critical(msg)

logger = Logging()