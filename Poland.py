import math


class Calculator:
    def __init__(self):
        pass
    
    def input_formula(self,text):
        self.text = text

    def show_formula(self):
        return self.text

    def calc(self,x=0):
        self.word = self.text.split(" ")

        idx = 0

        while len(self.word) > idx:
            if self.word[idx].isdigit():
                self.word[idx] = float(self.word[idx])
            elif self.word[idx] == "x":
                self.word[idx] = float(x)

            idx += 1
        
        ret = True
        idx = 0

        try:
            while len(self.word) > 1:
                if self.word[idx] == "+":
                    if isinstance(self.word[idx+1],float) and isinstance(self.word[idx+2],float):
                        self.word[idx] = self.word[idx+1] + self.word[idx+2]
                        del self.word[idx+1]
                        del self.word[idx+1]
                        idx = 0
                    else:
                        idx += 1

                elif self.word[idx] == "-":
                    if isinstance(self.word[idx+1],float) and isinstance(self.word[idx+2],float):
                        self.word[idx] = self.word[idx+1] - self.word[idx+2]
                        del self.word[idx+1]
                        del self.word[idx+1]
                        idx = 0
                    else:
                        idx += 1

                elif self.word[idx] == "*":
                    if isinstance(self.word[idx+1],float) and isinstance(self.word[idx+2],float):
                        self.word[idx] = (1.0 * self.word[idx+1]) * self.word[idx+2]
                        del self.word[idx+1]
                        del self.word[idx+1]
                        idx = 0
                    else:
                        idx += 1

                elif self.word[idx] == "/":
                    if isinstance(self.word[idx+1],float) and isinstance(self.word[idx+2],float):
                        self.word[idx] = (1.0 * self.word[idx+1]) / self.word[idx+2]
                        del self.word[idx+1]
                        del self.word[idx+1]
                        idx = 0
                    else:
                        idx += 1

                elif self.word[idx] == "^":
                    if isinstance(self.word[idx+1],float) and isinstance(self.word[idx+2],float):
                        self.word[idx] = math.pow(self.word[idx+1],self.word[idx+2])
                        del self.word[idx+1]
                        del self.word[idx+1]
                        idx = 0
                    else:
                        idx += 1

                else:
                    idx += 1


        except IndexError:
            ret = False
            self.word[0] = "Error!"
        except ZeroDivisionError:
            ret = False
            self.word[0] = "Zero Division Error!"
        except OverflowError:
            ret = False
            self.word[0] = "Value Large Error!"
        except ValueError:
            ret = False
            self.word[0] = "Value Large Error!"

        
        return ret

    def output(self):
        return self.word[0]
