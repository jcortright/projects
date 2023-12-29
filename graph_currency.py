import matplotlib.pyplot as plt
from forex_python.converter import CurrencyRates
from datetime import datetime, timedelta

def get_historical_exchange_rates(start_date, end_date):
    c = CurrencyRates()

    dates = []
    usd_to_eur_rates = []
    usd_to_gbp_rates = []

    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)

        usd_to_eur_rates.append(c.get_rate('USD', 'EUR', date_obj=current_date))
        usd_to_gbp_rates.append(c.get_rate('USD', 'GBP', date_obj=current_date))

        current_date += timedelta(days=1)

    return dates, usd_to_eur_rates, usd_to_gbp_rates

def plot_exchange_rate_graph(dates, usd_to_eur_rates, usd_to_gbp_rates):
    date_strings = [date.strftime('%Y-%m-%d') for date in dates]

    plt.figure(figsize=(10, 6))
    plt.plot(date_strings, usd_to_eur_rates, label='USD to EUR', marker='o')
    plt.plot(date_strings, usd_to_gbp_rates, label='USD to GBP', marker='o')

    plt.title('USD to EUR and GBP Exchange Rates Over Time')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.show()

def main():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    dates, usd_to_eur_rates, usd_to_gbp_rates = get_historical_exchange_rates(start_date, end_date)
    plot_exchange_rate_graph(dates, usd_to_eur_rates, usd_to_gbp_rates)

if __name__ == "__main__":
    main()