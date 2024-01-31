import pandas as pd
sInputFileName='C:/MScITPracs/MU-DATA-SCIENCE/Country_Code.json'
InputData=pd.read_json(sInputFileName,orient='index', encoding="latin-1")
print(InputData)
ProcessData=InputData
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
ProcessData.set_index('CountryNumber', inplace=True)
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
OutputData=ProcessData
sOutputFileName='C:/MScITPracs/MU-DATA-SCIENCE/HORUS-JSON-Country.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('JSON to HORUS - Done')

