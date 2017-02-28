# currency.py

Repository Name = currency.py

Files:

1. README.md
2. currency.py, run via terminal/shell "python3 currency.py"
    - the currency object, meets assignment standards
    - needs an amount with a symbol, or an amount and a code as parameters
    to the constructor.
3. currency_test.py run via terminal/shell "python3 currency_test_.py"
    - the test of the currency object and exception declarations
    - unittest test file
4. currency_converter.py run via terminal/shell "python 3 currency_converter.py"
    - the object which converts the currency, needs a list/dict of rates and codes to
    by constructed.
5. currency_converter_test.py run via terminal/shell "python 3 currency_converter.py"
    - the test of the converter object and its Exception declarations
    - unitttest test file

All tests passing except for one in currency_converter_test,

getting correct output but different memory addresses, trying to test convert function
with a divisor less than one.
