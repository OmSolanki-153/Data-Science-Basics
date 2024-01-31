import pandas as pd
import numpy as np
sFileDir='C:/MScITPracs/MU-DATA-SCIENCE/student.csv'
RawData=pd.read_csv(sFileDir,header=0)
print('Rows :',RawData.shape[0])
print('Columns :',RawData.shape[1])
df=RawData
for column in df.columns:
 df[column].fillna(df[column].mode()[0], inplace=True)
print(df)
sFileName='C:/MScITPracs/MU-DATA-SCIENCE/2ch-sound.wavmode.csv'
df.to_csv(sFileName, index = False)
print("Done")
