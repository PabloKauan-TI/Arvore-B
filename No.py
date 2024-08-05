class No:
    def __init__(self, ordem, folha=False):
        self.ordem = ordem
        self.folha = folha  
        self.chaves = []  
        self.filhos = [] 

    def inserir_incompleto(self, chave):
        i = len(self.chaves) - 1

        if self.folha:
            self.chaves.append(None)
            while i >= 0 and chave < self.chaves[i]:
                self.chaves[i + 1] = self.chaves[i]
                i -= 1
            self.chaves[i + 1] = chave
        else:
            while i >= 0 and chave < self.chaves[i]:
                i -= 1
            i += 1
            if len(self.filhos[i].chaves) == 2 * self.ordem - 1:
                self.dividi_pagina(i)
                if chave > self.chaves[i]:
                    i += 1
            self.filhos[i].inserir_incompleto(chave)

    def dividi_pagina(self, i):
        ordem = self.ordem
        y = self.filhos[i]
        z = No(ordem, y.folha)
        self.filhos.insert(i + 1, z)
        self.chaves.insert(i, y.chaves[ordem - 1])

        z.chaves = y.chaves[ordem:(2 * ordem - 1)]
        y.chaves = y.chaves[0:(ordem - 1)]

        if not y.folha:
            z.filhos = y.filhos[ordem:(2 * ordem)]
            y.filhos = y.filhos[0:(ordem)]
