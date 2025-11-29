import requests

rates = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").json()

currency = input("Введіть валюту (EUR, USD, PLN): ").upper()
amount = float(input("Введіть кількість: "))

rate = None
for item in rates:
    if item["cc"] == currency:
        rate = item["rate"]
        break

if rate is None:
    print("Невідома валюта")
else:
    print(f"{amount * rate} грн")
