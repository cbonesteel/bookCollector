import csv
import pandas

colNames = ['isbn', 'title', 'author', 'year']
data = pandas.read_csv('books.csv', names=colNames)

isbns = data.isbn.tolist()

