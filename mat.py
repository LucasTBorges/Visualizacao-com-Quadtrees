from cLista import cLista
from math import sin, cos

#Esse módulo contém as funções que descrevem operações matemáticas utilizadas no algoritmo utilizado para "desenhar"
#o gráfico no PyGlet, considerando uma janela de 1024 x 1024.

def quadSize(profundidade):
    #Retorna o tamanho de um quadrado de uma dada profundidade dele na árvore
    return 2 ** (10-profundidade)

def numQuads(precisao):
    #Retornar o número de seções da "grade" invisível que divide a janela
    return (1024 * (1/quadSize(precisao)))**2

def janela(x):
    #Retorna uma coordenada na janela do PyGlet dada uma coordenada no plano cartesiano gerado pela função
    return (x+4) * 128

def cartesiano(x):
    #Retorna uma coordenada no plano cartesiano dada uma coordenada na janela do PyGlet
    return (x/128) - 4

def distancia(x):
    #Dada uma distância em pixels, retorna a distância no plano cartesiano.
    return (x/128)

#As expressoes que representam os objetos implícitos:
def laco(x, y):
    return x**7 - y**5 + x**2 * y**3 - (x*y)**2

def rotatoria(x, y):
    return x**2 + y**2 + x*y - (x*y)**2 * 0.5 - 0.25

def cardioide(x, y):
    return (x**2 + y**2 - 4)**3 - x**2 * y**3

def losango(x, y):
    return abs(x) + abs(y) - 2

def ventilador(x, y):
    return x**2 - y**2 + y**3 - x**3 + x*y**2 + x*y**3

def gaspar(x, y):
    return x**6 - y**5 + x**4 + y**3 - x**2

def chinchila(x, y):
    sinx = sin(1.6*(-abs(x)-0.8))
    siny = sin(1.6*(y-0.8))
    return (((x**2/(y**2 + 2 ** -10)) * sinx)+ y**2 - x**2 * siny - 1)

funcoes = cLista()
funcoes.insereNo(laco)
funcoes.insereNo(rotatoria)
funcoes.insereNo(cardioide)
funcoes.insereNo(losango)
funcoes.insereNo(ventilador)
funcoes.insereNo(gaspar)
funcoes.insereNo(chinchila)

nomes = cLista()
nomes.insereNo("Laço")
nomes.insereNo("Rotatória")
nomes.insereNo("Cardioide")
nomes.insereNo("Losango")
nomes.insereNo("Ventilador")
nomes.insereNo("Gaspar")
nomes.insereNo("Chinchila")

cores = cLista()
cores.insereNo((44, 77, 221))
cores.insereNo((62, 72, 209))
cores.insereNo((81, 66, 197))
cores.insereNo((99, 61, 184))
cores.insereNo((117, 55, 172))
cores.insereNo((136, 50, 160))
cores.insereNo((154, 44, 148))
cores.insereNo((172, 39, 136))
cores.insereNo((190, 33, 123))
cores.insereNo((209, 28, 111))
cores.insereNo((227, 22, 99))
