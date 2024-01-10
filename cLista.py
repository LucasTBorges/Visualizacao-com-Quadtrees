from cNoLista import cNoLista

class cLista:
    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None

    def insereNo(self, dado):
        novoNo = cNoLista()
        novoNo.setDado(dado)
        novoNo.setProx(None)
        if self.tamanho != 0:
          self.fim.setProx(novoNo)
          self.fim = novoNo
          self.tamanho += 1
        else:
          self.inicio = novoNo
          self.fim = self.inicio
          self.tamanho += 1

    def __getitem__(self, index):
        no = self.inicio
        for i in range(index):
            try:
                no = no.getProx()
            except:
                raise IndexError("Tentativa de acessar item não existente da lista")
        return no.getDado()

    def __iter__(self):
        self.noAtual = self.inicio
        return self

    def __next__(self):
        if self.noAtual is not None:
            iteracao = self.noAtual
            self.noAtual = self.noAtual.getProx()
            return iteracao
        else:
            del self.noAtual
            raise StopIteration

    def __len__(self):
        return self.tamanho

    def concatenar(self, novalista):
        for i in novalista:
            self.insereNo(i.getDado())
