import pandas as pd
import numpy as np
sFileDir='C:/MScITPracs/MU-DATA-SCIENCE/menu.csv'
RawData=pd.read_csv(sFileDir,header=0)
print(RawData)
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
df=RawData
a=df.dropna(thresh=2)
print(a)
sFileName='C:/MScITPracs/MU-DATA-SCIENCE/deleterows.csv'
df.to_csv(sFileName, index = False)
print("Done")
