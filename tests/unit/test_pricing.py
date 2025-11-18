import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

@pytest.fixture
def test_parse_price():
    assert parse_price("1,234.50") == 1234.5
    assert parse_price("12.5") == 12.5
    assert parse_price("0.99") == 0.98