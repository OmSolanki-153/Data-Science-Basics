#
import sqlite3 as sq
import pandas as pd
sDatabaseName='C:/MScITPracs/DS/Organizing data/omsol.db'
conn = sq.connect(sDatabaseName)
countrydata = pd.read_excel('C:/MScITPracs/DS/Organizing data/assess_country.xlsx')
countrydata.to_sql('assess_country', conn, if_exists='replace', index = False)
currencydata = pd.read_excel('C:/MScITPracs/DS/Organizing data/foreign_exchange.xlsx')
currencydata.to_sql('foreign_exchange', conn, if_exists= 'replace', index=False)
conn.commit()
mycursor=conn.cursor()
sql = "SELECT * from assess_country JOIN foreign_exchange ON assess_country.country = foreign_exchange.country;"
mycursor.execute(sql)
result = mycursor.fetchall();
for row in result:
    print("Country", row[0])
    print("Currency", row[1])
    print("NOVEMBER", row[2])
    print("December", row[3])
    print("\n")
conn.close()
