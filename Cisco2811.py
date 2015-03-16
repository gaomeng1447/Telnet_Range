'''
Created on 2015-3-11

@author: gaomwang
'''

import time, datetime
import telnetlib

class Cisco2811:
    def __init__(self, host, port, password = 'admin'):
        '''
        Constructor
        '''
        self.host_2_login = host
        self.port_2_clear = port
        self.psw = password
        try:
            self.tnt1 = telnetlib.Telnet(host, port = 23)
        except:
            print 'exception happens at Cisco2811 __init__\n'
    
    def login(self):
        match = '*Password:'
        expt =['ts1#']
        try:
            self.tnt1.read_until(match, 2)
            self.tnt1.write(self.psw + '\n')
        except Exception as e:
            print 'try to login, exception happens:', e
        time.sleep(0.2)
        self.tnt1.write('en' + '\n')
        self.tnt1.expect(expt, 2)
        self.tnt1.write(self.psw + '\n')
        time.sleep(0.2)
    
    def show_line(self):
        self.tnt1.write('show line' + '\n')
        time.sleep(2)
        abc = self.tnt1.read_very_eager()
        print "show line: \n", abc
        time.sleep(0.2)
        self.tnt1.write('\n')
    
    def clear_line(self):
        for port in self.port_2_clear:
            self.tnt1.write('clear line ' + str(port) + '\n')
            expt =['[confirm]']
            self.tnt1.expect(expt, 2)
            self.tnt1.write('\n')#confirm
            time.sleep(0.2)
    
    def configure_dtr_act(self):
        for port in self.port_2_clear:
            self.tnt1.write('conf t' + '\n')
            time.sleep(0.2)
            self.tnt1.write('line ' + str(port)+ '\n')
            time.sleep(0.2)
            self.tnt1.write('modem dtr-active' + '\n')
            time.sleep(0.2)
            self.tnt1.write('logging synchronous' + '\n')
            time.sleep(0.2)
            self.tnt1.write('end' + '\n')
            time.sleep(0.2)
        self.tnt1.write('wi' + '\n')
        time.sleep(0.2)
    
    def __del__(self):
        """Destructor -- close the connection."""
        self.tnt1.close()
        
if __name__ == '__main__':
    host = '10.74.88.29'
    #port = 23
    bb = Cisco2811(host, ['18', '19', '20'])
    bb.login()
    print '1111111111'
    bb.show_line()
    bb.clear_line()
    bb.configure_dtr_act()
    print '2222222222'
    bb.show_line()
    time.sleep(1)
    del bb
    print 'finished!'
