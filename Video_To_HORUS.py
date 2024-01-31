import os 
import shutil 
import cv2
sInputFileName='C:/MScITPracs/MU-DATA-SCIENCE/dog.mp4'
sDataBaseDir='C:/MScITPracs/MU-DATA-SCIENCE/temp'
if os.path.exists(sDataBaseDir):
    shutil.rmtree(sDataBaseDir)
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)

vidcap = cv2.VideoCapture(sInputFileName)
success,image = vidcap.read()
count = 0
while success:
    success,image = vidcap.read()
    sFrame=sDataBaseDir + str('/dog-frame-' + str(format(count, '04d')) + '.jpg')
    print('Extracted: ', sFrame)
    cv2.imwrite(sFrame, image)
    if os.path.getsize(sFrame) == 0:
        count += -1
        os.remove(sFrame)
        print('Removed: ', sFrame)
    if cv2.waitKey(10) == 27: # exit if Escape is hit
        break
    if count > 100: # exit
        break
    count += 1


print('Generated : ', count, ' Frames')
print('Movie to Frames HORUS - Done')
