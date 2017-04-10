import currency


# init with a currency dict
# work to convert two curr first
# must take a currency, and the requested currency
# and return a currency object equal to the current currency
#
# must take a currency, covert it to requested currency, and return
# the new currency object
# must be able to use a dictionary of three or more codes_dict
# must be able to convert curr to any other curr
# raises UnknownCurrencyCodeError if there is an unknown curr


sample_dict = {'USD': 1.0, 'EUR': 0.74, 'JPY': 120, "KRW":1132, "GBP": 0.80}

class UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:

    def __init__(self, rate_dict):
        self.rate_dict = rate_dict

    def __str__(self):
        return "We will convert any currency that we know"

    def __eq__(self, other):
        return self.rate_dict == other.rate_dict

    def convert(self, currency_obj, curr_code):
        if curr_code not in self.rate_dict.keys():
            raise UnknownCurrencyCodeError
        else:
            if currency_obj.code == curr_code:
                return currency_obj
            else:
                converstion_rate = # something
                return currency.Currency(str(currency_obj.val * (self.rate_dict[curr_code] / self.rate_dict[currency_obj
                .code]), curr_code))
