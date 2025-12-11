import requests


def main():
    # Get series information for KXHIGHNY
    url = "https://api.elections.kalshi.com/trade-api/v2/series/KXHIGHNY"
    response = requests.get(url)
    series_data = response.json()

    print(f"Series Title: {series_data['series']['title']}")
    print(f"Frequency: {series_data['series']['frequency']}")
    print(f"Category: {series_data['series']['category']}")


if __name__ == "__main__":
    main()
