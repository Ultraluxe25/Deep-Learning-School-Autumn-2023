class Calculator:
    """
    Class implement simple operations
    """
    def __init__(self, a: str, b: str, operator: str, c: str) -> None:
        self.a = a
        self.b = b
        self.operator = operator
        self.c = c
           
            
    def addition(self):
        """
        Function finds unknown number from addition
        """
        if self.a == 'X':
            self.a = int(self.c) - int(self.b)
            return self.a
        elif self.b == 'X':
            self.b = int(self.c) - int(self.a)
            return self.b
        else:  # self.c == 'X':
            self.c = int(self.a) + int(self.b)
            return self.c
    
    
    def subtraction(self):
        """
        Function finds unknown number from subtraction
        """
        if self.a == 'X':
            self.a = int(self.b) + int(self.c)
            return self.a
        elif self.b == 'X':
            self.b = int(self.a) - int(self.c)
            return self.b
        else:  # self.c == 'X':
            self.c = int(self.a) - int(self.b)
            return self.c

        
    def multiplication(self):
        """
        Function finds unknown number from multiplication
        """
        if self.a == 'X':
            self.a = int(self.c) / int(self.b)
            
            if int(self.c) % int(self.b) == 0:
                self.a = int(self.a)
            else:
                self.a = float(self.a)
            return self.a

        elif self.b == 'X':
            self.b = int(self.c) / int(self.a)

            if int(self.c) % int(self.a) == 0:
                self.b = int(self.b)
            else:
                self.b = float(self.b)
            return self.b
        
        else:  # self.c == 'X':
            self.c = int(self.a) * int(self.b)
            return self.c
        

    def division(self):
        """
        Function finds unknown number from division
        """
        if self.a == 'X':
            self.a = int(self.b) * int(self.c)
            return self.a
        
        elif self.b == 'X':
            self.b = int(self.a) / int(self.c)

            if int(self.a) % int(self.c) == 0:
                self.b = int(self.b)
            else:
                self.b = float(self.b)
            return self.b

        else:  # self.c == 'X':
            self.c = int(self.a) / int(self.b)

            if int(self.a) % int(self.b) == 0:
                self.c = int(self.c)
            else:
                self.c = float(self.c)
            return self.c
    
    
x, y, sign, z = [input() for _ in range(4)]
my_calculator = Calculator(x, y, sign, z)

match sign:
    case '+':
        result = my_calculator.addition()
    case '-':
        result = my_calculator.subtraction()
    case '*':
        result = my_calculator.multiplication()
    case '/':
        result = my_calculator.division()
        
print(f'{result} значение X')
