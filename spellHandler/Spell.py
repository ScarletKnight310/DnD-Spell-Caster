class Spell:
    # sourcebook-page : detail + per spell == desc
    # V, S, M == comp
    def __init__(self, name, lvl, isRitual, castTime, spRange, targetArea, v, s, m, component, cost, isCon, dura,
                 attack_SaveThrow, damageType, healthChange, page, additional_desc, perHigherLvldesc,
                 usableClass):
            self.name = name  #
            self.lvl = int(lvl)  #
            #
            self.isRitual = isRitual != ""
            self.isConcentration = isCon != ""
            #
            self.castTime = castTime  #
            self.spRange = spRange + " - " + targetArea  #
            self.duration = dura  #
            #
            self.components = [v, s, m, component, cost]  #
            #
            self.effect = [damageType, healthChange, attack_SaveThrow]
            self.desc = "# " + page + ": " + additional_desc + " " + perHigherLvldesc
            self.usableGroup = usableClass

    def __str__(self):
            return self.name + " [" + self.usableGroup + "]\nLevel: " + str(self.lvl) + "\nCasting Time: " + self.castTime \
                + "\nRange: " + self.spRange + "\nComponents: " + str(self.components) + "\nDuration: " + self.duration \
                + "\n" + str(self.effect) + "\n" + str(self.desc) + "\n"

    def containsClass(self, classList):
        for c in classList:
            if c in self.classes:
                return True
        return False
