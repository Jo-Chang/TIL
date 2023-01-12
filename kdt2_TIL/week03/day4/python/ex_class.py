class Calculator:
    
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2
        
    def plus(self):
        return (self.number1 + self.number2)
    
    def minus(self):
        return (self.number1 - self.number2)
    
    def multiply(self):
        return (self.number1 * self.number2)
    
    def division(self):
        return (self.number1 // self.number2)
    
    def print(self):
        print(f"number1 = {self.number1}, number2 = {self.number2}")
        print(f"plus    : {self.plus()}")
        print(f"minus   : {self.minus()}")
        print(f"multiply: {self.multiply()}")
        print(f"division: {self.division()}")
        

a, b = map(int, input().split())
c = Calculator(a, b)
c.print()