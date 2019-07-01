import os

while True:
    internet = True
    message = os.popen('ping6 -c 2 2001:19f0:6c01:25f6:5400:02ff:fe21:a9c1 | grep received').readlines()
    #message = os.popen('ping -c 2 www.baidu.com | grep received').readlines()
    if message == []:
        internet = False
        print 'there is no internet'
    
    if internet == True:
        message = message[0].split(' ')

        
        if message[4] == 'received,' and (message[3] == '2' or message[3] == '1'):
            internet = True
#            print 'there is internet'
        else:
            internet = False
#            print 'no internet'
    if internet == False:
        os.system('dhclient -6 -T -r; dhclient -6 -T')
