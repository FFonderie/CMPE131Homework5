import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total
from src.order_io import load_order, write_receipt

def test_order_integration(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\ndoodad,100\ncontraption,$-20.", encoding="utf-8")

    items = load_order(input_file)
    write_receipt(tmp_path / "receipt.txt", items, discount_percent=10, tax_rate=0.1)

    output_text = (tmp_path / "receipt.txt").read_text(encoding="utf-8")
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    assert "doodad: $100.00" in output_text
    assert "contraption: $-20" in output_text
    assert "TOTAL:" in output_text


    input_file.write_text("\ndoohickey,$100,000")
    with pytest.raises(ValueError):
        load_order(input_file)