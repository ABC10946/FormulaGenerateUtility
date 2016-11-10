import random
import math
from FormulaGenerateUtility.PolishFormulaCalculateUtility import Calculator

class FormulaMaker:
    #initialize
    def __init__(self):
        self.calculator = Calculator()

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


    #check formula possible calculate
    def checkPossibleCalc(self):
        self.calculator.input_formula(self.show_formula())
        return self.calculator.calc(1)

    #formula
    def show_formula(self):
        return " ".join(map(str,self.formula))
