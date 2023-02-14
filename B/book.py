class book:
    def __init__(self, nombre, año, páginas, tapa, color, idioma):
        self.nombre = nombre
        self.año = año
        self.páginas = páginas
        self.tapa = tapa
        self.color = color
        self.idioma = idioma

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getAño(self):
         return self.año
    def setAño(self, año):
        self.año = año

    def getPáginas(self):
        return self.páginas
    def setPáginas(self, páginas):
        self.páginas = páginas

    def getTapa(self):
        return self.tapa
    def setTapa(self, tapa):
        self.tapa = tapa

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getIdioma(self):
        return self.idioma
    def setIdioma(self, idioma):
        self.idioma = idioma

    def info(self):
        print("EL nombre del libro es: " + self.nombre)
        print("Es del año: " + self.año)
        print("Tiene " + self.páginas + " páginas")
        print("La tapa es " + self.tapa)
        print("El color del libro es " + self.color)
        print("El idioma es: " + self.idioma)