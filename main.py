import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://api.freecurrencyapi.com/api/v1/latest?base_currency={base_currency}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data.get(target_currency, {}).get("value")
    return exchange_rate

base_currency = input("Введите код базовой валюты (например, USD): ")
target_currency = input("Введите код целевой валюты (например, RUB): ")
api_key = "ВАШ_API_КЛЮЧ"
exchange_rate = get_exchange_rate(base_currency, target_currency, api_key)
print(f"1 {base_currency} = {exchange_rate:.2f} {target_currency}")
