class Character:

    def __init__(self, name, classes, spells):
        self.name = name
        self.classes = classes
        self.allSpells = spells
        self.usableSpells = self.setusableSp(spells)

    def lvlUp(self, className):
        for c in range(0, len(self.classes)):
            if className in self.classes[c][0]:
                self.classes[c][1] += 1

    def lvlUpAll(self, className):
        for c in range(0, len(self.classes)):
            self.classes[c][1] += 1

    def addClass(self, newClass):
        self.classes.append(newClass)

    def setusableSp(self, spells):
        sp = []
        # for clSpell in spells:
        return sp
    #def __str__(self):