import random
import abc
class niceSensor(abc.ABC):
    def __init__(self, numberOfOutputs, sensorAddress=None):
        self.sensorAddress = sensorAddress
        self.numberOfOutputs = numberOfOutputs
    def getValue(self):
        self.thisList = []
        for x in range(self.numberOfOutputs):
            self.thisList.append(random.randint(1,100))
        return self.thisList
    def isAlive(self):
        return True