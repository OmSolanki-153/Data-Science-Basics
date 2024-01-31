import pandas as pd
import numpy as np

sFileDir = 'C:/MScITPracs/MU-DATA-SCIENCE/menu.csv'
RawData = pd.read_csv(sFileDir, header=0)

print("Original Data:")
print(RawData)
print('Rows:', RawData.shape[0])
print('Columns:', RawData.shape[1])

df = RawData
a = df.dropna(axis=1, how='all')  # how='any' is not needed

print("\nData after removing columns with all NaN values:")
print(a)

sFileName = 'C:/MScITPracs/MU-DATA-SCIENCE/deletecolumn.csv'
a.to_csv(sFileName, index=False)
print("Done")
