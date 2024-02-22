from unittest.mock import patch

from requests.exceptions import RequestException
from sat.gravity_forms import GravityForms


def test_environment_variable_error():
    try:
        gravity_forms = GravityForms()
        gravity_forms.get(
            "/forms/2/entries", params={"paging[current_page]": 1, "paging[page_size]": 5}
        )
        assert False
    except ValueError:
        assert True


def test_request_exception_get():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        mock_get.side_effect = RequestException("Simulated request exception.")
        gravity_forms = GravityForms(
            consumer_key="your_key", consumer_secret="your_secret", base_url="https://baseurl.edu"
        )
        try:
            _ = gravity_forms.get(
                "/forms/2/entries", params={"paging[current_page]": 1, "paging[page_size]": 5}
            )
            assert False
        except RequestException as e:
            assert str(e) == "Simulated request exception."


def test_get_forms_exception():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        mock_get.side_effect = RequestException("Simulated request exception.")
        gravity_forms = GravityForms(
            consumer_key="your_key", consumer_secret="your_secret", base_url="https://baseurl.edu"
        )
        try:
            _ = gravity_forms.get_forms()
            assert False
        except RequestException as e:
            assert str(e) == "Simulated request exception."


def test_get_form_exception():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        mock_get.side_effect = RequestException("Simulated request exception.")
        gravity_forms = GravityForms(
            consumer_key="your_key", consumer_secret="your_secret", base_url="https://baseurl.edu"
        )
        try:
            _ = gravity_forms.get_form("1234")
            assert False
        except RequestException as e:
            assert str(e) == "Simulated request exception."


def test_get_entries_exception():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        mock_get.side_effect = RequestException("Simulated request exception.")
        gravity_forms = GravityForms(
            consumer_key="your_key", consumer_secret="your_secret", base_url="https://baseurl.edu"
        )
        try:
            _ = gravity_forms.get_entries()
            assert False
        except RequestException as e:
            assert str(e) == "Simulated request exception."


def test_get_entry_exception():
    with patch("requests_oauthlib.OAuth1Session.get") as mock_get:
        mock_get.side_effect = RequestException("Simulated request exception.")
        gravity_forms = GravityForms(
            consumer_key="your_key", consumer_secret="your_secret", base_url="https://baseurl.edu"
        )
        try:
            _ = gravity_forms.get_entry("1234")
            assert False
        except RequestException as e:
            assert str(e) == "Simulated request exception."
