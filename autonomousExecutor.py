import threading
import time

class autonomousExecutorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def terminate(self):
        self.running = False

    def run(self):
        while self.running:
            print('kieno')
            time.sleep(2)

