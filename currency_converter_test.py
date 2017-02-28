import unittest
import currency

from currency_converter import CurrencyConverter
from currency_converter import UnknownCurrencyCodeError


# test suite for currency_converter

class TestCurrencyConverter(unittest.TestCase):
    # set up tests
    def setUp(self):
        self.currency_a = currency.Currency(500, "USD")
        self.currency_b = currency.Currency(7, "GBP")
        self.currency_c = currency.Currency(10, "KRW")
        self.currency_d = currency.Currency(2100, "JPY")
        self.curr_converter = CurrencyConverter({'USD': 1.0,
        'EUR': 0.74, 'JPY': 120, "KRW":1132, "GBP": 0.80})
        self.other_curr_converter = CurrencyConverter({"USD": 1.0, "EUR": 0.74})

    # test string method
    def test_currency_converter_str(self):
        self.assertEqual(self.curr_converter.__str__(), "We will convert any currency that we know")

    def test_currency_converter_eq(self):
        self.assertTrue(self.curr_converter.__eq__(self.curr_converter))

    def test_currency_converter_not_eq(self):
        self.assertFalse(self.curr_converter.__eq__(self.other_curr_converter))

    def test_currency_converter_convert_same_code(self):
        self.assertEqual(self.curr_converter.convert(self.currency_a, "USD"), self.currency_a)

    def test_currency_converter_convert_rate_grtr_thn_1(self):
        self.assertEqual(self.curr_converter.convert(self.currency_d, "KRW"), currency.Currency(2377200.00, "KRW"))

    def test_currency_converter_convert_rate_lss_thn_1(self):
        self.assertEqual(self.curr_converter.convert(self.currency_c, "EUR"), currency.Currency(13.52, "EUR"))

    def test_currency_converter_unknown_currency_error(self):
        with self.assertRaises(UnknownCurrencyCodeError):
            self.curr_converter.convert(self.currency_b, "AUD")


if __name__ == '__main__':
    unittest.main()
