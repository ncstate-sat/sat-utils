"""
Access to the Gravity Forms API.

Two required environment variables:
- CONSUMER_KEY
- CONSUMER_SECRET
"""

import os

import oauthlib
from requests.exceptions import RequestException
from requests_oauthlib import OAuth1Session


class GravityForms:
    """
    A helper class for connecting to and calling the Gravity Forms API.
    """

    session = None
    base_url = "https://onecard.ncsu.edu/wp-json/gf/v2"

    def __init__(self, **settings) -> None:
        """
        Configure the connection to Gravity Forms.

        Optional Parameters:
        - consumer_key: Key for accessing the Gravity Forms API.
        - consumer_secret: Secret for authenticating with the Gravity Forms API.
        - base_url: An alternate base URL, if different than the default.
        """
        consumer_key = settings.get("consumer_key", os.getenv("CONSUMER_KEY"))
        consumer_secret = settings.get("consumer_secret", os.getenv("CONSUMER_SECRET"))

        if not consumer_key:
            raise RuntimeError(
                "A consumer_key is required as either an environment variable or parameter."
            )

        if not consumer_secret:
            raise RuntimeError(
                "A consumer_secret is required as either an environment variable or parameter."
            )

        self.session = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY,
        )
        self.base_url = settings.get("base_url", self.base_url)

    def get_sponsors(self):
        """Gets the sponsor."""
        try:
            response = self.session.get(self.base_url + "/forms/2/entries")
            return response.json()
        except RequestException as e:
            print(e)
            raise e

    def get_cards_requested(self):
        """Gets requested cards."""
        response = self.session.get(self.base_url + "/forms/3/entries")
        return response.json()

    def get(self, endpoint: str):
        """
        Submits a GET request to a specified endpoint.

        Parameters:
        - endpoint: The string representing the endpoint URL. (ex. "/forms")
        """
        try:
            response = self.session.get(self.base_url + endpoint)
            return response.json()
        except RequestException as e:
            print(e)
            raise e
