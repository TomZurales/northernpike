import random

class niceBoard:
    def __init__(self, addresses):
        self.addresses = addresses


    def getTemp(self):
        return random.randint(1,100)
    def getGravityVector(self):
        return [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    def getMagneticVector(self):
        return [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    def getAccelerationVector(self):
        return [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    def getAngularVelocity(self):
        return [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    def getAbsoluteOrientation(self):
        return [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    def getValue(self):
        return [random.randint(1,100), random.randint(1,100), random.randint(1,100),
                random.randint(1,100), random.randint(1,100), random.randint(1,100),
                random.randint(1,100), random.randint(1,100), random.randint(1,100),
                random.randint(1,100), random.randint(1,100), random.randint(1,100),
                random.randint(1,100), random.randint(1,100), random.randint(1,100), # All 16
                random.randint(1,100)]
