import urllib.request
import os.path
import re
test=(os.path.isfile("log.txt"))
if test is False:
    urllib.request.urlretrieve ("https://s3.amazonaws.com/tcmg476/http_access_log", "log.txt")
    if os.path.isfile("log.txt") is True:
        print("Finished downloading")
    
else:
    '''line = 'local - - [24/Oct/1994:14:01:02 -0600] "GET index.html HTTP/1.0" 200 150'
    print(re.split('.*\[(.*) .*\] \".* (.*) .*\" (\d{3})',line))'''
    
    print (os.path.isfile("log.txt"))
    file=open('log.txt')
    for line in file:
        print(re.split('.*\[(.*) .*\] \".* (.*) .*\" (\d{3})',line))
        #print(line.split()[0])
    file.close()