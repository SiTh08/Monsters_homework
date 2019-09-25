class Monsters():

    def __init__(self, name, fur, skill1, skill2, skill3, cuteness, colour, eyes =2):
        self.name = name
        self.number_eyes = eyes
        self.fur = fur
        self.skills = [skill1, skill2, skill3]
        self.cuteness = cuteness
        self.colour = colour

    def eat(self):
        return 'NOM NOM NOM '

    def sleep(self):
        return 'zzz zzz zzz'

    def hunt(self):
        return 'I need food.'

    def scare(self):
        return 'RRRAAAWWWWRRRR BOOO!'

    def transform(self):
        return 'sssskkkrrrtt'

    def roar(self):
        return 'RRRRRRRRRRRRROOOOOOOOOOOOOAAAAAAAAAAAAARRRRRRRR!!!'
