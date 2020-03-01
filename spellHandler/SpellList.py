from spellHandler.ClassSpells import ClassSpells
from spellHandler.Spell import Spell


class SpellList:
    def __init__(self, filenames):
        self.ClassSpells = []
        for file in filenames:
            self.ClassSpells.append(self.readspells(file))

    def __str__(self):
        stri = "\n"
        for cs in self.ClassSpells:
            stri += (str(cs) + "\n")
        return stri

    def readspells(self, filename):
        file = open(filename, "r")
        spellList = []
        className = self.extractClassName(filename)

        for line in file:
            spellprts = line.split(",")
            if spellprts[19] == "":
                spellList.append(
                    Spell(spellprts[0], spellprts[1], spellprts[2], spellprts[3], spellprts[4], spellprts[5],
                          spellprts[6], spellprts[7], spellprts[8], spellprts[9], spellprts[10], spellprts[11],
                          spellprts[12], spellprts[13], spellprts[14], spellprts[15], spellprts[16], spellprts[17],
                          spellprts[18], className))
            else:
                spellList.append(
                    Spell(spellprts[0], spellprts[1], spellprts[2], spellprts[3], spellprts[4], spellprts[5],
                          spellprts[6], spellprts[7], spellprts[8], spellprts[9], spellprts[10], spellprts[11],
                          spellprts[12], spellprts[13], spellprts[14], spellprts[15], spellprts[16], spellprts[17],
                          spellprts[18], spellprts[19]))

        return ClassSpells(className, spellList)

    def extractClassName(self, filename):
        name = str(filename).split("\\")
        classname = name[len(name) - 1].split(".")
        return classname[0]
