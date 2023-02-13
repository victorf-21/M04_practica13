class school:
    def ___init___(self, altura, nom, cognom, classe, edat, curs):
        self.altura = altura
        self.nom = nom
        self.cognom = cognom
        self. classe= classe
        self.edat = edat
        self.curs = curs

    # # # # # # Apartat 1 # # # # # #
    def getAltura(self):
        return self.altura
    def setAltura(self, altura):
        self.altura = altura

    # # # # # # Apartat 2 # # # # # #
    def getNom(self):
        return self.nom
    def selfNom(self, nom):
        self.nom = nom

    # # # # # # Apartat 3 # # # # # #
    def getCogom(self):
        return self.cognom
    def selfCogom(self, cognom):
        self.cognom = cognom

    # # # # # # Apartat 4 # # # # # #
    def getClasse(self):
        return self.classe
    def selfClasse(self, classe):
        self.classe = classe

    # # # # # # Apartat 5 # # # # # #
    def getEdat(self):
        return self.edat
    def selfEdat(self, edat):
        self.edat = edat

    # # # # # # Apartat 6 # # # # # #
    def getCurs(self):
        return self.curs
    def selfCurs(self, curs):
            self.curs = curs

    # # # # # # Mètode 3 # # # # # #
    def nomInfo(self):
        print("Les dades de school és: " + self.altura + self.nom + self.cognom + self.classe + self.edat + self.curs)

    from school import school
    p3 = school("altura", "nom", "cognom", "classe", "edat", "curs")
    p3.nomInfo()
    """ Esto va una vez creado el main! """