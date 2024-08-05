from No import No

class ArvoreB:
    def __init__(self, ordem):
        self.raiz = No(ordem, True)
        self.ordem = ordem

    def inserir(self, chave):
        raiz = self.raiz
        if len(raiz.chaves) == 2 * self.ordem - 1:
            new_raiz = No(self.ordem, False)
            new_raiz.filhos.append(raiz)
            new_raiz.dividi_pagina(0)
            idx = 0
            if chave > new_raiz.chaves[0]:
                idx += 1
            new_raiz.filhos[idx].inserir_incompleto(chave)
            self.raiz = new_raiz
        else:
            raiz.inserir_incompleto(chave)

    def procurar(self, chave):
        return self.procurar_auxiliar(self.raiz, chave)

    def procurar_auxiliar(self, no, chave):
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1
        if i < len(no.chaves) and chave == no.chaves[i]:
            return no
        elif no.folha:
            return None
        else:
            return self.procurar_auxiliar(no.filhos[i], chave)

    def quantidade_de_niveis(self):
            return self.ultimo_nivel(self.raiz) + 1

    def ultimo_nivel(self, no):
        if no.folha:
            return 0
        else:
            return 1 + max(self.ultimo_nivel(filho) for filho in no.filhos)

    def escrever(self):
        with open("saida.txt", 'w') as arquivo:
            arquivo.write("")

        if not self.raiz:
            with open("saida.txt", 'w') as arquivo:
                arquivo.write("The tree is empty.")
                return
        
        with open("saida.txt", 'a') as arquivo:
            arquivo.write(str(self.ordem) + " " + str(self.quantidade_de_niveis()) + "\n")
            
        
        fila_de_nos = [(self.raiz, 0)] 
        nivel_atual = 0
        nos_do_nivel = []

        while fila_de_nos:
            no, nivel = fila_de_nos.pop(0)
            
            if nivel > nivel_atual:
                with open("saida.txt", 'a') as arquivo:
                    arquivo.write(f"Nivel: {nivel_atual}: {' - '.join(nos_do_nivel)}\n")
                nos_do_nivel = []
                nivel_atual = nivel
            
            nos_do_nivel.append('[' + ' '.join(map(str, no.chaves)) + ']')

            for filho in no.filhos:
                fila_de_nos.append((filho, nivel + 1))
        
        if nos_do_nivel:
            with open("saida.txt", 'a') as arquivo:
                arquivo.write(f"Nivel {nivel_atual}: {' - '.join(nos_do_nivel)}")
