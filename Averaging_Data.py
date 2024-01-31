import pandas as pd
inputfile='C:/MScITPracs/MU-DATA-SCIENCE/sample.csv'
print('Loading :',inputfile)
IP_DATA_ALL=pd.read_csv(inputfile,header=0,low_memory=False,usecols=['id','department','Salary'], encoding="latin-1")
AllData=IP_DATA_ALL[['id','department','Salary']]
print(AllData)
MeanData=AllData.groupby(['department'])['Salary'].mean()
print(MeanData)
