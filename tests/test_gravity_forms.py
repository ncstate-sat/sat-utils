from unittest.mock import patch

import pytest
from requests.exceptions import RequestException
from sat.gravity_forms import GravityForms


def test_environment_variable_error():
    try:
        gravity_forms = GravityForms()
        gravity_forms.get("/forms/2/entries")
        assert False
    except ValueError:
        assert True


def test_request_exception_get(caplog):
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        gravity_forms = GravityForms(
            consumer_key="your_key", consumer_secret="your_secret", base_url="https://baseurl.edu"
        )
        mock_get.side_effect = RequestException("Simulated request exception.")

        print(f"1 - {caplog.text}")
        with pytest.raises(RequestException):
            gravity_forms.get("/forms")

        print(f"2 - {caplog.text}")
        assert "Simulated request exception." in caplog.text
