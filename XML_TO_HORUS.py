import pandas as pd
import xml.etree.ElementTree as ET
def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    for row in range(data.shape[0]):
        entry = ET.SubElement(root,'entry')
        for index in range(data.shape[1]):
            schild=str(header[index])
            child = ET.SubElement(entry, schild)
            if str(data[schild][row]) != 'nan':
                child.text = str(data[schild][row])
            else:
                child.text = 'n/a'
                entry.append(child)
    result = ET.tostring(root)
    return result
def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)
sInputFileName='C:/MScITPracs/MU-DATA-SCIENCE/books.xml'
InputData = open(sInputFileName).read()
ProcessDataXML=InputData
ProcessData=xml2df(ProcessDataXML)
ProcessData.drop('genre', axis=1,inplace=True)
ProcessData.rename(columns={'publish_date': 'date'}, inplace=True)
ProcessData.sort_values('price', axis=0, ascending=False, inplace=True)
OutputData=ProcessData
sOutputFileName='C:/MScITPracs/MU-DATA-SCIENCE/XML to horus.csv'
OutputData.to_csv(sOutputFileName, index = False)
print("Data conversion done")
 
