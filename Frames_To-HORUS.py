import imageio.v2 as imageio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

sDataBaseDir = 'C:/MScITPracs/MU-DATA-SCIENCE/temp'
f = 0
ProcessData = pd.DataFrame()

for file in os.listdir(sDataBaseDir):
    if file.endswith(".jpg"):
        f += 1
        sInputFileName = os.path.join(sDataBaseDir, file)
        print('Process : ', sInputFileName)
        InputData = imageio.imread(sInputFileName, pilmode='RGBA')
        print('Input Data Values ===================================')
        print('X: ', InputData.shape[0])
        print('Y: ', InputData.shape[1])
        print('RGBA: ', InputData.shape[2])
        ProcessRawData = InputData.flatten()
        y = InputData.shape[2] + 2
        x = int(ProcessRawData.shape[0] / y)
        ProcessFrameData = pd.DataFrame(np.reshape(ProcessRawData, (x, y)))
        ProcessFrameData['FrameName'] = file
        plt.imshow(InputData)
        plt.show()

        if f == 1:
            ProcessData = ProcessFrameData
        else:
            ProcessData = ProcessData._append(ProcessFrameData)

if f > 0:
    sColumns = ['XAxis', 'YAxis', 'Red', 'Green', 'Blue', 'Alpha', 'FrameName']
    ProcessData.columns = sColumns
    ProcessData.index.names = ['ID']
    print('Rows: ', ProcessData.shape[0])
    print('Columns :', ProcessData.shape[1])
    OutputData = ProcessData
    print('Storing File')
    sOutputFileName = 'C:/MScITPracs/MU-DATA-SCIENCE/HORUS-Movie-Frame.csv'
    OutputData.to_csv(sOutputFileName, index=False)
    print('Processed ; ', f, ' frames')
else:
    print('No frames found in the specified directory.')
