class ClassSpells:
    def __init__(self, className, spellList):
        self.name = className
        self.list = spellList

    def __str__(self):
        stri = self.name + "\n"
        for s in self.list:
            stri += (str(s) + "\n")
        return stri
