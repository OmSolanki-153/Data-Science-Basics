import pandas as pd
import numpy as np
sFileDir='C:/Users/lenovo/Dropbox/farzana/DS Msc/practical/accident.csv'
RawData=pd.read_csv(sFileDir,header=0)
print(RawData)
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
df=RawData
a=df.fillna(df.min())
print(a)
b=df.fillna(df.max())
print(b)
sFileName='C:/Users/lenovo/Dropbox/farzana/DS Msc/prac all/prac 5/min max.csv'
df.to_csv(sFileName, index = False)
print("Done")
