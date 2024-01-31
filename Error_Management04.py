import pandas as pd
import numpy as np
sFileDir='C:/MScITPracs/MU-DATA-SCIENCE/accident.csv'
RawData=pd.read_csv(sFileDir,header=0)
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
df=RawData
a=df.fillna(df.mean())
print(a)
b=df.fillna(df.median())
print(b)
sFileName='C:/MScITPracs/MU-DATA-SCIENCE/mean&median.csv'
df.to_csv(sFileName, index = False)
print("Done")
