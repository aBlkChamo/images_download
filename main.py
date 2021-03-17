import time
import random
from multiprocessing import Process
import os
import sys

PROSSCESS_NUMBER = 10

class Run(Process):
    def __init__(self,num):
        super().__init__()
        self.num=num
    def run(self):
        with open(r"P:\2021lab\bingImages\ngram.txt","r",encoding='utf-8') as f:
            lines = f.readlines()
        word_list = []
        for line in lines:
            word_list.append(line.split(",")[0])
        cmd_1 = r"python P:\2021lab\bingImages\google-images-download-master\google-images-download-master\bing_scraper.py --search "
        cmd_2 =  r' --limit 10 --download --chromedriver "C:\Users\86732\AppData\Local\Programs\Python\Python39\chromedriver.exe"'
        i = 0
        for word in word_list:
            if i % 100 == self.num:
                cmd = cmd_1 + word + cmd_2
                os.popen(cmd)
                print(word)
                time.sleep(100)
            i+=1 
        print('%s runing' %self.num)
        time.sleep(random.randrange(10,15))
        print('%s runing end' %self.num)

if __name__ == '__main__':
    # freeze_support()
    p =[]
    for i in range(PROSSCESS_NUMBER):
        p.append(Run(i))

    for i in  range(PROSSCESS_NUMBER):
        p[i].start()
    print('主线程')
