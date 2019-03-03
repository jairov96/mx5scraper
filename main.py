import requests
import json
import re

from bs4 import BeautifulSoup


def clean_key_string(string_):
    """Cleans the "key" in milanuncios."""

    cleaner = re.compile("[a-z][0-9]{1,10}")
    clean_string = cleaner.findall(string_)[0]

    return(clean_string)


def get_website(url):
    soup = BeautifulSoup(url.content, "html.parser")

    return(soup)


def generate_list_of_cars(soup):

    keys = soup.find_all('div', attrs={'class': 'x5'})
    names = soup.find_all('a', attrs={'class': 'aditem-detail-title'})
    prices = soup.find_all('div', attrs={'class': 'aditem-price'})
    # descriptions = soup.find_all('div', attrs={'class': 'tx'})
    kms = soup.find_all('div', attrs={'class': 'kms tag-mobile'})
    years = soup.find_all('div', attrs={'class': 'gas tag-mobile'})
    hps = soup.find_all('div', attrs={'class': 'cc tag-mobile'})

    car_list = []
    for i in range(0, len(keys)):
        car = {
            str(clean_key_string(keys[3].text)): {
                "name": names[i].text,
                "price": prices[i].text,
                # "description": descriptions[i].text,
                "km": kms[i].text,
                "year": years[i].text,
                "hp": hps[i].text
            }
        }
        car_list.append(car)

    return(car_list)


def print_car_list(car_list):
    for car in car_list:
        print(car)
        print("\n")


def write_json_file(json_data):
    with open('data.json', 'w') as file:
        file.write(json_data)


def update_price(car_list):
    """Checks of price of a car is lower than on the DB, if so, updates it"""
     
    with open('data.json', 'r') as current_data:
        current_data = json.load(current_data)
        for each 
    return()


def main():
    url = requests.get('http://jcabello.me/test.html')
    soup = get_website(url)  # Soup is the web scrapper library, BeautifulSoup.
    car_list = generate_list_of_cars(soup)

    # json_data = json.dumps(car_list)

    # write_json_file(json_data)

    update_price(car_list)

    # print(json_data)


if __name__ == "__main__":
    main()
