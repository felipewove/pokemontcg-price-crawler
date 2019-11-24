import sys

import pytest

from util import parse_price

sys.path.append("..")


class TestMoney:
    def test_parse_price_correct_cases(self):
        assert parse_price("R$ 123,55 ") == "123.55"
        assert parse_price("R$ 12,55 ") == "12.55"
        assert parse_price("R$ 2,55 ") == "2.55"
        assert parse_price("R$ 0,55 ") == "0.55"
        assert parse_price("R$ 0,50 ") == "0.50"
        assert parse_price("R$ 0,05 ") == "0.05"
        assert parse_price("R$ 0,00 ") == "0.00"

        assert parse_price("USD 123,55 ") == "123.55"
        assert parse_price("USD$ 123,55 ") == "123.55"
        assert parse_price("$ 123,55 ") == "123.55"

    def test_parse_price_unusual_but_ok(self):
        assert parse_price("R$ 123.55 ") == "123.55"
        assert parse_price("123,55 ") == "123.55"
        assert parse_price("123.55 ") == "123.55"

    def test_parse_price_when_ligapokemon_fix_themselves(self):
        assert parse_price("R$ 123,55") != "123.55"
        assert parse_price("123,55") != "123.55"
        assert parse_price("123.55") != "123.55"
