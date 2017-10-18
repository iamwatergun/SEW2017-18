import threading
import Schneeflocke
import time
import os
from random import randint

class Main(threading.Thread):
    counter = 0
    list = []
    closedThreads = 0

    def __init__(self, list):
        threading.Thread.__init__(self)
        self.list = list

    def run(self):
        #alle Threads starten
        for i in (self.list):
            i.start()

        #Commandline clearen
        os.system("cls")


        while self.closedThreads < len(self.list):

            #erstellt Abstände zwischen Schneeflocken
            for j in range(i.xPos):
                print(" ", end='')
            print(".", end='')

            #wenn ein Thread fertig ist wird er removed
            for k in self.list:
                if k.end:
                    self.list.remove(k)
                    self.closedThreads += 1
            time.sleep(0.1)
            os.system("cls")


threadList = []

print("Bitte 'Main.py' über cmd starten wegen formatierung mit os")

schneeflocke1 = Schneeflocke.Schneeflocke(10)
schneeflocke2 = Schneeflocke.Schneeflocke(10)
schneeflocke3 = Schneeflocke.Schneeflocke(10)
schneeflocke4 = Schneeflocke.Schneeflocke(10)
schneeflocke5 = Schneeflocke.Schneeflocke(10)

threadList.append(schneeflocke1)
threadList.append(schneeflocke2)
threadList.append(schneeflocke3)
threadList.append(schneeflocke4)
threadList.append(schneeflocke5)

mainThread = Main(threadList)
mainThread.start()
mainThread.join()