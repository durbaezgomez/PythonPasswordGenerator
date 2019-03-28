import random

class Password:

    def __init__(self):
        self.upperCases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lowerCases = self.upperCases.lower()
        self.numbers = "1234567890"
        self.characters = self.upperCases + self.lowerCases + self.numbers
        self.passwd = self.generatePasswd()

    def generatePasswd(self):
        passwd = ""

        for i in range(10):
            r = random.randint(0,len(self.characters)-1)
            passwd += self.characters[r]
            i+=1
        return passwd

p = Password()
print("GENERATED PASSWORD IS: "+p.passwd)