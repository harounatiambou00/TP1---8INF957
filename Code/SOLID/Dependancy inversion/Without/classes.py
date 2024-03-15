class Engine:
    def start(self):
        pass

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()


