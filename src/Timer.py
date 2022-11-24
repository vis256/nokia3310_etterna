import time

TICK_LENGTH_MILISECONDS = 20

class Timer:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += TICK_LENGTH_MILISECONDS
        time.sleep(TICK_LENGTH_MILISECONDS / 1000)

    def getTime(self):
        return self.time
        
GLOBAL_TIMER = Timer()
print("Created a global Timer object")
