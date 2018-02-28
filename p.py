import urllib.request
import os.path
import re
test=(os.path.isfile("log.txt"))
if test is False:
    urllib.request.urlretrieve ("https://s3.amazonaws.com/tcmg476/http_access_log", "log.txt")
    if os.path.isfile("log.txt") is True:
        print("Finished downloading")
    
else:
    file2 = open('testfile.txt','w')       
    print (os.path.isfile("log.txt"))
    file=open('log.txt')
    count=0
    for line in file:
        a=re.split('.*\[(.*) .*\] \".* (.*) .*\" (\d{3})',line)
        #if ray is not certain length ignore 
        #else:
        if len(a) < 5:
            #print(len(a))
            count+=1
            for item in a:
                file2.write(item) 

    print('count is', count)      
        #print(line.split()[0])
    file.close()
    file2.close()