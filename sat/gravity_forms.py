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

    @classmethod
    def get_session(cls) -> OAuth1Session:
        """Gets the existing authenticated session."""
        if cls.session is None:
            session = OAuth1Session(
                os.getenv("CONSUMER_KEY"),
                client_secret=os.getenv("CONSUMER_SECRET"),
                signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY,
            )

        return session

    @classmethod
    def get_sponsors(cls):
        """Gets the sponsor."""
        session = cls.get_session()
        response = session.get("https://onecard.ncsu.edu/wp-json/gf/v2/forms/2/entries")

        return response.json()

    @classmethod
    def get_cards_requested(cls):
        """Gets requested cards."""
        session = cls.get_session()
        response = session.get("https://onecard.ncsu.edu/wp-json/gf/v2/forms/3/entries")

        return response.json()
