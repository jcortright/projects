from forex_python.converter import CurrencyRates

def get_latest_exchange_rates():
    c = CurrencyRates()
    usd_to_eur = c.get_rate('USD', 'EUR')
    usd_to_gbp = c.get_rate('USD', 'GBP')
    return usd_to_eur, usd_to_gbp

def main():
    usd_to_eur, usd_to_gbp = get_latest_exchange_rates()

    print("Latest exchange rates:")
    print(f"USD to Euro (EUR): {usd_to_eur:.2f} USD")
    print(f"USD to British Pound (GBP): {usd_to_gbp:.2f} USD")

    # Calculate the cost to buy 1 Euro and 1 British Pound in USD
    cost_to_buy_1_eur = 1 / usd_to_eur
    cost_to_buy_1_gbp = 1 / usd_to_gbp

    print(f"To buy 1 Euro, it would cost {cost_to_buy_1_eur:.2f} USD")
    print(f"To buy 1 British Pound, it would cost {cost_to_buy_1_gbp:.2f} USD")

if __name__ == "__main__":
    main()

#written with chatgpt