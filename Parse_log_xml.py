'''
created date: 2015/03/23
author: gaomwang@cisco.com
'''
import xml.etree.ElementTree as ET
#arrowList = ['']*5
myList = []
class Parse_log_xml:
    def __init__(self, path):
        try:
            self.tree = ET.parse(path)
        except:
            print 'path error!\n'
    
    def root(self):
        self.root = self.tree.getroot()
        print self.root.tag, self.root.attrib
    
    def Level_1(self):
        for level in self.root:
            print level.tag, level.attrib
            print level.text
    
    def Level_2(self):
        for level in self.root:
            for corner in level:
                print 'corner info:', corner.tag, corner.attrib
                print 'corner text:', corner.text
    
    def Level_3(self):
        for level in self.root:
            for corner in level:
                for loop in corner:
                    print 'loop info:', loop.tag, loop.attrib
                    print 'loop text:', loop.text
    
    def Level_4(self):
        myList = []
        for level in self.root:
            for corner in level:
                for loop in corner:
                    arrowList = []
                    arrowList.append(corner.attrib['id'])
                    for ID in loop:
                        arrowList.append(ID.text)
                        #print 'ID info:', ID.tag, ID.attrib
                        #print 'ID text:', ID.text
                    #print 'arrowList is: \n', arrowList
                    myList.append(arrowList)
        return myList
    
if __name__ == '__main__':
    gm = Parse_log_xml('abc.xml')
    gm.root()
    #gm.Level_2()
    lt = gm.Level_4()
    print 'my list is:\n'
    for sublt in lt:
        print sublt