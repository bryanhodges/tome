import pyodbc

connString = "Driver={ODBC Driver 13 for SQL Server};Server=tcp:tome.database.windows.net,1433;Database=tome;Uid=lj553650;Pwd=Duff153z;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

conn = pyodbc.connect(connString)
cursor = conn.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()