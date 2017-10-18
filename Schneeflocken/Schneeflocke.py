import threading
import time
import sys
from random import randint

class Schneeflocke(threading.Thread):
    yPos = 0
    xPos = 0
    ground = 20

    def __init__(self, xPos):
        threading.Thread.__init__(self)
        self.xPos=xPos
        self.yPos=0
        self.end = False
        self.lock = threading.Lock()

    def run(self):
        while not self.end:

            #entscheidet zufällige Bewegung der Schneeflocke
            self.move()

            self.yPos += 1
            #print(self.xPos, self.yPos)

            time.sleep(0.5)

            #Wenn Schneeflocke den Boden berührt
            if self.yPos == self.ground:
                self.end = True

        #lock releasen
        self.lock.acquire()
        self.lock.release()


    def move(self):

        move = randint(1, 3)

        if (move == 1):
            self.xPos += 1
        if (move == 2):
            self.xPos -= 1
