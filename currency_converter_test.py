import unittest
import Currency
from currency_converter import __str__
from currency_converter import __eq__
from currency_converter import convert
from currency_converter import UnknownCurrencyCodeError


# test suite for currency_converter

class CurrencyConverterTest:
    # set up tests
    def setUp(self):
        self.currency_a = Currency("500", "USD")
        self.currency_b = Currency("7", "GBP")
        self.currency_c = Currency("10", "KRW")
        self.currenct_d = Currency("2100", "JPY")
        self.curr_conveter = CurrencyConverter({'USD': 1.0,
        'EUR': 0.74, 'JPY': 120, "KRW":1132, "GBP": 0.80})

    # test string method
    def test_currency_converter_str(self):
        self.assertEqual(self.curr_conveter.__str__(), "We will convert any currency that we know")

    def test_currency_converter_eq(self):
        pass

    def test_currency_converter_not_eq(self):
        pass

    def test_currency_converter_convert_same_code(self):
        pass

    def test_currency_converter_convert_small_to_big(self):
        pass

    def test_currency_converter_convert_big_to_small(self):
        pass

    def test_currency_converter_convert_invalid_input(self):
        pass

    def test_currency_converter_unknown_currency_error(self):
        pass


if __name__ == '__main__':
    unittest.main()
