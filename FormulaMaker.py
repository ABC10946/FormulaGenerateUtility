import random
import math
import Poland


class FormulaMaker:
    #initialize
    def __init__(self):
        self.pc = Poland.Calculator()

    #generating formula
    #length must be an odd number but if it is not odd number,program change number to odd one.
    def make(self,length):
        if length%2 == 0:
            length += 1

        self.formula = []

        for i in range(length):
            choice = random.randint(0,6)
            if choice == 0:
                self.formula.append("+")
            elif choice == 1:
                self.formula.append("-")
            elif choice == 2:
                self.formula.append("*")
            elif choice == 3:
                self.formula.append("/")
            elif choice == 4:
                self.formula.append("x")
            elif choice == 5:
                self.formula.append("^")
            else:
                self.formula.append(str(random.randint(0,9)))

        return 0

    #check formula possible calculate
    def checkPossibleCalc(self):
        self.pc.input_formula(self.show_formula())
        return self.pc.calc(1)

    #formula
    def show_formula(self):
        return " ".join(map(str,self.formula))

def main():
    import sys
    import random

    fm = FormulaMaker()
    formulaLength = random.randint(2,15)
    if formulaLength%2 == 0:
        formulaLength += 1

    def check():
        fm.make(formulaLength)
        return fm.checkPossibleCalc()

    while check() == False:
        check()

    return fm.show_formula()

if __name__ == "__main__":
    print main()
