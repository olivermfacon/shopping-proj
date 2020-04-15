import datetime
from app.shopping import to_usd
from app.shopping import human_friendly_timestamp

def test_to_usd():
    result = to_usd(5)
    assert result == "$5.00"
    result = to_usd(2100.1)
    assert result == "$2,100.10"
    result = to_usd(21.99)
    assert result == "$21.99"

def test_human_friendly_message():
    result = human_friendly_timestamp(datetime.datetime(2020, 4, 15, 14, 19, 11, 609990))
    assert result == "2020-04-15 14:19:11"