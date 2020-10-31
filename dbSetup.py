import sqlite3
import pandas as pd

df = pd.read_csv("oct20General.csv")

df.columns = df.columns.str.strip()

con = sqlite3.connect("oct20General.db")

df.to_sql("MyTable", con)

con.close()



# con = sqlite3.connect("oct20General.db") # change to 'sqlite:///your_filename.db'
# cur = con.cursor()
# cur.execute("CREATE TABLE newT2 (Date, col2, col3, col4, col5, col6, col7, col8, col9, Date0, Date1, Date2);")
#  # use your column names here
#
# with open('oct20General.csv','r') as fin: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
#     dr = csv.DictReader(fin) # comma is default delimiter
#     to_db = [(i['Date'], i['col2'], i['col3'], i['col4'], i['col5'], i['col6'], i['col7'], i['col8'], i['col9'], i['Date0'], i['Date1'], i['Date2']) for i in dr]
#
# cur.executemany("INSERT INTO newT2 (Date, col2, col3, col4, col5, col6, col7, col8, col9, Date0, Date1, Date2) VALUES (?, ?);", to_db)
# con.commit()
# con.close()
#
#
# conn = sqlite3.connect('general.db')
# c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
#
# # Create table - CLIENTS
# c.execute('''CREATE TABLE CLIENTS
#              ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Country_ID] integer, [Date] date)''')
#
# # Create table - COUNTRY
# c.execute('''CREATE TABLE COUNTRY
#              ([generated_id] INTEGER PRIMARY KEY,[Country_ID] integer, [Country_Name] text)''')
#
# # Create table - DAILY_STATUS
# c.execute('''CREATE TABLE DAILY_STATUS
#              ([Client_Name] text, [Country_Name] text, [Date] date)''')
#
# conn.commit()
#
# # Note that the syntax to create new tables should only be used once in the code (unless you dropped the table/s at the end of the code).
# # The [generated_id] column is used to set an auto-increment ID for each record
# # When creating a new table, you can add both the field names as well as the field formats (e.g., Text)
