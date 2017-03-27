import re

# Currency has a single digit symbol (code) and a value
# __init__, __add__, __subtract__, __multiply__
# raises DifferentCurrencyCodeError when different currencies
# are added or subtracted
# Currency() takes one argument, and can find the currency symbol in that argument,
# or take a symbol and a value


class DifferentCurrencyCodeError(ValueError):
    pass


class InvalidInputError(ValueError):
    pass


class Currency:
    # amount is the monetary amount passed in, e.g $2.50
    # value is a monetary amount, e.g. Currency($, 2.75)
    def __init__(self, amount, code=""):
        symbol_dict ={"USD":'$', "EUR":"€", "GBP":"£", "JPY":"¥", "KRW":"₩"}
        if type(amount) == int or type(amount) == float:
            self.val = amount
            self.code = code.upper()
            self.symbol = symbol_dict[self.code]
        else:
            self.symbol = re.sub(r'[^$£¥€₩]', '', amount)
            self.val = re.sub(r'[^0-9.]', '', amount)
            self.val = float(self.val)
            self.code = code.upper()

    # str method
    def __str__(self):
        return "{v:.2f}, {c}".format(v=self.val, c=self.code)

    # equals method
    def __eq__(self, other):
        return self.code == other.code and self.val == other.val

    # add b to self
    def __add__(self, b):
        if isinstance(b, Currency) and self.symbol == b.symbol:
            self.val += b.val
            return self.val, self.code
        else:
            raise InvalidInputError

    # subtract b from self
    def __sub__(self, b):
        if self.symbol != b.symbol:
            raise DifferentCurrencyCodeError
        if isinstance(b, Currency):
            if self.val > b.val:
                self.val -= b.val
                return "{s}{v:.2f}".format(s=self.symbol, v=self.val)
            else:
                raise InvalidInputError
        else:
            raise InvalidInputError

    # multiply self by num
    def __mult__(self, num):
        if type(num) == int or type(num) == float:
            self.val *= num
            return "{s}{v:.2f}".format(s=self.symbol,  v=self.val)
        else:
            raise TypeError
