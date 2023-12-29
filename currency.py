from forex_python.converter import CurrencyRates

def get_latest_exchange_rates():
    c = CurrencyRates()
    usd_to_eur = c.get_rate('USD', 'EUR')
    usd_to_gbp = c.get_rate('USD', 'GBP')
    return usd_to_eur, usd_to_gbp

def main():
    usd_to_eur, usd_to_gbp = get_latest_exchange_rates()

    print(f"Latest exchange rates:")
    print(f"USD to Euro (EUR): {usd_to_eur}")
    print(f"USD to British Pound (GBP): {usd_to_gbp}")

    # Simple comparison
    if usd_to_eur < usd_to_gbp:
        print("It's cheaper to convert USD to Euro.")
    elif usd_to_eur > usd_to_gbp:
        print("It's cheaper to convert USD to British Pound.")
    else:
        print("The exchange rates are the same.")

if __name__ == "__main__":
    main()