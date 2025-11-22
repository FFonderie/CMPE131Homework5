import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

def test_parse_price():
    assert parse_price("1,234.50") == 1234.5
    assert parse_price("$1,234.50") == 1234.5
    assert parse_price("12.5") == 12.5
    assert parse_price("0.99") == 0.99
    with pytest.raises(ValueError):
        parse_price("abc")
    assert parse_price("12,34,50") == 123450 # not sure if this should be

# trying out mark.parameterize
@pytest.mark.parametrize("price, expOut", [
    (2, "$2.00"),
    (2.00, "$2.00"),
    (200, "$200.00"),
    (2.0000, "$2.00"),
    ])
def test_format_currency(price, expOut):
    assert format_currency(price) == expOut
    with pytest.raises(ValueError):
        parse_price("abc")

def test_appy_discount():
    with pytest.raises(ValueError):
        apply_discount(100, -1)
        apply_discount("abc", 0.5)
    assert apply_discount(100, 0.25) == 75
    assert apply_discount(100, 1) == 0
    assert apply_discount(100, 2) == -100 # wrong, now you get paid
    assert apply_discount(100, 25) == -2400 # same problem

def test_add_tax():
    with pytest.raises(TypeError):
        add_tax("abc")
    with pytest.raises(ValueError):
        add_tax(100, -0.05)
    assert add_tax(100) == 107
    assert add_tax(100, 0.09) == pytest.approx(109)
    assert add_tax(0, 0.09) == 0
    assert add_tax(100, 0) == 100
    assert add_tax(100, 1) == 200

def test_bulk_total():
    goodPrices = [1, 2, 100, 200]
    badPrices = [1, 2, 100, "abc"]
    goodDiscount = 0.25
    badDiscount = -0.5
    wrongDiscount = 2
    goodTax = 0.09
    badTax = -0.05
    assert bulk_total(goodPrices) == pytest.approx(324.21)
    assert bulk_total(goodPrices, goodDiscount, goodTax) ==  pytest.approx(247.7025)
    assert bulk_total(goodPrices, wrongDiscount) ==  pytest.approx(-324.21)
    with pytest.raises(ValueError):
        assert bulk_total(badPrices, goodDiscount, goodTax)
        assert bulk_total(goodPrices, badDiscount, goodTax)
        assert bulk_total(goodPrices, goodDiscount, badTax)