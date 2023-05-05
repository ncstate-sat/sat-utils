import logging


class SATLogger:
    def __init__(self, name: str = __name__, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def add_handlers(self, handlers: list[logging.Handler]) -> None:
        for handler in handlers:
            self.logger.addHandler(handler)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        self.logger.critical(msg)
