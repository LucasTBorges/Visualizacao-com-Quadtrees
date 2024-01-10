import mat

import sys

from cArvore import cArvore
from cQuadrado import cNo
from cLista import cLista

import pyglet
from pyglet import shapes
from pyglet.window import Window
from pyglet.window import key

WIN_X = 1024
WIN_Y = 1024

def getObjeto():
    try:
        return int(sys.argv[1])
    except:
        objeto = input(f'Escolha um objeto a ser visualizado (entre 0 e {len(mat.funcoes) - 1})')
    try:
        objeto = int(objeto)
        if objeto >= 0 and objeto <= len(mat.funcoes) - 1:
            return objeto
        else:
            print(f'\n"{objeto}" está fora do intervalo definido. Tente novamente.\n')
            return getObjeto()
    except:
        print(f'\nO valor inserido deve ser um número. Tente novamente.\n')
        return getObjeto()

def getVisual():
    try:
        return int(sys.argv[2])
    except:
        visu = input("Escolha uma forma de visualizar o objeto (Entre 0 e 2)")
    try:
        visu = int(visu)
        if visu >= 0 and visu <= 2:
            return visu
        else:
            print(f'\n"{visu}" está fora do intervalo definido. Tente novamente.\n')
            return getVisual()
    except:
        print(f'\nO valor inserido deve ser um número. Tente novamente.\n')
        return getVisual()

def getPrecisao():
    try:
        return int(sys.argv[3])
    except:
        precisao = input("Escolha o nível inicial de refinamento da imagem apresentada.")
    try:
        precisao = int(precisao)
        if precisao >= 0 and precisao <= 10:
            return precisao
        else:
            print(f'\n"{precisao}" está fora do intervalo definido. Tente novamente.\n')
            return getPrecisao()
    except:
        print(f'\nO valor inserido deve ser um número. Tente novamente.\n')
        return getPrecisao()



def gameLoop():
    global debug, arvore, backgroundWhite, backgroundBlack, nome, funcao, precisao, visual, objeto, WIN_X, WIN_Y, window, atualizar
    arvore = cArvore(funcao, precisao)
    window = pyglet.window.Window(WIN_X, WIN_Y)
    window.set_caption(nome)
    backgroundWhite = shapes.Rectangle(0, 0, 1024, 1024, color = (255, 255, 255))
    backgroundBlack = shapes.Rectangle(x=0, y=0, width = 1024, height = 1024, color = (0, 0, 0),)
    def quadBranco(no, batch):
        #Gera um quadrado branco baseado num nó da árvore
        x = mat.janela(no.getCoordenadaX())
        y = mat.janela(no.getCoordenadaY())
        w = mat.quadSize(no.getProfundidade())
        h = w
        return shapes.Rectangle(x, y, w, h, color = (255, 255, 255), batch=batch)
    
    def grid(no, batch):
        x = mat.janela(no.getCoordenadaX())
        y = mat.janela(no.getCoordenadaY())
        w = mat.quadSize(no.getProfundidade())
        h = w
        if no.isPonto():
            return shapes.BorderedRectangle(x, y, w, h, border = 2, border_color=mat.cores[no.getProfundidade()],color = (255, 255, 255), batch=batch)
        else:
            return shapes.BorderedRectangle(x, y, w, h, border = 2, border_color=mat.cores[no.getProfundidade()],color = (0,0,0), batch=batch)
    
    def area(no, batch):
        x = mat.janela(no.getCoordenadaX())
        y = mat.janela(no.getCoordenadaY())
        w = mat.quadSize(no.getProfundidade())
        h = w
        if no.isPonto():
            return shapes.Rectangle(x, y, w, h, color = (0, 255, 0), batch=batch)
        if no.isMaior():
            return shapes.Rectangle(x, y, w, h, color = (255, 0, 0), batch=batch)
        return shapes.Rectangle(x, y, w, h, color = (0, 0, 255), batch=batch)
        

        
    def on_draw():
        batch = pyglet.graphics.Batch()
        window.clear()
        shapeslist = cLista()
        if visual == 0:
            for i in arvore.getPontos():
                shapeslist.insereNo(quadBranco(i.getDado(), batch))
        elif visual == 1:
            for i in arvore.getFolhas():
                shapeslist.insereNo(grid(i.getDado(), batch))
        else:
            for i in arvore.getFolhas():
                shapeslist.insereNo(area(i.getDado(), batch))
        batch.draw()
        if debug:
            pyglet.text.Label(f'Precisão Global: {precisao}; Precisão da Árvore: {arvore.getPrecisao()}; Número de quadrados: {len(shapeslist)}; Objeto:{mat.nomes[objeto]}; Visualização:{visual}', font_name='Times New Roman', font_size = 10, color = (255, 0, 255, 255), x = 25, y = 995).draw()
    
    def on_key_press(symbol, modifiers):
        global visual, precisao, arvore, objeto, debug, atualizar
        atualizar = True
        if symbol == pyglet.window.key.D:
            precisao = arvore.aumentarPrecisao()
        elif symbol == pyglet.window.key.A:
            precisao = arvore.reduzirPrecisao()
        elif symbol == pyglet.window.key.W:
            if visual < 2:
                visual += 1
            else:
                visual = 0
        elif symbol == pyglet.window.key.S:
            if visual > 0: 
                visual -= 1
            else:
                visual = 2
        elif symbol == pyglet.window.key.E:
            if objeto < len(mat.funcoes) - 1:
                objeto += 1
            else:
                objeto = 0
            funcao = mat.funcoes[objeto]
            window.set_caption(mat.nomes[objeto])
            arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key.Q:
            if objeto > 0:
                objeto -= 1
            else:
                objeto = len(mat.funcoes) - 1
            window.set_caption(mat.nomes[objeto])
            funcao = mat.funcoes[objeto]
            arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key._1:
            objeto = 0
            funcao = mat.funcoes[0]
            window.set_caption(mat.nomes[objeto])
            arvore = arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key._2:
            objeto = 1
            funcao = mat.funcoes[1]
            window.set_caption(mat.nomes[objeto])
            arvore = arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key._3:
            objeto = 2
            funcao = mat.funcoes[2]
            window.set_caption(mat.nomes[objeto])
            arvore = arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key._4:
            objeto = 3
            funcao = mat.funcoes[3]
            window.set_caption(mat.nomes[objeto])
            arvore = arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key._5:
            objeto = 4
            funcao = mat.funcoes[4]
            window.set_caption(mat.nomes[objeto])
            arvore = arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key._6:
            objeto = 5
            funcao = mat.funcoes[5]
            window.set_caption(mat.nomes[objeto])
            arvore = arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key._7:
            objeto = 6
            funcao = mat.funcoes[6]
            window.set_caption(mat.nomes[objeto])
            arvore = arvore = cArvore(funcao, precisao)
        elif symbol == pyglet.window.key.F:
            debug = not debug


    window.push_handlers(on_draw)
    window.push_handlers(on_key_press)
    pyglet.app.run()

        
if __name__ == '__main__':
    debug = False
    try:
        if int(sys.argv[4]) == 1:
            debug = True
    except:
        pass

    objeto = getObjeto()
    funcao = mat.funcoes[objeto]
    nome = mat.nomes[objeto]

    visual = getVisual()

    precisao = getPrecisao()

    gameLoop()