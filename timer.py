import time
class Timer:
    def __init__(self):
        self.begin = 0
        self.end = 0
    def start(self):
        self.begin = time.time()
    def stop(self):
        self.end = time.time()
        return self.end-self.begin