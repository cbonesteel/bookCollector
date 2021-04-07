import requests
from random import randrange
import pandas

colNames = ['isbn', 'title', 'author', 'year']
data = pandas.read_csv('books.csv', names=colNames)

isbns = data.isbn.tolist()

counter = 0

for k in isbns:
    url = "https://www.googleapis.com/books/v1/volumes?q={isbn}".format(isbn=k)

    response = requests.get(url)

    dictionary = response.json()

    for i in dictionary.get("items"):
        try:
            ISBN = i.get("volumeInfo").get("industryIdentifiers")[0].get("identifier")
            title = i.get("volumeInfo").get("title")
            publisher = i.get("volumeInfo").get("publisher")
            date = i.get("volumeInfo").get("publishedDate")
            rating = i.get("volumeInfo").get("averageRating")
            cover = i.get("volumeInfo").get("imageLinks").get("thumbnail")
            description = i.get("volumeInfo").get("description")

            print("Iteration %d: book saved" % counter)
        except KeyError:
            print("Iteration %d: key error, moving to next book")
        except AttributeError:
            print("Iteration %d: attribute error, moving to next book")
        except TypeError:
            print("Iteration %d: type error, moving to next book")

        counter = counter + 1
