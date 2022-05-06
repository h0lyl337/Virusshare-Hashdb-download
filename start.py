
import requests
import os
import subprocess
import hashdatabase
import threading
import multiprocessing
import time
import hashdb

max = 415
thread = 5

def startit(i):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get("https://virusshare.com/hashfiles/VirusShare_{0}.md5".format(format(i, '05d')), headers=headers)
    file = open('virusshare_{0}.txt'.format(i), 'wb')
    file.write(r.content)

    f = open('virusshare_{0}.txt'.format(i), 'r')
    for LINE in f.readlines():
        if len(LINE) <= 15:
            pass

        elif '#' in LINE:
            pass

        else:
            hashdatabase.insert_new_hash(LINE.strip())

        #hashdatabase.insert_new_hash(LINE)

i = 0
while i <= max:
    if threading.active_count() <= 10:
        t = threading.Thread(target=startit, args=(i,))
        t.start()
        i+=1
    
    
