import logging
import os

TMP_FILE = "/tmp/test.log"


def test_default_logger(caplog):
    """Test the default logger"""
    from sat.logs import SATLogger

    logger = SATLogger()
    logger.info("Test message")
    assert "Test message" in caplog.text
    logger.debug("DEBUG message")
    assert "DEBUG message" not in caplog.text


def test_add_handlers(caplog):
    """Test adding handlers to the logger"""
    from sat.logs import SATLogger

    logger = SATLogger()
    logger.add_handlers([(logging.FileHandler(TMP_FILE), logging.Formatter("%(message)s"))])
    logger.info("Test message")
    assert "Test message" in caplog.text
    assert os.path.exists(TMP_FILE)
