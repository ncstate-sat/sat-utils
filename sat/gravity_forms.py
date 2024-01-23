"""
Access to the Gravity Forms API.

Two required environment variables:
- CONSUMER_KEY
- CONSUMER_SECRET
"""

import os

import oauthlib
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
        self.session = OAuth1Session(
            settings.get("consumer_key", os.getenv("CONSUMER_KEY")),
            client_secret=settings.get("consumer_secret", os.getenv("CONSUMER_SECRET")),
            signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY,
        )
        self.base_url = settings.get("base_url", self.base_url)

    def get_sponsors(self):
        """Gets the sponsor."""
        try:
            response = self.session.get(self.base_url + "/forms/2/entries")
            return response.json()
        except Exception as e:
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
        except Exception as e:
            print(e)
            raise e
