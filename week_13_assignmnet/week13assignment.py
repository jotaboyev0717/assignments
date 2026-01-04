import requests
import json

url = "https://api.coingecko.com/api/v3/coins/markets"


def get_crypto_data(limit):
    try:
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": limit,
            "page": 1
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            raise Exception("API error: " + str(response.status_code))

        return response.json()

    except Exception as e:
        raise e


def sort_by_price(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j]["current_price"] > data[i]["current_price"]:
                data[i], data[j] = data[j], data[i]
    return data


def sort_by_change(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j]["price_change_percentage_24h"] > data[i]["price_change_percentage_24h"]:
                data[i], data[j] = data[j], data[i]
    return data


def process_data(data, choice):
    if not data:
        print("No data received.")
        return []

    if choice == "1":
        return sort_by_price(data)
    elif choice == "2":
        return sort_by_change(data)
    else:
        print("Invalid sorting choice.")
        return []


def display_results(data):
    if not data:
        print("No results found.")
        return

    print("\nCrypto Market Analysis\n")
    for coin in data:
        print("Name:", coin["name"])
        print("Price:", coin["current_price"])
        print("24h Change:", coin["price_change_percentage_24h"])
        print("------------------------------")


def save_to_file(data):
    try:
        file = open("crypto_results.txt", "w")
        for coin in data:
            file.write(
                coin["name"] + " | Price: " +
                str(coin["current_price"]) + " | 24h Change: " +
                str(coin["price_change_percentage_24h"]) + "\n"
            )
        file.close()
    except Exception:
        raise Exception("File writing failed")


def main():
    try:
        limit = int(input("Enter number of cryptocurrencies (1-50): "))
        if limit < 1 or limit > 50:
            print("Invalid number.")
            return

        print("\nChoose sorting method:")
        print("1. Highest price")
        print("2. Highest 24h change")

        choice = input("Enter 1 or 2: ")

        data = get_crypto_data(limit)
        processed_data = process_data(data, choice)

        display_results(processed_data)
        save_to_file(processed_data)

    except Exception as e:
        print("Program stopped:", e)


main()
