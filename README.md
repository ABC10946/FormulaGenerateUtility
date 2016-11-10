# FormulaGenerateUtility

This programs are utility for calculate the formula that written in Polish Notation.

# Require Environment

- Python3

# Usage

#### main.py
This program generate random formula that written in Polish Notation.  
And,This program also calculate the formula.  
x = {0,1,2,3,4,5,6,7,8,9}

Example
```bash
$ python main.py
^ 4 + 6 + x + 6 * x x #generated forula and bottoms are answers.
x = 0:16777216.0
x = 1:268435456.0
x = 2:68719476736.0
x = 3:281474976710656.0
x = 4:1.8446744073709552e+19
x = 5:1.9342813113834067e+25
x = 6:3.2451855365842673e+32
x = 7:8.711228593176025e+40
x = 8:3.7414441915671115e+50
x = 9:2.5711008708143844e+61
```

#### PolishFormulaCalculateUtility
This is utility for calculate the formula that written in Polish Notation.  

##### Class:Calculator(void)  
######  methods  
- input_formula(string text)  -- return None  
  input formula that string text.

- show_formula(void)  -- return None  
  show inputted formula.

- calc(void or int value)  -- return Bool value  
  calculate the formula that written in Polish Notation.  
  if error happend in calculate phase,this function return error message.  

  error messages:
  - Formula Error
  - Zero Division Error
  - Overflow Error
  - Value Error  


- output(void) -- return float value  
output answer.

#### FormulaMaker
This is utility for generate the formula that written in Polish Notation.  
##### Class:FormulaMaker(void)

###### methods  
- make(int length)  -- return None  
generate not checked formula.

- checkPossibleCalc(void)  -- return Bool value  
check that the formula can be calculate.

- show_formula(void) -- return string value  
output formula.
