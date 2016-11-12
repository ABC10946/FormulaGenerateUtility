import sys
import random
from FormulaGenerateUtility.PolishFormulaCalculateUtility import Calculator
from FormulaGenerateUtility.FormulaMaker import FormulaMaker

def main():
    calculator = Calculator()
    fm = FormulaMaker()

    formula = fm.make()
    calculator.input_formula(formula)

    print(formula)
    for i in range(10):
        calculator.calc(i)
        print("x = "+str(i)+":"+str(calculator.output()))

if __name__ == "__main__":
    main()
