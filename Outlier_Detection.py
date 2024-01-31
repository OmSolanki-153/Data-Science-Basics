import pandas as pd
inputfile='C:/MScITPracs/MU-DATA-SCIENCE/sample2.csv'
print('Loading :',inputfile)
IP_DATA_ALL=pd.read_csv(inputfile,header=0,low_memory=False,usecols=['state','latitude'], encoding="latin-1")
AllData=IP_DATA_ALL[['state','latitude']]
print(AllData)
MeanData=AllData.groupby(['state'])['latitude'].mean()
StdData=AllData.groupby(['state'])['latitude'].std()
print('\n Mean data \n', MeanData)
print('\nStd Data\n',StdData)
print('Outliers BOUNDARY')
UpperBound=MeanData+StdData
print('\n UpperBOUND\n', UpperBound)
LowerBound=MeanData-StdData
print('\n LOWER BOUND\n', LowerBound)
