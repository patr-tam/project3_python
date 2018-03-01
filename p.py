import urllib.request
import os.path
import re
from datetime import datetime
test=(os.path.isfile("log.txt"))

regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

if test is False:
    urllib.request.urlretrieve ("https://s3.amazonaws.com/tcmg476/http_access_log", "log.txt")
    if os.path.isfile("log.txt") is True:
        print("Finished downloading")
    
else:
    file2 = open('logerrors.txt','w')
    o94= open('oct94.txt','w')
    n94= open('nov94.txt', 'w')
    d94= open('dec95.txt', 'w')
    ja95= open('jan95.txt', 'w')
    f95= open('feb95.txt', 'w')
    m95= open('mar95.txt', 'w')
    a95= open('apr95.txt', 'w')
    ma95= open('may95.txt', 'w')
    ju95= open('jun95.txt', 'w')
    jl95= open('jul95.txt', 'w')
    au95= open('aug95.txt', 'w')
    s95= open('sep95.txt', 'w')
    o95= open('oct95.txt', 'w')    
    #print (os.path.isfile("log.txt"))
    file=open('log.txt')
    ercount,total,good,oct94,nov94,dec94,jan95,feb95,mar95,apr95,may95,jun95,jul95,aug95,sep95,oct95,notsuc,redir=(0,)*18
    for line in file:
        total+=1
        #a=re.split('.*\[(.*) .*\] \".* (.*) .*\" (\d{3})',line)
        
        errors = [] # a list to store errors from the parsing process

        parts = regex.split(line)
        
        # Let's see what the regex grabbed...
        #print (parts)
        month1,month2,month3,month4,month5,month6,month7,month8,month9,month10,month11,month12,month13 =([],)*13
        if len(parts)>=7:
            b=parts[1]
            c=parts[6]
            month=b[3:6]
            year=b[7:11]
            date=b[0:11]
            good+=1 #find count
            if c[0] == '4':
                notsuc+=1
            if c[0] == '3':
                redir+=1
            if month == 'Oct' and year == '1994':  
                oct94+=1
                month1.append(line)
                for item in month1:
                    o94.write(item)                
            if month == 'Nov' and year == '1994':
                nov94+=1
                month2.append(line)
                for item in month2:
                    n94.write(item)  
                    
            if month == 'Dec' and year == '1994':
                dec94+=1  
                month3.append(line)
                for item in month3:
                    d94.write(item)                  
            if month == 'Jan' and year == '1995':
                jan95+=1
                month4.append(line)
                for item in month4:
                    ja95.write(item)                  
            if month == 'Feb' and year == '1995':
                feb95+=1   
                month5.append(line)
                for item in month5:
                    f95.write(item)                  
            if month == 'Mar' and year == '1995':
                mar95+=1  
                month6.append(line)
                for item in month6:
                    m95.write(item)                  
            if month == 'Apr' and year == '1995':
                apr95+=1 
                month7.append(line)
                for item in month7:
                    a95.write(item)                  
            if month == 'May' and year == '1995':
                may95+=1 
                month8.append(line)
                for item in month8:
                    ma95.write(item)                  
            if month == 'Jun' and year == '1995':
                jun95+=1  
                month9.append(line)
                for item in month9:
                    ju95.write(item)                  
            if month == 'Jul' and year == '1995':
                jul95+=1  
                month10.append(line)
                for item in month10:
                    jl95.write(item)                  
            if month == 'Aug' and year == '1995':
                aug95+=1 
                month11.append(line)
                for item in month11:
                    au95.write(item)                  
            if month == 'Sep' and year == '1995':
                sep95+=1 
                month12.append(line)
                for item in month12:
                    s95.write(item)                  
            if month == 'Oct' and year == '1995':
                oct95+=1 
                month13.append(line)
                for item in month13:
                    o95.write(item)                  
            date2=datetime.strptime(date,"%d/%b/%Y")  
            #print(date2)
        # Sanity check the line -- there should be 7 elements in the list (remember that index 0 has the whole string)
        if not parts or len(parts) < 7:
            #print("Error parsing line! Log entry added to ERRORS[] list...")
            #errors=[]
            errors.append(line)
            for item in errors:
                file2.write(item)
                ercount+=1
        
        # Now we can do something with the parts we grabbed...        
        #if ray is not certain length ignore 
        #else:            
        ''' if len(a) < 5:
            #print(len(a))
            count+=1
            for item in a:
                file2.write(item) '''
                
    print('error count is', ercount)    
    print('total logs for October 1994:',oct94)
    print('total logs for November 1994:',nov94)
    print('total logs for December 1994:',dec94)
    print('total logs for January 1995:',jan95)
    print('total logs for February 1995:',feb95)
    print('total logs for March 1995:',mar95)
    print('total logs for April 1995:',apr95)
    print('total logs for May 1995:',may95)
    print('total logs for June 1995:',jun95)
    print('total logs for July 1995:',jul95)
    print('total logs for August 1995:',aug95)
    print('total logs for September 1995:',sep95)
    print('total logs for October 1995:',oct95)
    
    sumofm= oct94+nov94+dec94+jan95+feb95+mar95+apr95+may95+jun95+jul95+aug95+sep95+oct95
    print('total is', total)
    print('good logs:', good)
    print('bad logs:', ercount)
    bad=ercount/total
    print('percent of bad:', round((bad*100),2),'%')
    print('percent logs not successful (error 4xx):', round(((notsuc/good)*100),2),'%')
    print('percent requests redirected elsewhere (3xx):',round(((redir/good)*100),2),'%')
    #print('sum is', sumofm)
        #print(line.split()[0])
    file.close()
    file2.close()
    o94.close()
    n94.close()
    d94.close()
    ja95.close()
    f95.close()
    m95.close()
    a95.close()
    ma95.close()
    ju95.close()
    jl95.close()
    au95.close()
    s95.close()
    o95.close()
    
    '''o94
    n94
    d94
    ja95
    f95
    m95
    a95
    ma95
    ju95
    jl95
    au95
    s95
    o95'''
