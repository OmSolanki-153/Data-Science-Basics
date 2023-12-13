import pandas as pd
import xml.etree.ElementTree as ET
print("Om Solanki 04")
def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    for row in range(data.shape[0]):
        entry = ET.SubElement(root, 'entry')
        for index in range(data.shape[1]):
            schild = str(header[index])
            if schild in data.columns:  # Check if the column exists in the DataFrame
                child = ET.SubElement(entry, schild)
                if not pd.isna(data[schild][row]):
                    child.text = str(data[schild][row])
                else:
                    child.text = 'n/a'
                entry.append(child)
    result = ET.tostring(root)
    return result

def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records=[]
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text

        all_records.append(record)
    return pd.DataFrame(all_records)

sInputName='C:/MScITPracs/DS/Country_Code.xml'

InputData = open(sInputName).read()
print("=================================================")
print('Input Data Values===============================================')
print("=================================================")
print(InputData)
print("=================================================")
ProcessDataXML=InputData
ProcessData=xml2df(ProcessDataXML)

ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-CODE',axis=1,inplace=True)

ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)

ProcessData.set_index('CountryNumber',inplace=True)

ProcessData.sortValues('CountryName',axis=0,ascending=False,inplace=True)
print("=================================================")
print("Process Data Values =============================")
print("=================================================")
print(ProcessData)
print("=================================================")

OutputData=ProcessData
OutputFileName='C:/MScITPracs/DS/OutputDataB.xml'
OutputData.to_csv(OutputFileName,index=False)
print("CSV to HORUS - Done")

