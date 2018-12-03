import requests
import sqlite3
import datetime
from lxml import html



time = datetime.datetime.now().strftime("%d-%m-%Y")
file = open('report.txt', 'w+')




def main():
    # page = requests.get('http://jcabello.me/test.html')
    page = requests.get('https://www.milanuncios.com/mazda-mx-5-de-segunda-mano/?fromSearch=1&hasta=10000&demanda=n&anod=2005&potencia=200')
    dataFromWebsite = getData(page)

    #print(cleanMilanuncios(dataFromWebsite["key"]))

    for key, value in dataFromWebsite.items():   
        value = cleanMilanuncios(value)
        file.write(value + "\n")
        #insertInDb(key, value)
        print(value)

def createCar():
    pass

def insertInDb(key, value):
    try:
        print(key, value + "\n")
        dbConnection = sqlite3.connect("mx5.db", check_same_thread=False)
        dbCursor = dbConnection.cursor()
        dbCursor.execute("INSERT INTO main ('key', 'key') VALUES(?,?)", (key, value))
    except UnboundLocalError:
        print("fail")
    finally:
        dbConnection.close()


def getData(page):
    tree = html.fromstring(page.content)
    key = tree.xpath('//div[@class="x5"]/text()'),
    title = tree.xpath('//a[@target="_blank"]/text()'),
    description = tree.xpath('//div[@class="tx"]/text()'),
    price = tree.xpath('//div[@class="aditem-price"]/text()'),
    km = tree.xpath('//div[@class="kms tag-mobile"]/text()'),
    year = tree.xpath('//div[@class="gas tag-mobile"]/text()'),
    hp = tree.xpath('//div[@class="cc tag-mobile"]/text()'),

    listOfItems = {
            "key": key,
            "title": title,
            #"description": description,
            "price": price,
            "km": km,
            "year": year,
            "hp": hp
        }
    return(listOfItems)


def cleanMilanuncios(list):
        x = str(list)
        x = x.strip("[(")
        x = x.replace("\\n", "")
        x = x.replace("'", "")
        x = x.replace("            ", "")
        x = x.replace("         ", "")
        x = x.replace("],)", "")
        x = x.replace(", Contacta con milanuncios, , ,, , ,, , ,, , ,, CONTACTAR, Schibsted, vibbo.com, infojobs.net, fotocasa, habitaclia.com, coches.net, motos.net", "")
        return(x)


if __name__ == '__main__':
    main()
