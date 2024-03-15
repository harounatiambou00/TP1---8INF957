from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class ElectricEngine(Engine):
    def start(self):
        #Logique de demarrage du moteur.
        pass

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()


