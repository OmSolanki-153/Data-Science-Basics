import sys
import os
Base='C:/Users/Om Solanki'
print('Working Base :',Base, ' using ', sys.platform)
sCompanies=['Oracle','Dropbox','Saved Games','Microsoft']
Steps=['Practical 1', 'Practical 2', 'Practical 3']
SubSteps=['R','Python']
for i in range(len(sCompanies)):
    for j in range(len(Steps)):
        for k in range(len(SubSteps)):
            sFileDir=Base + '/' + sCompanies[i] + '/' + Steps[j] + '/' + SubSteps[k]
            print('Check:',sFileDir)
            if not os.path.exists(sFileDir):
                os.makedirs(sFileDir)
            
for i in range(len(sCompanies)):
    for j in range(len(Steps)):
        sDataBaseDir=Base + '/' + sCompanies[i] + '/' + \
        Steps[j] + '/SQLite' 
        DatabaseName=sDataBaseDir + '/'  + sCompanies[i][3:] + '.db' 
        print('Check:',DatabaseName)
        sDataBaseDir='C:/MScITPracs/DS' 
        DatabaseName=sDataBaseDir + '/mydatabase.db' 
        print('Check:',DatabaseName)
        DatabaseName=sDataBaseDir + '/omsol.db' 
        print('Check:',DatabaseName)
