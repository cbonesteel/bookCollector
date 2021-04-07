import requests
import mysql.connector
from random import randrange
import databaseConnector as db
import pandas

colNames = ['isbn', 'title', 'author', 'year']
data = pandas.read_csv('books.csv', names=colNames)

isbns = data.isbn.tolist()

isbns.pop(0)

for k in isbns:

    url = "https://www.googleapis.com/books/v1/volumes?q={isbn}".format(isbn=k)

    response = requests.get(url)

    dictionary = response.json()

    try:
        for i in dictionary.get("items"):
            try:
                # Gets standard book information (i.e. title, authors, etc.)
                if isinstance(i.get("volumeInfo").get("categories"), list):
                    cat = ""
                    for j in i.get("volumeInfo").get("categories"):
                        cat += j + " "
                else:
                    cat = "None"

                authors = ""
                for j in i.get("volumeInfo").get("authors"):
                    authors += j + " "

                if i.get("volumeInfo").get("edition") == "null":
                    edition = 1
                else:
                    edition = i.get("volumeInfo").get("edition")

                ISBN = i.get("volumeInfo").get("industryIdentifiers")[0].get("identifier")
                title = i.get("volumeInfo").get("title")
                publisher = i.get("volumeInfo").get("publisher")
                date = i.get("volumeInfo").get("publishedDate")
                rating = i.get("volumeInfo").get("averageRating")
                cover = i.get("volumeInfo").get("imageLinks").get("thumbnail")
                description = i.get("volumeInfo").get("description")

                if len(ISBN) > 13:
                    raise TypeError

                quantity = randrange(50)

                if quantity == 0:
                    available = "1"
                else:
                    available = "0"

                if type(i.get("saleInfo").get("retailPrice")) == dict:
                    buyPrice = i.get("saleInfo").get("retailPrice").get("amount")
                else:
                    buyPrice = 9.99

                if type(i.get("saleInfo").get("listPrice")) == dict:
                    sellPrice = i.get("saleInfo").get("listPrice").get("amount")
                else:
                    sellPrice = 19.99

                db.query(
                    "INSERT INTO Books (ISBN, Category, Author, Title, Edition, Publisher, PublicationYear, Rating, CoverPicture, Description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (ISBN, cat, authors, title, edition, publisher, date[0:4], rating, cover, description)
                )

                selectID = "SELECT BookID FROM Books WHERE ISBN={isbn}".format(isbn=ISBN)

                bookID = db.query(selectID)

                db.query(
                    "INSERT INTO Inventory (BookID, Quantity, MinThreshold, BuyPrice, SellPrice, BookStatus) VALUES (%s, %s, %s, %s, %s, %s)",
                    (bookID[0][0], quantity, "2", buyPrice, sellPrice, available)
                )

                db.commit()

                # increments bookID for inventory information foreign key
            except KeyError:
                print("Key Error, moving to next book")
            except AttributeError:
                print("Attribute Error, moving to next book")
            except TypeError:
                print("Type Error, moving to next book")
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
    except TypeError:
        print("Type Error, moving to next book")