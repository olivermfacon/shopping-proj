from app.shopping import to_usd

def test_to_usd():
    result = to_usd(5)
    assert result == "$5.00"
    result = to_usd(2100.1)
    assert result == "$2,100.10"
    result = to_usd(21.99)
    assert result == "$21.99"