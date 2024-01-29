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


def test_request_exception_get():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        gravity_forms = GravityForms(
            consumer_key="your_key", consumer_secret="your_secret", base_url="https://baseurl.edu"
        )
        mock_get.side_effect = RequestException("Simulated request exception.")
        # with pytest.raises(RequestException) as ex:
        #     gravity_forms.get("/forms")
        try:
            gravity_forms.get("/forms")
        except RequestException as ex:
            # Asserting that the error message in the caught exception matches the simulated one
            assert str(ex) == "Simulated request exception."
        else:
            # If no exception is raised, fail the test
            pytest.fail("Expected RequestException but no exception was raised.")
    # assert "Simulated request exception." in str(ex.value)
