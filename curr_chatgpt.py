import requests
from currency_api import currency_api

from_cur = input("Convert from currency: ").upper()
to_cur = input("Convert to currency: ").upper()

amount = float(input("Enter amount to convert: "))
while amount <= 0:
    print("Amount must be more than zero.")
    amount = float(input("Enter amount to convert: "))

url = f"https://api.apilayer.com/fixer/convert?to={to_cur}&from={from_cur}&amount={amount}"
headers = currency_api()

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Sorry, there is a problem. Please try again later.")
else:
    result = response.json()
    print(f"The converted amount is {result['result']} in {to_cur}.")
