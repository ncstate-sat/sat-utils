import logging
from unittest.mock import patch, MagicMock

from sat.slack import Slack, SlackApiError
from sat.logs import setup_sat_logging


def mock_slack_response():
    return {"ok": False, "error": "test error", "args": {"error": "test error"}}


def test_send_message_error(caplog):
    caplog.set_level(logging.INFO)
    with patch("sat.slack.WebClient.chat_postMessage") as mock:
        mock.side_effect = SlackApiError("test error", mock_slack_response())
        slack = Slack("test")
        slack.send_message("test", "test")
        assert mock.called
        assert "Slack encountered an error: test error" in caplog.text
