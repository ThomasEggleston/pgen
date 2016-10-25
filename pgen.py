HELP_STRING = ""
TAGS = ['l','u','d','o']

import sys, random, string

class Pgen:
    def __init__(self, tags, length):
        self.tags = tags
        if tags != "":
            self.checkTags()
        self.length = length
        self.checkLength()
        self.characters = []
        self.setCharacters()

    def password(self):
        password = ""
        for i in range(int(self.length)):
            c = self.getRandom()
            password += self.characters[c]
        print(password)

    def getRandom(self):
        return int(random.uniform(0, len(self.characters)))

    def setCharacters(self):
        tags = self.tags.lower()
        if tags == "":
            self.addCharRange(33, 127)
        else:
            if 'l' in tags:
                self.addCharRange(97, 123)
            if 'u' in tags:
                self.addCharRange(65, 91)
            if 'd' in tags:
                self.addCharRange(48, 58)
            if 'o' in tags:
                self.addCharRange(33, 48)
                self.addCharRange(58, 65)
                self.addCharRange(91, 97)
                self.addCharRange(123, 127)

    def addCharRange(self, lower, upper):
        for i in range(lower, upper):
            self.characters.append(chr(i))

    def checkTags(self):
        if self.tags[0] != '-' or len(self.tags) < 2:
            print("Error: Incorrect options tag. Must be of from -Options")
            print(HELP_STRING)
            exit()
        tags = []
        for c in self.tags[1:]:
            if c.lower() in TAGS:
                if c not in tags:
                    tags.append(c)
                else:
                    print("Error: Tag duplicate")
            else:
                print("Error: Unknown tag specified")
                print(HELP_STRING)


    def checkLength(self):
        length = self.length
        if len(length) == 0:
            print("Error: Length not given")
            exit()
        for c in length:
            if c not in string.digits:
                print("Error: Length must be given as a number")
                exit()
        if int(length) == 0:
            print("Error: Password length must be at least 1")
            exit()
        if int(length) > 128:
            print("Error: Maximum password length is 128")
            exit()

if __name__ == '__main__':
    numArgs = len(sys.argv) - 1
    if numArgs == 0:
        print("Error: No arguments given")
        print(HELP_STRING)
        exit()
    elif numArgs > 2:
        print("Error: Too many arguments given")
        print(HELP_STRING)
        exit()
    if numArgs == 1:
        p = Pgen("", sys.argv[1])
        p.password()
    elif numArgs == 2:
        p = Pgen(sys.argv[1], sys.argv[2])
        p.password()
