import logging
import os


class SATLogger:
    def __init__(self, name: str = __name__, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        if os.getenv("DEBUG"):
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(level)
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def add_handlers(self, handlers: list[(logging.Handler, logging.Formatter)]) -> None:
        """
        Add additional handlers to the logger.
        Handlers should be a list of tuples with a logging.Handler and an
        optional logging.Formatter.
        """
        for tup in handlers:
            handler, formatter = tup
            if formatter:
                handler.setFormatter(formatter)
            else:
                handler.setFormatter(self.formatter)
            self.logger.addHandler(handler)

    def debug(self, msg: str, *args, **kwargs) -> None:
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs) -> None:
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs) -> None:
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs) -> None:
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs) -> None:
        self.logger.critical(msg, args, kwargs)
