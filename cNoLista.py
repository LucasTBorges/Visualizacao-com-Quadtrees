class cNoLista:
    def __init__(self):
        self.dado = None
        self.prox = None

    def setDado(self,dado):
        self.dado = dado

    def getDado(self):
        return self.dado

    def setProx(self, no):
        self.prox = no

    def getProx(self):
        return self.prox

    def __str__(self):
        return str(self.dado)