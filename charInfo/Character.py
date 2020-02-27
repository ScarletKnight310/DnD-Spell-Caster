class Character:

    def __init__(self, name, class_lvlList, spells):
        self.name = name
        self.class_lvlList = class_lvlList
        self.usableSpells = spells
        self.allSpells = spells
        self.filterSp(spells)

    def editClass(self, newClassList):
        self.classList = newClassList
        self.filterSp()

    def editLevel(self, lvl):
        self.lvl = lvl
        self.filterSp()

    def levelUp(self,):
        self.lvl = self.lvl + 1
        self.filterSp()

    def filterSp(self):
        self.usableSpells = filter(lambda s: s.lvl == self.lvl and s.containsClass(), self.allSpells)

    def __str__(self):
        s = self.name + "\nLvl " + str(self.lvl) + "\n"