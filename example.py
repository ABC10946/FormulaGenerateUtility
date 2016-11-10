import sys
import random
from FormulaGenerateUtility.PolishFormulaCalculateUtility import Calculator
from FormulaGenerateUtility.FormulaMaker import FormulaMaker

def main():
    calculator = Calculator()
    fm = FormulaMaker()
    formulaLength = random.randint(2,15)
    if formulaLength%2 == 0:
        formulaLength += 1

    fm.make(formulaLength)

    while not fm.checkPossibleCalc():
        fm.make(formulaLength)

    calculator.input_formula(fm.show_formula())


    print(fm.show_formula())
    for i in range(10):
        calculator.calc(i)
        print("x = "+str(i)+":"+str(calculator.output()))

if __name__ == "__main__":
    main()
