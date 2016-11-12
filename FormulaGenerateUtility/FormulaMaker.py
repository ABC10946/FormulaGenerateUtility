import random

class Tree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class FormulaMaker:
    def __init__(self):
        self.formula = []

    def make_basic_tree(self):
        ope = random.choice(["+","-","*","/"])
        left = random.choice(list(map(str,list(range(1,10))))+["x"])
        right = random.choice(list(map(str,list(range(1,10))))+["x"])
        return Tree(ope,Tree(left),Tree(right))

    def glow_tree(self,tree):
        choice = random.choice([0,1,2]) #0:left,1:right

        if choice == 0:
            tree.left = self.make_basic_tree()
            self.glow_tree(tree.left)
        elif choice == 1:
            tree.right = self.make_basic_tree()
            self.glow_tree(tree.right)

        return tree

    def gen_formula(self,tree):
        self.formula.append(tree.value)
        if tree.left is not None:
            self.gen_formula(tree.left)

        if tree.right is not None:
            self.gen_formula(tree.right)

        return " ".join(self.formula)

    def make(self):
        fm = FormulaMaker()
        tree = fm.make_basic_tree()
        tree = fm.glow_tree(tree)
        return fm.gen_formula(tree)
