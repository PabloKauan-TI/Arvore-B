class No:
    def __init__(self, t, folha=False):
        self.t = t  # Grau mínimo (define o intervalo de número de chaves)
        self.folha = folha  # Verdadeiro se o nó é uma folha
        self.chaves = []  # Lista de chaves no nó
        self.filhos = []  # Lista de filhos (apenas se não for uma folha)

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
            if len(self.filhos[i].chaves) == 2 * self.t - 1:
                self.dividi_pagina(i)
                if chave > self.chaves[i]:
                    i += 1
            self.filhos[i].inserir_incompleto(chave)

    def dividi_pagina(self, i):
        t = self.t
        y = self.filhos[i]
        z = No(t, y.folha)
        self.filhos.insert(i + 1, z)
        self.chaves.insert(i, y.chaves[t - 1])

        z.chaves = y.chaves[t:(2 * t - 1)]
        y.chaves = y.chaves[0:(t - 1)]

        if not y.folha:
            z.filhos = y.filhos[t:(2 * t)]
            y.filhos = y.filhos[0:(t)]
