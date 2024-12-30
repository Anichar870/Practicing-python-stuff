import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rates(base_currency):
    """
    Fetch live exchange rates from the API.
    :param base_currency: The base currency for conversion.
    :return: A dictionary of exchange rates.
    """
    try:
        response = requests.get(f"{API_URL}?base={base_currency}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    """
    Convert an amount between two currencies using exchange rates.
    :param amount: Amount to convert.
    :param from_currency: The currency to convert from.
    :param to_currency: The currency to convert to.
    :param rates: A dictionary of exchange rates.
    :return: Converted amount.
    """
    if from_currency == rates['base']:
        rate = rates['rates'].get(to_currency)
        if rate:
            return amount * rate
    else:
        print(f"Conversion from {from_currency} not supported in this version.")
    return None

def main():
    print("Welcome to the Currency Converter!")
    base_currency = "USD"
    rates = get_exchange_rates(base_currency)
    
    if not rates:
        print("Could not fetch exchange rates. Please try again later.")
        return

    print("\nAvailable Currencies:")
    print(", ".join(rates['rates'].keys()))

    from_currency = input("\nEnter the currency to convert from (default USD): ") or "USD"
    to_currency = input("Enter the currency to convert to: ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        if converted_amount:
            print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            print("Conversion failed. Please check your inputs.")
    except ValueError:
        print("Invalid amount entered.")

if __name__ == "__main__":
    main()
