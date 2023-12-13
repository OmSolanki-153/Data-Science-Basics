import imageio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

sDataBaseDir = 'C:/MScITPracs/DS/tempo'
f = 0
processData = pd.DataFrame()  # Initialize an empty DataFrame

for file in os.listdir(sDataBaseDir):
    if file.endswith(".jpg"):
        f += 1
sInputFileName = os.path.join(sDataBaseDir, file)
print("Process: ", sInputFileName)
InputData = imageio.imread(sInputFileName, mode='RGBA')
print('Input Data Values==================================')
print("X: ", InputData.shape[0])
print("Y: ", InputData.shape[1])
print('RGBA: ', InputData.shape[2])
print('===================================================')
processRawData = InputData.flatten()
y = InputData.shape[2] + 2
x = int(processRawData.shape[0] / y)
processFrameData = pd.DataFrame(np.reshape(processRawData, (x, y)))
processFrameData['Frame'] = file
print('==================================================')
print("Process Data values ===========================================")
print("===================================================")
plt.show()

if f == 1:
    processData = processFrameData
else:
    processData = processData._append(processFrameData)

if f > 0:
    sColumns = ['XAxis', 'YAxis', 'Red', 'Green', 'Blue', 'Alpha', 'FrameName']
processData.columns = sColumns
print("===================================================")
processFrameData.index.names = ['ID']
print("Rows: ", processData.shape[0])
print("Columns: ", processData.shape[1])
print("===================================================")
OutputData = processData
print("Storing File")
sOutputFileName = 'C:/Python34/temp/Movie-Frame.csv'
OutputData.to_csv(sOutputFileName, index=False)
print("===================================================")
print("Processed: ", f, ' Frames')
print("====================================================")
print("SCORPION WINS FATALITY!!!!!")
print("======================================================")
