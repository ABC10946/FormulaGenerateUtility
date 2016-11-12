# FormulaGenerateUtility

This programs are utility for calculate the formula that written in Polish Notation.

# Require Environment

- Python3

# Usage

#### import this program  
```python
from FormulaGenerateUtility.FormulaMaker import FormulaMaker
from FormulaGenerateUtility.PolishFormulaCalculateUtility import Calculator
#use FormulaMaker
fm = FormulaMaker()
calculator = Calculator()
```

#### example.py
This program generate random formula that written in Polish Notation.  
And,This program also calculate the formula.  
x = {0,1,2,3,4,5,6,7,8,9}


```bash
$ python example.py
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
##### Class:Tree(value,left=None,right=None)

###### Usage
you want to generate tree structure like bottom.

```
#tree structure of "+ 1 2"
#"1" and "2" are leaves.
#but these have value of None

          "+"
     ______|______
    "1"          "2"
  ___|___      ___|___
  |     |      |     |
(None)(None) (None)(None)
```

On use class

```python
tree = Tree("+",Tree("1"),Tree("2"))

tree.right       #=> "2"
tree.right.right #=>None
```

###### methods
- None  

##### Class:FormulaMaker(void)

###### methods  
- make_basic_tree  --  return tree object  
generate base tree on random
- glow_tree(tree)  --  return tree object  
glow tree on random

- make(int length)  --  return string text  
generate formula  
