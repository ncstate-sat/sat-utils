from sat.gravity_forms import GravityForms


def test_get_sponsors():
    response = GravityForms.get_sponsors()
    assert len(response) > 0


def test_get_card_requests():
    response = GravityForms.get_cards_requested()
    assert len(response) > 0
