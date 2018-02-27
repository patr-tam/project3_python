import urllib.request
import os.path
test=(os.path.isfile("log.txt"))
if test is False:
    urllib.request.urlretrieve ("https://s3.amazonaws.com/tcmg476/http_access_log", "log.txt")
    if os.path.isfile("log.txt") is True:
        print("Finished downloading")
    
else:
    print (os.path.isfile("log.txt"))
