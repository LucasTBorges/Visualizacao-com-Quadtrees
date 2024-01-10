from cQuadrado import cNo
from cLista import cLista
import mat

class cArvore:
    def __init__(self, funcao, precisao = 0):
        self.precisao = precisao
        self.raiz = cNo(0, -1, -4, -4, funcao)
        self.funcao = funcao
        self.nos = cLista()
        self.nos.insereNo(self.raiz)

        if self.precisao != 0:
            resolucao = self.getPrecisao()
            self.precisao = 0
            for i in range(resolucao):
                self.aumentarPrecisao()

    def getPrecisao(self):
        return self.precisao

    def getRaiz(self):
        return self.raiz

    def subdividir(self, no):
        filho0 = cNo(no.getProfundidade() + 1, 0, x = no.getCoordenadaX(), y = no.getCoordenadaY() + mat.distancia(mat.quadSize(no.getProfundidade() + 1)), funcao = self.funcao)
        filho1 = cNo(no.getProfundidade() + 1, 1, x = no.getCoordenadaX() + (mat.distancia(mat.quadSize(no.getProfundidade() + 1))), y = no.getCoordenadaY() + mat.distancia(mat.quadSize(no.getProfundidade() + 1)), funcao = self.funcao)
        filho2 = cNo(no.getProfundidade() + 1, 2, x = no.getCoordenadaX(), y = no.getCoordenadaY(), funcao = self.funcao)
        filho3 = cNo(no.getProfundidade() + 1, 3, x = no.getCoordenadaX() + mat.distancia(mat.quadSize(no.getProfundidade() + 1)), y = no.getCoordenadaY(), funcao = self.funcao)
        self.nos.insereNo(filho0)
        self.nos.insereNo(filho1)
        self.nos.insereNo(filho2)
        self.nos.insereNo(filho3)
        no.setFilho(0, filho0)
        no.setFilho(1, filho1)
        no.setFilho(2, filho2)
        no.setFilho(3, filho3)

        #Para Debug
        #print((mat.distancia(mat.quadSize(no.getProfundidade() + 1))), "Distancia")
        #print(mat.quadSize(no.getProfundidade() + 1), "Quadsize")
        #print(no.getProfundidade() + 1, "Profundidade do filho")
        #print(filho0.getCoordenadaX(), filho0.getCoordenadaY(), "filho 0")
        #print(filho1.getCoordenadaX(), filho1.getCoordenadaY(), "filho 1")
        #print(filho2.getCoordenadaX(), filho2.getCoordenadaY(), "filho 2")
        #print(filho3.getCoordenadaX(), filho3.getCoordenadaY(), "filho 3")

    def getNos(self):
        return self.nos

    def getFolhas(self, no = None):
        if no is None:
            no = self.raiz
        lista = cLista()
        if no.isFolha():
            lista.insereNo(no)
            return lista
        else:
            for i in range(4):
                lista.concatenar(self.getFolhas(no.getFilho(i)))
            return lista

    def getPontos(self):
        folhas = self.getFolhas(self.raiz)
        lista = cLista()
        for i in folhas:
            if i.getDado().isPonto():
                lista.insereNo(i.getDado())
        return lista

    def getPaisDeFolhas(self, no):
        lista = cLista()
        if no is None:
            return lista
        if no.getProfundidade() == self.precisao - 1:
            lista.insereNo(no)
            return lista
        else:
            for i in range(4):
                lista.concatenar(self.getPaisDeFolhas(no.getFilho(i)))
            return lista

    def aumentarPrecisao(self):
        if self.precisao < 10:
            self.precisao += 1
            for i in self.getPontos():
                self.subdividir(i.getDado())
        return self.precisao

    def reduzirPrecisao(self):
        if self.precisao > 0:  
            for i in self.getPaisDeFolhas(self.raiz):
                for j in range(4):
                    i.getDado().setFilho(j, None)
            self.precisao -= 1
        return self.precisao
        
    def getQuadradoLado(self):
        return 2 ** (10 - self.precisao)
