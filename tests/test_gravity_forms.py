from unittest.mock import patch

import pytest
from oauthlib.oauth1 import OAuth1Error
from requests.exceptions import RequestException
from sat.gravity_forms import GravityForms


def test_environment_variable_error():
    try:
        gravity_forms = GravityForms()
        gravity_forms.get_sponsors()
        assert False
    except RuntimeError:
        assert True


def test_request_exception():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        gravity_forms = GravityForms(consumer_key="your_key", consumer_secret="your_secret")
        mock_get.side_effect = RequestException("Simulated request exception.")
        with pytest.raises(RequestException) as ex:
            gravity_forms.get_sponsors()
    assert "Simulated request exception." in str(ex.value)


def test_oauth_error():
    with patch("requests_oauthlib.OAuth1Session") as mock_oauth_session:
        gravity_forms = GravityForms(consumer_key="your_key", consumer_secret="your_secret")
        mock_oauth_session.side_effect = OAuth1Error("Simulated OAuth error.")
        with pytest.raises(OAuth1Error) as ex:
            gravity_forms.get_sponsors()
    assert "Simulated OAuth error." in str(ex.value)
