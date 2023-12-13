import imageio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sInputFileName = 'C:/Python34/darth-vader.jpg'
InputData = imageio.imread(sInputFileName)

print("Input Data Values =============================")
print('X:', InputData.shape[0])
print('Y:', InputData.shape[1])
print('RGBA:', InputData.shape[2])

print("==============================================")

ProcessRawData = InputData.flatten()
y = InputData.shape[2] + 2
x = int(ProcessRawData.shape[0] / y)
ProcessData = pd.DataFrame(np.reshape(ProcessRawData, (x, y)))
sColumns = ['XAxis', 'YAxis', 'Red', 'Green', 'Blue']
ProcessData.columns = sColumns
ProcessData.index.names = ['ID']
print('Rows:', ProcessData.shape[0])
print('Columns:', ProcessData.shape[1])
print("==============================================")
print("Process Data Values =========================")
print("==============================================")
plt.imshow(InputData)
plt.show()
print("==============================================")

OutputData = ProcessData
print("Storing File.....")
sOutputFileName = 'C:/Python34/Anakin.csv'
OutputData.to_csv(sOutputFileName, index=False)
print("==============================================")
print("Picture to HORUS - Done")
print("==============================================")
