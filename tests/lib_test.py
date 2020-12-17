from bbquotes.lib import quotes

def test_quotes():
    response = quotes()

    assert response[:5] == "QUOTE"
