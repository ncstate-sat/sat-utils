import pytest
from sat.models.ccure.access import Clearance, Credential


@pytest.fixture
def clearance():
    def _clearance(multiple: int = None):
        clearance = {
            "name": "John Doe",
            "object_id": 1234,
            "guid": "12345678-1234-1234-1234-123456789012",
        }
        if multiple:
            return [Clearance(**clearance) for _ in range(multiple)]
        else:
            return Clearance(**clearance)

    return _clearance


@pytest.fixture
def credential():
    def _credential(multiple: int = None):
        credential = {
            "card_number": 1234567890,
            "patron_id": 1234567890,
        }
        if multiple:
            return [Credential(**credential) for _ in range(multiple)]
        else:
            return Credential(**credential)

    return _credential
