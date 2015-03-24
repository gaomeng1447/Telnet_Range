'''
Created on 2015-3-12

@author: gaomwang
'''
import xml.etree.ElementTree as ET

class Xml:
    '''
    This class closely related with the file:abc.xml
    the method of find_all, get just demonstrate the use of ...
    '''
    def __init__(self, path):
        try:
            self.tree = ET.parse(path)
        except:
            print '__init__ fail, path error?\n'
    
    def root(self):
        self.root = self.tree.getroot()
        print self.root.tag, self.root.attrib
    
    def Level_1(self):
        for level in self.root:
            print level.tag, level.attrib
            print level.text
    
    def iter_element(self, elem):
        for content in self.root.iter(elem):
            print content.tag, content.text
            #print 'content.tag', content.tag
            #print 'content.attrib', content.attrib
            #print 'content.text', content.text
    
    def find_all(self, elem):
        str1 = 'CONTENT'
        bk = []
        for content in self.root.findall(elem):
            subcont1 = content.find(str1).text
            bk.append(subcont1)
            print subcont1
        return bk
    
    def get(self, elem):
        str2 = 'logFile'
        for content in self.root.findall(elem):
            subcont2 = content.get(str2)
            print subcont2
    
    def XPath(self, elem):
        for cont in self.root.findall(elem):
            print cont
            
    def update(self, file):
        for temp in self.root.iter('TEMP'):
            new_temp = float(temp.text) + 100
            temp.text = str(new_temp)
            temp.set('gaomeng updated', 'yes')
        return self.tree.write(file)
    
    def write(self, file):
        rt = ET.Element("library")
        head = ET.SubElement(rt, "Classical")
        title = ET.SubElement(rt, 'book')
        title.text = 'Classical Electronics'
        body = ET.SubElement(title, "body")#body is the child element of title
        body.set("comments", "good")#set attributes
        body.text = "hello, world!" #text string
        rt.append(ET.Element("one"))
        tree = ET.ElementTree(rt)
        tree.write(file)
    
    def dump(self):
        #only used for debugging
        a = ET.Element('World')
        b = ET.SubElement(a, 'China')
        c = ET.SubElement(a, 'America')
        ET.dump(a)
        pass
    
    def iselement(self, element):
        return ET.iselement(element)
        
    
    def open(self):
        pass
if __name__ == '__main__':
    tree = Xml('abc.xml')
    tree.root()
    tree.iter_element('STARTTIME')
    print "find_all"
    element = tree.find_all('CONFIG_FILE')#only find level 1?
    print 'element is:', element
    print "get"
    tree.get('LOG_FILE')
    print tree.iselement("STARTTIME")
 
    print "XPath"
    print tree.XPath("[STARTTIME]")
    print tree.update('output.xml')
    tree.dump()
    tree.write("page.xml")
    
    