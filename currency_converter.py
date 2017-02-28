from currency import Currency


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

# codes_dict = {'$': "USD", "£":'GBP', "¥":'JPY', "€":"EUR", "₩":"KRW"}
sample_dict = {'USD': 1.0, 'EUR': 0.74}

class UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:

    def __init__(self, curr_dict):
        self.curr_dict = curr_dict
        for key, value in self.curr_dict:
            self.code = curr_dict[key]
            self.rate = curr_dict[value]
        self.new_amount = 0

    def convert(self, currency_obj, currency_to_be_converted):
            if currency_to_be_converted not in self.curr_dict:
                raise UnknownCurrencyCodeError
            else:
                if currency_obj.code == key:
                    return currency_obj
                else:
                    self.new_amount = round(currency_obj.val, 2) * value
        return Currency(self.new_amount, currency_to_be_converted)


c = Currency("500", "USD")
print(CurrencyConverter(sample_dict))
print(CurrencyConverter.convert(c, "GBP"))
