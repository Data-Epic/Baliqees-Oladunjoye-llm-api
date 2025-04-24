import pytest
from CSA import CustomerSupportAssistant

@pytest.fixture
def assistant():
    return CustomerSupportAssistant()

def test_get_response_valid_input(assistant):
    response = assistant.get_response("What products do you have?")
    assert isinstance(response, str)
    assert any(product in response.lower() for product in ["chicken", "meat", "fish", "snail"])

def test_get_response_empty_input(assistant):
    response = assistant.get_response("")
    assert isinstance(response, str)
    assert response != ""  # Should return something, even if it's a polite prompt

def test_get_response_unusual_question(assistant):
    response = assistant.get_response("Do you sell dragons?")
    assert isinstance(response, str)
    assert "we don't sell dragons" in response.lower()

def test_get_response_normal_enquiry(assistant):
    response = assistant.get_response("Do you sell smoked chicken?")
    assert isinstance(response, str)
    assert "smoked chicken" in response.lower()
    assert "yes" in response.lower() or "we offer" in response.lower()

