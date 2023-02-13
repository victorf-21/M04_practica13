class university:
    def __init__(self, nombre, dirección, teléfono, provincia, aulas, estudios):
        self.nombre = nombre
        self.dirección = dirección
        self.teléfono = teléfono
        self.provincia = provincia
        self.aulas = aulas
        self.estudios = estudios

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDirección(self):
         return self.dirección
    def setEdad(self, dirección):
        self.dirección = dirección

    def getTeléfono(self):
        return self.teléfono
    def setTeléfono(self, teléfono):
        self.teléfono = teléfono

    def getProvincia(self):
        return self.provincia
    def setProvincia(self, provincia):
        self.provincia = provincia

    def getAulas(self):
        return self.aulas
    def setAulas(self, aulas):
        self.aulas = aulas

    def getEstudios(self):
        return self.estudios
    def setEstudios(self, estudios):
        self.estudios = estudios

    def info(self):
        print("El nombre del usuario es : " + self.nombre)
        print("Su edad es : " + self.dirección)
        print("Su sexo es :" + self.teléfono)
        print("Su nacionalidad es : " + self.provincia)
        print("Su altura es : " + self.aulas)
        print("El estudio que da es : " + self.estudios)