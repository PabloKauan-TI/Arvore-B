from No import BTreeNode

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.append(root)
            new_root.split_child(0)
            idx = 0
            if key > new_root.keys[0]:
                idx += 1
            new_root.children[idx].insert_non_full(key)
            self.root = new_root
        else:
            root.insert_non_full(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node
        elif node.leaf:
            return None
        else:
            return self._search(node.children[i], key)

    def get_max_level(self):
            return self._get_max_level(self.root)

    def _get_max_level(self, node):
        if node.leaf:
            return 0
        else:
            return 1 + max(self._get_max_level(child) for child in node.children)

    def print_tree(self):
        with open("saida.txt", 'w') as arquivo:
            arquivo.write("")

        if not self.root:
            with open("saida.txt", 'w') as arquivo:
                arquivo.write("The tree is empty.")
                return
        
        with open("saida.txt", 'a') as arquivo:
            arquivo.write(str(self.t) + " " + str(self.get_max_level() + 1) + "\n")
            
        
        queue = [(self.root, 0)]  # Fila de nós para BFS com seus níveis
        current_level = 0
        level_nodes = []

        while queue:
            node, level = queue.pop(0)
            
            if level > current_level:
                with open("saida.txt", 'a') as arquivo:
                    arquivo.write(f"Level {current_level}: {' - '.join(level_nodes)}\n")
                level_nodes = []
                current_level = level
            
            level_nodes.append('[' + ' '.join(map(str, node.keys)) + ']')

            for child in node.children:
                queue.append((child, level + 1))
        
        # Print the last level
        if level_nodes:
            with open("saida.txt", 'a') as arquivo:
                arquivo.write(f"Level {current_level}: {' - '.join(level_nodes)}")
