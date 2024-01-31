import pandas as pd
myfile='C:/MScITPracs/MU-DATA-SCIENCE/sample3.csv'
all=pd.read_csv(myfile)
print('Rows:', all.shape[0])
print('Columns:', all.shape[1])
print('\n Raw Data Set')
for i in range(0,len(all.columns)):
 print(all.columns[i],type(all.columns[i]))

print('\n Fixed Data Set ')
for i in range(0,len(all.columns)):
 old_col=all.columns[i] + ' '
 colnew=old_col.strip().replace(" ", ".")
 all.columns.values[i] = colnew
 print(all.columns[i],type(all.columns[i]))
print(' Done!!')
mydata_ID=all
mydata_ID.index.names = ['RowID']
print(mydata_ID.head())
myfile2='C:/MScITPracs/MU-DATA-SCIENCE/Retrieve_IP_Routing.csv'
mydata_ID.to_csv(myfile2, index = True, encoding="latin-1")
print('### \n Done!! ')
