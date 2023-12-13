import pandas as pd
print("Om Solanki 04")
sInputFileName='C:/Users/pc24/Desktop/Data Science MSc IT/Country_Code.csv'
InputData=pd.read_csv(sInputFileName,encoding="latin-1")
print("Input Data Values ========================================")
print(InputData)
print("==========================================================")


ProcessData=InputData
ProcessData.drop("ISO-2-CODE",axis=1,inplace=True)
ProcessData.drop("ISO-3-CODE",axis=1,inplace=True)

ProcessData.rename(columns={'Country':'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'}, inplace=True)

ProcessData.set_index('CountryNumber',inplace=True)
ProcessData.sort_values('CountryName',axis=0, ascending=False, inplace=True)

print(ProcessData)
print("================================================================")

OutputData=ProcessData
OutputFileName='C:/Users/pc24/Desktop/Data Science MSc IT/OutputData.csv'
OutputData.to_csv(OutputFileName,index=False)
print("CSV to HORUS - Done")
