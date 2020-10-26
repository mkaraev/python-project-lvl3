import logging
import sys
from functools import wraps

log = logging.getLogger(__name__)
LEVELS = (INFO, DEBUG) = ("INFO", "DEBUG")


def configure_logger(log_level):
    log_format = "[ %(levelname)-5.5s ] :: %(message)s"
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        format=log_format,
        level=logging.getLevelName(log_level),
    )


def debug_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(f"[{func.__name__:>30}] :: input: {args} {kwargs}")
        res = func(*args, **kwargs)
        log.debug(f"[{func.__name__:>30}] :: return: {str(res)}")
        return res

    return wrapper