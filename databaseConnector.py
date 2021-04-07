import mysql.connector
from mysql.connector import errorcode

CURSOR = 0

with open('credentials.txt') as credentials:
    username = credentials.readline().replace('\n','')
    password = credentials.readline().replace('\n','')
    hostid = credentials.readline().replace('\n','')
    
try:
    database = mysql.connector.connect(
        user = username,
        passwd = password,
        host = hostid)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Database Connection Established")

CURSOR = database.cursor()

def query(query, data = None):
    if data:
        if type(data) is not tuple:
            data = (data,)
        CURSOR.execute(query, data)
    else:
        CURSOR.execute(query)
    
    # Return as list instead of having to deal with CURSOR
    returnVals = []
    for item in CURSOR:
        returnVals.append(item)    
        
    return returnVals

def commit():
    database.commit()


# Set the default database
query("use `online-book-store`")
