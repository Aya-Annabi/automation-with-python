import requests
from bs4 import BeautifulSoup

API_KEY = 'YOUR-API-KEY-HERE'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def fetch_tnd_to_usd():
    # Get the value of the dinnar in dollars on Google Finance to obtain the real value, which may change. 
    url = 'https://www.google.com/finance/quote/TND-USD?sa=X&ved=2ahUKEwi97eHfy7GHAxXzTKQEHYXsCxYQmY0JegQICRAw'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Assuming the rate is found in a div with class "YMlKec fxKbKc"
    rate_text = soup.find("div", {"class": "YMlKec fxKbKc"}).text
    tnd_to_usd = float(rate_text.replace('$', ''))
    
    return tnd_to_usd

def convert_currency(amount_in_usd):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency=USD&currencies={currencies}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'data' in data:
            conversion_rates = data["data"]
            converted_values = {currency: amount_in_usd * rate for currency, rate in conversion_rates.items()}
            return converted_values
        else:
            print("Error: 'data' key not found in the response.")
            print("Response received:", data)
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    tnd_to_usd_rate = fetch_tnd_to_usd()
    print(f"1 TND = {tnd_to_usd_rate} USD")
    
    while True:
        tnd_amount = input("Enter the amount in TND (q to quit): ").strip().upper()
        
        if tnd_amount == 'Q':
            break
        
        try:
            tnd_amount = float(tnd_amount)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        usd_amount = tnd_amount * tnd_to_usd_rate
        conversions = convert_currency(usd_amount)
        
        if not conversions:
            continue
        
        print(f"{tnd_amount} TND is equivalent to:")
        for currency, value in conversions.items():
            print(f"{value:.2f} {currency}")

if __name__ == "__main__":
    main()
