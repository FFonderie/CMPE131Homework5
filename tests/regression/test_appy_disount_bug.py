import pytest
from src.pricing import apply_discount

def test_apply_discount_bug():
    with pytest.raises(AssertionError):
        assert apply_discount(100, 100) == 0 # 100% off is $0
        assert apply_discount(100, 200) == 0 # 200% off is also 0$ (you should not get paid)