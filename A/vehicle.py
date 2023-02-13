class vehicle:
    def ___init___(self, rodes, marca, portes, antigüetat, color, motor):
        self.rodes = rodes
        self.marca = marca
        self.portes = portes
        self.antigüetat = antigüetat
        self.color = color
        self.motor = motor

    # # # # # # Apartat 1 # # # # # #
    def getRodes(self):
        return self.rodes
    def setRodes(self, rodes):
        self.rodes = rodes

    # # # # # # Apartat 2 # # # # # #
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    # # # # # # Apartat 3 # # # # # #
    def getPortes(self):
        return self.portes
    def getPortes(self, portes):
        self.portes = portes

    # # # # # # Apartat 4 # # # # # #
    def getAntigüetat(self):
        return self.antigüetat
    def setAntigüetat(self, antigüetat):
        self.antigüetat = antigüetat

    # # # # # # Apartat 5 # # # # # #
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    # # # # # # Apartat 6 # # # # # #
    def getMotor(self):
        return self.motor
    def setMotor(self, motor):
        self.motor = motor

    # # # # # # Mètode 2 # # # # # #
    def nomParts(self):
        print("Les dades del vehicle és: " + self.rodes)
        print("La marca es: " + self.marca)
        print("El número de portes es: " + self.tamany)
        print("Te una cantitat de +"  + self.portes + "portes")
        print("La seva antiguetat es: " + self.antigüetat)
        print("El seu es color: " + self.color)
        print("El seu motor es:" + self.motor)