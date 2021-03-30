# bookCollector

## Project Description
This project is to assist with a term long course project. The script runs
through a long list of isbn's and calls the Google Books API. Certain
book information is then pulled from the api call and immediatly entered
into the database. The original plan was to make a text file and upload
it that way but some issues were encountered with this method. The
code still exists and can be easily switched to if needed.

## File Explanations

* app.py - The original python script that still uses the text file output
method. Currently used for some testing but will likely be the final
version of the script.

* bookCollector.py - The updated script that uses the databaseConnector
to query our database. Currently being used for testing database insertion.

* csvReader.py - A stray file I used for learning how to use csv files :)

* databaseConnector.py - Our main app's database connector to allow
query testing.

* books.csv - The primary list of books used to call the api based on ISBN.

* books.txt - The primary book information output.

* inventory.txt - The inventory information output.
