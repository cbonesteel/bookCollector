import requests
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

    bookID = 17

    # books = open('books.txt', 'w')
    # inventory = open('inventory.txt', 'w')

    for i in dictionary.get("items"):
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

        print(ISBN)
        
        db.query(
            "INSERT INTO Books (ISBN, Category, Author, Title, Edition, Publisher, PublicationYear, Rating, CoverPicture, Description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (ISBN, cat, authors, title, edition, publisher, date[0:4], rating, cover, description)
        )

        db.commit()
    
        # Prints standard book information to books text file
        # print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %
        #       (ISBN, cat, authors, title, edition, publisher, date[0:4], rating, cover, description), file=books)

        # Gets inventory information for a book (i.e. prices, quantity in stock, etc.)
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
            "INSERT INTO Inventory (BookID, Quantity, MinThreshold, BuyPrice, SellPrice, BookStatus) VALUES (%s, %s, %s, %s, %s, %s)",
            (bookID, quantity, "2", buyPrice, sellPrice, available)
        )

        db.commit()
    
        # Prints inventory information to inventory text file
        # print('%s\t%s\t%s\t%s\t%s\t%s' % (bookID, quantity, "2", buyPrice, sellPrice, available), file=inventory)

        # increments bookID for inventory information foreign key
        bookID = bookID + 1
