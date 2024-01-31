import pandas as pd
import sys
sFileName='C:/MScITPracs/MU-DATA-SCIENCE/sample2.csv'
print('Working base:',sFileName)
print('working using', sys.platform)
alldata=pd.read_csv(sFileName,usecols=['state','city','latitude'])
sFileDir='C:/MScITPracs/MU-DATA-SCIENCE/practicals'
mydata = alldata.drop_duplicates(subset=None, keep='first', inplace=False)
print('Rows :',mydata.shape[0])
print('Columns :',mydata.shape[1])
sFileName=sFileDir + '/output data.csv'
mydata.to_csv(sFileName, index = False)
print('Data saved successfully in csv format')
#shape() is used to get current shape of an array
