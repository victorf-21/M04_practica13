class animal:
    def ___init___(self, tipus, tamany, pelatge, edat, cua, altura):
        self.tipus = tipus
        self.tamany = tamany
        self.pelatge = pelatge
        self.edat = edat
        self.cua = cua
        self.altura = altura

    # # # # # # Apartat 1 # # # # # #
    def getTipus(self):
        return self.tipus
    def setTipus(self, tipus):
        self.tipus = tipus

    # # # # # # Apartat 2 # # # # # #
    def getTamany(self):
        return self.tamany
    def setTamant(self, tamany):
        self.tamany = tamany

    # # # # # # Apartat 3 # # # # # #
    def getPelatge(self):
        return self.pelatge
    def setPelatge(self, pelatge):
        self.pelatge = pelatge

    # # # # # # Apartat 4 # # # # # #
    def getEdat(self):
        return self.edat
    def setEdat(self, edat):
        self.edat = edat

    # # # # # # Apartat 5 # # # # # #
    def getCua(self):
        return self.cua
    def setCua(self, cua):
        self.cua = cua

    # # # # # # Apartat 6 # # # # # #
    def getAltura(self):
        return self.altura
    def setAltura(self, altura):
        self.altura = altura

    # # # # # # Mètode 1 # # # # # #
    def salutacio(self):
        print("Les dades del animal és: " + self.tipus)
        print("El tamany és: " + self.tamany)
        print ("El seu pelatge és" + self.pelatge)
        print ( "La seva edat és " + self.edat)
        print("la seva cua és: " +  self.cua)
        print("La seva altura es:" + self.altura)