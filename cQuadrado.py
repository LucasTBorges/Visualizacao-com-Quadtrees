import mat
from cLista import cLista as lista

class cNo:
    def __init__(self, profundidade = 0, posicao = 0, x = 0, y = 0, funcao = mat.laco):
        self.filho0 = None
        self.filho1 = None
        self.filho2 = None
        self.filho3 = None
        self.posicao = posicao
        self.profundidade = profundidade
        if self.profundidade <= 1:
            self.temPonto = True
        else:
            verticeSO = lista()
            verticeSO.insereNo(x)
            verticeSO.insereNo(y)

            verticeSE = lista()
            verticeSE.insereNo(x + mat.distancia(mat.quadSize(profundidade)))
            verticeSE.insereNo(y) 

            verticeNO = lista()
            verticeNO.insereNo(x)
            verticeNO.insereNo(y + mat.distancia(mat.quadSize(profundidade)))

            verticeNE = lista()
            verticeNE.insereNo(x + mat.distancia(mat.quadSize(profundidade)))
            verticeNE.insereNo(y + mat.distancia(mat.quadSize(profundidade)))

            SO = funcao(verticeSO[0], verticeSO[1])
            SE = funcao(verticeSE[0], verticeSE[1])
            NO = funcao(verticeNO[0], verticeNO[1])
            NE = funcao(verticeNE[0], verticeNE[1])
            #print(SO, "SO")
            #print(SE, "SE")
            #print(NO, "NO")
            #print(NE, "NE")

            if (SO == 0 or SE == 0 or NO == 0 or NE == 0):
                self.temPonto = True

            elif (SO > 0 and SE > 0 and NO > 0 and NE > 0):
                self.maior = True
                self.temPonto = False

            elif (SO < 0 and SE < 0 and NO < 0 and NE < 0):
                self.maior = False
                self.temPonto = False

            else:
                self.temPonto = True

        

        self.posicao = posicao
        self.x = x
        self.y = y

    def isFolha(self):
        return not self.temPonto or (self.temPonto and self.filho0 == None and self.filho1 == None and self.filho2 == None and self.filho3 == None)

    def getProfundidade(self):
        #profundidade na árvore
        return self.profundidade

    def isPonto(self):
        return self.temPonto

    def isMaior(self):
        #Caso não possua um ponto, retorna True caso o resultado da expressão seja maior que zero e False se menor que 0.
        return self.maior

    def getPosicao(self):
        #Retorna um inteiro entre 0 e 3, indicando a posição do quadrado dentro do quadrado-pai (0 = noroeste, 1 = nordeste, 2 = sudoeste, 3 = sudeste)
        return self.posicao

    def setFilho(self, posicao, novoNo):
        if posicao == 0:
            self.filho0 = novoNo
        elif posicao == 1:
            self.filho1 = novoNo
        elif posicao == 2:
            self.filho2 = novoNo
        elif posicao == 3:
            self.filho3 = novoNo
        else:
            raise RuntimeError(f'Tentativa de setar um filho na posição {posicao}')

    def getFilho(self, posicao):
        if posicao == 0:
            return self.filho0
        elif posicao == 1:
            return self.filho1
        elif posicao == 2:
            return self.filho2
        elif posicao == 3:
            return self.filho3
        else:
            raise IndexError(f'Tentativa de resgatar filho na posição {posicao}')

    def getCoordenadaX(self):
        return self.x

    def getCoordenadaY(self):
        return self.y

    def getDado(self):
        return self
