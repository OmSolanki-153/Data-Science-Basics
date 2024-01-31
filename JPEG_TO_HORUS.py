import imageio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Use imageio.v3.imread to avoid the deprecation warning
sInputFileName='C:/MScITPracs/MU-DATA-SCIENCE/darth-vader.jpg'

InputData = imageio.v3.imread(sInputFileName)

print('X: ', InputData.shape[0])
print('Y: ', InputData.shape[1])
print('RGBA: ', InputData.shape[2])

# Flatten the array without using the deprecated 'flatten' keyword
ProcessRawData = InputData.reshape(-1, InputData.shape[2])

# Determine the number of columns based on the shape
y = InputData.shape[2]
x = ProcessRawData.shape[0] // y

# Create a DataFrame with reshaped data
ProcessData = pd.DataFrame(ProcessRawData, columns=['Red', 'Green', 'Blue', 'Alpha'])
ProcessData['XAxis'] = np.repeat(np.arange(InputData.shape[0]), y)
ProcessData['YAxis'] = np.tile(np.arange(InputData.shape[1]), x)
ProcessData = ProcessData[['XAxis', 'YAxis', 'Red', 'Green', 'Blue', 'Alpha']]

ProcessData.index.names = ['ID']
print('Rows: ', ProcessData.shape[0])
print('Columns: ', ProcessData.shape[1])

plt.imshow(InputData)
plt.show()

OutputData = ProcessData
print('Storing File')
sOutputFileName = 'C:/MScITPracs/MU-DATA-SCIENCE/HORUS-Picture.csv'
OutputData.to_csv(sOutputFileName, index=False)
print('Picture to HORUS - Done')
