import random


class Controller:

    def __init__(self):
        self.inp = 0

    def runMenu(self):
        print("INPUT PASSWORD LENGTH:")
        self.inp = input()


class Password:

    def __init__(self, inp):
        self.inp = inp
        self.upperCases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lowerCases = self.upperCases.lower()
        self.numbers = "1234567890"
        self.characters = self.upperCases + self.lowerCases + self.numbers
        self.passwd = self.generatePasswd()

    def generatePasswd(self):
        passwd = ""

        for i in range(int(self.inp)):
            r = random.randint(0,len(self.characters)-1)
            passwd += self.characters[r]
            i+=1
        return passwd


controller = Controller()
controller.runMenu()
p = Password(controller.inp)
print("GENERATED PASSWORD IS: "+p.passwd)