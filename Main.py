from ArvoreB import BTree

if __name__ == "__main__":
    elementos = None
    arvore = None
    with open("entrada.txt", 'r') as arquivo:
        elementos = arquivo.readlines()

    for i in range(len(elementos)):
        if i==0:
            x = int(elementos[i])
            arvore = BTree(x)
        else:
            x = int(elementos[i])
            arvore.insert(x)

    arvore.print_tree()
