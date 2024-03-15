class Workable:
    def work(self):
        pass

class Feedable:
    def eat(self):
        pass

class Human(Workable, Feedable):
    def work(self):
        # Logique du travail de l'humain
        pass

    def eat(self):
        # Logique pour prendre une pause déjeuner
        pass

class Robot(Workable):
    def work(self):
        # Logique du travail du robot
        pass


