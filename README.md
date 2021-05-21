# bookCollector

## Project Description
This project is to assist with a term long course project. The script runs
through a long list of isbn's and calls the Google Books API. Certain
book information is then pulled from the api call and immediatly entered
into the database. The original plan was to make a text file and upload
it that way but some issues were encountered with this method. The
code still exists and can be easily switched to if needed.

## File Explanations

* README.md - This readme.

* app.py - The original python script that still uses the text file output
method. Only being used to test parse and error functionality. Does not function
entirely as intended.

* bookCollector.py - The updated script that uses the databaseConnector
to query our database. This script makes many api calls based on a list
of isbns generated from books.csv. It then error checks to ensure the api
returns all the information required by our system. If it does not, it simply
skips that entry and moves onto the next entry as incomplete information is
useless to us. There are so many isbns and calls that we still get a substantial
return volume from the script.

* databaseConnector.py - Our main app's database connector to allow
queries to be called to add the books directly to our database.

* books.csv - The primary list of books used to call the api based on ISBN.

* books.txt - The primary book information output.

* inventory.txt - The inventory information output.

* deletetxt.sh - A bash script used to delete the two texts files inbetween runs.

* requirements.txt - The file containing project requirements. Used to call the
-r flag on pip install.