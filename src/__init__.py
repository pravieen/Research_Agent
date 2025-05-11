import logging


# Custom logger class that can set and use an identifier
class CustomLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        self.identifier = None

    def set_identifier(self, identifier):
        self.identifier = identifier

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False, stacklevel=3):
        if extra is None:
            extra = {}
        extra['identifier'] = getattr(self, 'identifier', 'unset_identifier')
        super()._log(level, msg, args, exc_info, extra, stack_info, stacklevel)


# Set up the logger
logging.setLoggerClass(CustomLogger)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Create a handler
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "[%(asctime)s][%(levelname)-7s][%(identifier)s][%(funcName)s][%(module)s:%(filename)s].(%(lineno)d)] : %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)