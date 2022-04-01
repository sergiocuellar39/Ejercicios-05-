class Galleta:

    def __init__(self, sabor="dulce", chocolate=False):
        self.sabor = sabor
        self.chocolate = chocolate

    def __str__(self):
        resumen = "Soy una galletita " + self.sabor
        if self.chocolate:
            resumen += " con chocolate"
        return resumen  # debe devolver una cadena

    def chocolatear(self):
        self.chocolate = True


galleta = Galleta()
print(galleta)