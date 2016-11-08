import sys
import random
import FormulaMaker
import PolishFormulaCalculateUtility

def main():
    calculator = PolishFormulaCalculateUtility.Calculator()
    fm = FormulaMaker.FormulaMaker()
    formulaLength = random.randint(2,15)
    if formulaLength%2 == 0:
        formulaLength += 1

    def check():
        fm.make(formulaLength)
        return fm.checkPossibleCalc()

    while check() == False:
        check()

    calculator.input_formula(fm.show_formula())


    print(fm.show_formula())
    for i in range(10):
        calculator.calc(i)
        print("x = "+str(i)+":"+str(calculator.output()))

if __name__ == "__main__":
    main()
