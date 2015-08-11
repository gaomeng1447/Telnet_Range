'''
Platform: python 2-7-7
Version:1.2
Created on 2015-03-10
Updated on 2015-08-11
@author: gaomwang@cisco.com
'''
import time, datetime
import telnetlib

class Telnet:
    count = 0  #class variable, equal c++ static member
    def __init__(self, host, port=23):
        pot = int(port)#+ 2000
        try:
            self.tn = telnetlib.Telnet(host, pot)
        except:
            print "Exception at Telnet init, occupied port %d?\n"%(port)
        Telnet.count += 1
    
    def __del__(self):
        Telnet.count -= 1
        self.close()
        
    def close(self):
        self.tn.close()
    
    def read(self, delay = 0.05):
        time.sleep(delay)
        return self.tn.read_very_eager()
    
    def write(self, str):
        time.sleep(0.01)
        bk = self.tn.write(str)
        time.sleep(0.01)
        return bk
    
    def read_until(self, match, timeout=1):
        #match = 'msg-string'
        try:
            bk = self.tn.read_until(match, timeout)
        except:
            print 'wait %d seconds, cannot find the given string format!\n'%(timeout)
        finally:
            return "back of read_until: %s"%(bk)
    
    def expect(self, list, timeout=1):
        pass
#         list = ['match-string1', 'match-string2']
#         if cannot get match, return = ['-1', None, text]
#         only back None, I cannot use it.
#         try:
#             bk = self.tn.expect(list, timeout)
#         except Exception as e:
#             print e
#         finally:
#             print bk
    
    def sendCmd(self, cmd, match, timeout=1):
#        return a list of matched string
        self.write(cmd)
        bk = self.read(timeout)
        return self.match(match, bk)
        
    def match(self, match, bk):
        import re
        rt = re.findall(match, bk)
        if len(rt) >= 0.5:
            return rt
        else:
            print "timeout match: %s, %s"%(bk, match)
    
    def interact(self):
        #Occupy the console,always reading. Do not return.
        self.tn.interact()
    
    def howMany(self):
        # calculates the Number of the instance of Telnet.
        return Telnet.count

if __name__ == '__main__':
    host = '10.74.88.41'
    #port = 23
    uut = Telnet(host, 2007)
    time.sleep(1)
    uut.write('\n')
    t1=datetime.datetime.now()
    p1 = uut.read_until('R2#', 1)
    t2=datetime.datetime.now()
    print t1
    print t2
    print p1
    p2 = uut.sendCmd('show mod\n', '.*Feature.*', 5)
    print "this is p2:" 
    for line in p2:
        print line
    time.sleep(0.01)
    print 'Closed successfully!'
