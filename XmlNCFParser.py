

class XmlNCFParser(object):
    
    @classmethod
    def parse(cls, filePath):
        import xml.etree.ElementTree as ET
        allList = []
        lineList = []
        try:
            f = open(filePath)
            tree = ET.parse(f)
        finally:
            f.close()
        root = tree.getroot()
        for child in root:
            for row in child:
                lineList = []
                for item in row:
                    lineList.append(item.text)
                allList.append(lineList)
                
        condList = []
        tcListList = []
        tcList = []
        glbParList = []
        limitList = []
        for elem in allList:
            if "TEST_CONDITION" in elem:
                condList.append(elem)
            elif "TEST_CASE_LIST" in elem:
                tcListList.append(elem)
            elif "TEST_CASE" in elem:
                tcList.append(elem)
            elif "SYS_PARAM" in elem:
                glbParList.append(elem)
            elif "T_LIMIT" in elem:
                limitList.append(elem)
        tsTcInfoList = [condList, tcListList, tcList, glbParList, limitList]
        return tsTcInfoList
    
if __name__ == '__main__':
    host = XmlNCFParser()
    filePath = 'C:\Cisco_File\Python_Library\L1_EDVT_Cisco\Sum_Xml\country_data.xml'
    a = host.parse(filePath)
    print a