import sqlite3 as sq
import pandas as pd

sInputFileName = 'C:/MScITPracs/DS/utility.db'
sInputTable = 'Country_Code'
conn=sq.connect(sInputFileName)
sSQL='select * FROM ' +sInputTable+ ';'
InputData=pd.read_sql_query(sSQL,conn)
print("Input Data Values ===========================")
print(InputData)
print("===============================================")

processData = InputData
processData.drop('ISO-2-CODE',axis=1,inplace=True)
processData.drop('ISO-3-Code',axis=1,inplace=True)

processData.rename(columns={'Country':'CountryName'},inplace=True)
processData.rename(columns={'ISO-M49':'countryNumber'},inplace=True)

processData.set_index('countryNumber',inplace=True)

processData.sort_values('CountryName',axis=0,ascending=False,inplace=True)
print("Process Data Values=================================")
print(processData)
print("=======================================================")

OutputData=processData
sOutputFileName='C:/MScITPracs/DS/countriesOPP.csv'
OutputData.to_csv(sOutputFileName,index=False)
print("Database to HORUS-Done")
