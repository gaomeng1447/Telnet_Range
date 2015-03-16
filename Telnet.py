'''
Created on 2015-03-10

@author: gaomwang
'''
import sys
import time, datetime
import string
import telnetlib
import abc

class Telnet:
    count = 0  #static member
    '''
    This is a class for Telnet operation. As limited to personal knowledge, it only operate Cisco C2960 Server
    '''

    def __init__(self, host, port):
        '''
        Constructor
        '''
        pot = int(port) + 2000
        self.tn = telnetlib.Telnet(host, pot)
        Telnet.count += 1
    
#     @staticmethod
#     def open():
#         pass
#         
    def close(self):
        #in-class method
        self.tn.close()
    
    def read(self, delay = 0.5):
        time.sleep(delay)
        return self.tn.read_very_eager()
    
    def read_long(self):
        time.sleep(5)
        return self.tn.read_very_eager()
    
    def write(self, str):
        time.sleep(0.1)
        return self.tn.write(str + '\n')
        time.sleep(0.1)
        pass
    
    def read_until(self):
        pass
    
    def expect(self):
        pass
    
    def __del__(self):
        """Destructor -- close the connection."""
#         Telnet.count -= 1
        self.close()
        
#     def howMany(self):
#         # calculates the Number of the instance of Telnet.
#         self.open()
#         return Telnet.count

if __name__ == '__main__':
    host = '10.74.88.41'
    #port = 23
    bb = Telnet(host, 12)
    time.sleep(1)
    #abc = bb.write('b bootdisk:xformer_0303')
    time.sleep(3)
    for id in range(0,30):
        #print "the following is part of:", id
        pp = bb.read_long()
        print pp
    
    del bb
    print 'Closed successfully!'
