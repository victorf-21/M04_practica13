class user:
    def __init__(self, nombre, edad, sexo, nacionalidad, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad
        self.altura = altura
        self.peso = peso

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
         return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def getSexo(self):
        return self.sexo
    def setSexo(self, sexo):
        self.sexo = sexo

    def getNacionalidad(self):
        return self.nacionalidad
    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def getAltura(self):
        return self.altura
    def setAltura(self, altura):
        self.altura = altura

    def getPeso(self):
        return self.peso
    def setPeso(self, peso):
        self.peso = peso

    def salutacio(self):
        print("El nombre del usuario es: " + self.nombre)
        print("Su edad es: " + self.edad)
        print("Su sexo es: " + self.sexo)
        print("Su nacionalidad es: " + self.nacionalidad)
        print("Su altura es: " + self.altura)
        print("Su peso es: " + self.peso)