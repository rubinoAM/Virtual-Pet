personalities = ["Analytical","Sentimental","Idealist","Meditative","Cynical"]

class Pet(object):
    def __init__(self, name, personality, weight):
        self.name = name
        self.age = 0
        self.weight = weight
        self.personality = personality