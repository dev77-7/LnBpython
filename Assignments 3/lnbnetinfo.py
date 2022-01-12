import socket
import uuid
import dns.resolver
def get_info():
    try:
        device_name = socket.gethostname()
        device_ip = socket.gethostbyname(device_name)
        print("Devicename :",device_name)
        print("IP :",device_ip)
        print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
        for elements in range(0,2*6,2)][::-1]))
        result = dns.resolver.resolve('learnandbuild.in', 'A')
        for ipval in result:
            print('Learn And Build DNS Server IP', ipval.to_text())
    except:
        print("Unable to get Devicename and IP")
 

get_info()






    
