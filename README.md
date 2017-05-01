# currency.py

Using classes and unittest, build a currency converter.

For my portfolio and contact info, please visit me: [Will Warren](https://willwile4.github.io)

## Requirements
CURRENCY OBJECTS

* Must be created with an amount and a currency code.
* Must equal another Currency object with the same amount and currency code.
* Must NOT equal another Currency object with different amount or currency code.
* Must be able to be added to another Currency object with the same currency code.
* Must be able to be subtracted by another Currency object with the same currency code.
* Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.
* Must be able to be multiplied by an int or float and return a Currency object.
Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.

CURRENCYCONVERTER OBJECTS
* Must be initialized with a dictionary of currency codes to conversion rates (see link to rates below).
* At first, just make this work with two currency codes and conversation rates, with one rate being 1.0 and the other being the conversation rate. An example would be this: {'USD': 1.0, 'EUR': 0.74}, which implies that a dollar is worth 0.74 euros.
* Must be able to take a Currency object and a requested currency code that is the same currency code as the Currency object's and return a Currency object equal to the one passed in. That is, currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD').
* Must be able to take a Currency object that has one currency code it knows and a requested currency code and return a new Currency object with the right amount in the new currency code.
* Must be able to be created with a dictionary of three or more currency codes and conversion rates. An example would be this: {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}, which implies that a dollar is worth 0.74 euros and that a dollar is worth 120 yen, but also that a euro is worth 120/0.74 = 162.2 yen.
* Must be able to convert Currency in any currency code it knows about to Currency in any other currency code it knows about.
* Must raise an UnknownCurrencyCodeError when you try to convert from or to a currency code it doesn't know about.

## Objectives
* Understand how to override mathematical operators.
* Understand how objects can return objects of other classes as responses to messages.
* Understand how to execute Python code which spans multiple files.
* Understand how to create your own exception classes.
* Be able to initialize an object from a set of parameters.
* Be able to initialize a set of objects from a complex data structure.
* Be able to raise exceptions/errors as appropriate.
* Be able to parse strings to isolate specific symbols.


## How To Run:
1. Make sure python3 is installed on your computer.
2. Clone this Repository
3. Switch into that newly cloned Repository.
4. Run the tests using unittest

## Files
1. README.md
2. currency.py, run via terminal/shell "python3 currency.py"
    - the currency object, meets assignment standards
    - needs an amount with a symbol, or an amount and a code as parameters
    to the constructor.
3. currency_test.py run via terminal/shell "python3 currency_test_.py"
    - the test of the currency object and exception declarations
4. currency_converter.py run via terminal/shell "python 3 currency_converter.py"
    - the object which converts the currency, needs a list/dict of rates and codes to
    by constructed.
5. currency_converter_test.py run via terminal/shell "python 3 currency_converter.py"
    - the test of the converter object and its Exception declarations

### Notes

- All tests passing except for one in currency_converter_test,

- Getting correct output but different memory addresses, trying to test convert function
with a divisor less than one.
