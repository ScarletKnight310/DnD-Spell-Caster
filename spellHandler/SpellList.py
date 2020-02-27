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

    def readspells(self,filename):
        file = open(filename, "r")
        spellList = []
        for line in file:
            className = str(file).split("\\\\")
            name = className[len(className) - 1].split(".")
            spellprts = line.split(",")
            spellList.append(Spell(spellprts[0], spellprts[1], spellprts[2], spellprts[3], spellprts[4], spellprts[5],
                               spellprts[6], spellprts[7], spellprts[8], spellprts[9], spellprts[10], spellprts[11],
                               spellprts[12], spellprts[13], spellprts[14], spellprts[15], spellprts[16], spellprts[17],
                               spellprts[18], spellprts[19], name[0]))

        return ClassSpells(name[0], spellList)
