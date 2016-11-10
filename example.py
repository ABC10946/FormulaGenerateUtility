import sys
import random
import FormulaGenerateUtility.PolishFormulaCalculateUtility as PolishFormulaCalculateUtility
import FormulaGenerateUtility.FormulaMaker as FormulaMaker

def main():
    calculator = PolishFormulaCalculateUtility.Calculator()
    fm = FormulaMaker.FormulaMaker()
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
