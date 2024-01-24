from unittest.mock import patch

import pytest
from requests.exceptions import RequestException
from sat.gravity_forms import GravityForms


def test_environment_variable_error():
    try:
        gravity_forms = GravityForms()
        gravity_forms.get_sponsors()
        assert False
    except RuntimeError:
        assert True


def test_request_exception_get_sponsors():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        gravity_forms = GravityForms(consumer_key="your_key", consumer_secret="your_secret")
        mock_get.side_effect = RequestException("Simulated request exception.")
        with pytest.raises(RequestException) as ex:
            gravity_forms.get_sponsors()
    assert "Simulated request exception." in str(ex.value)


def test_request_exception_get_cards_requested():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        gravity_forms = GravityForms(consumer_key="your_key", consumer_secret="your_secret")
        mock_get.side_effect = RequestException("Simulated request exception.")
        with pytest.raises(RequestException) as ex:
            gravity_forms.get_cards_requested()
    assert "Simulated request exception." in str(ex.value)


def test_request_exception_get():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        gravity_forms = GravityForms(consumer_key="your_key", consumer_secret="your_secret")
        mock_get.side_effect = RequestException("Simulated request exception.")
        with pytest.raises(RequestException) as ex:
            gravity_forms.get("/forms")
    assert "Simulated request exception." in str(ex.value)
