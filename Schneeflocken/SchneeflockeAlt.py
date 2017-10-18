import threading
import time
import sys
from random import randint

class Schneeflocke(threading.Thread):
    yPos = 1
    xPos = 0

    def __init__(self, xPos):
        threading.Thread.__init__(self)
        self.xPos=xPos

    def run(self):
        for i in range(100):
            for j in range(self.yPos):
                print("\n", end='')

            move = randint(1, 3)

            if (move == 1):
                self.xPos += 1
            if (move == 2):
                self.xPos -= 1

            for i in range(self.xPos):
                print(" ", end='')

            print(".", end='')
            self.yPos += 0
            time.sleep(0.5)


def start():
    thread1 = Schneeflocke(10)
    thread2 = Schneeflocke(10)
    thread3 = Schneeflocke(10)

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    thread3.start()
    thread3.join()


start()