import pandas as pd
sInputFileName='C:/MScITPracs/MU-DATA-SCIENCE/Male.csv'
InputData=pd.read_csv(sInputFileName,encoding="latin-1")
print('\n Input Data Values ===================================')
print(InputData)
ProcessData=InputData
ProcessData.drop('LastName', axis=1,inplace=True)
ProcessData.rename(columns={'FirstName': 'F_Name'}, inplace=True)
ProcessData.sort_values('Salary', axis=0, ascending=True, inplace=True)
print('\n Process Data Values =================================')
print(ProcessData)
OutputData=ProcessData
sOutputFileName='C:/MScITPracs/MU-DATA-SCIENCE/CSV_To_HORUS.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('\n CSV to HORUS - Done')
