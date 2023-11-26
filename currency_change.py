import requests
from currency_api import currency_api
from_cur = input("what's the currency you want to convert from?:\n").upper()
to_cur = input("what's the currency you want to convert to?:\n").upper()

while True:
    try:
        amount = float(input("how much you want to convert?:\n"))
    except:
        print("the ammount must be a numeric value")
        continue
    if amount == 0 :
        print("The amount must be more than zero")
        continue
    else:
        break
url = f"https://api.apilayer.com/fixer/convert?to={to_cur}&from={from_cur}&amount={amount}"

payload = {}
headers= currency_api()
response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if status_code != 200 :
    print("sorry there is a problem, try again later")
    quit()
result = response.json()
print(f"The amount in {to_cur} is {result['result']}")
