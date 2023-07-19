"""
Теперь обратимся к нашему калькулятору для простых уравнений из шага 4.3!
Вы же выполнили все необходимые условия?

Напомним их!

Сделайте так, чтобы ваш калькулятор отрабатывал ситуации, когда  X может стать любая переменная, 
а в спектр воспринимаемых системой знаков входили бы следующие:

+ (плюс)
- (минус)
* (умножить)
/ (разделить, возможен не целочисленный результат)

И как дополнительное задание - ** (возведение в степень) - здесь оно не проверяется
Калькулятор должен принимать только целые числа! А выдавать может и не целые.

Вставьте код вашего калькулятора в поле для ответов начиная от приема значений и заканчивая выводом 
верного ответа.

Обратите внимание:
Если деление целочисленное, то следует отбрасывать дробную часть. В случае деления с остатком, 
дробную часть нужно оставить!!!

Sample Input:
4
X
-
6

Sample Output:
-2 значение X
"""
def calculator(a, b, operator, c):
    '''
    This function makes calculation and return result
    '''
    if operator == '+':  # ---------- addition
        if a == 'X':
            a = int(c) - int(b)
            return f'{a} значение X'
        
        elif b == 'X':
            b = int(c) - int(a)
            return f'{b} значение X'
        
        elif c == 'X':
            c = int(a) + int(b)
            return f'{c} значение X'
     
    elif operator == '-':  # ---------- subtraction
        if a == 'X':
            a = int(b) + int(c)
            return f'{a} значение X'
        
        elif b == 'X':
            b = int(a) - int(c)
            return f'{b} значение X'
        
        elif c == 'X':
            c = int(a) - int(b)
            return f'{c} значение X'
        
    elif operator == '*':  # ---------- multiplication
        if a == 'X':
            a = int(c) / int(b)
            
            if int(c) % int(b) == 0:
                a = int(a)
            else:
                a = float(a)
            return f'{a} значение X'
        
        elif b == 'X':
            b = int(c) / int(a)
            
            if int(c) % int(a) == 0:
                b = int(b)
            else:
                b = float(b)
            return f'{b} значение X'
        
        elif c == 'X':
            c = int(a) * int(b)
            return f'{c} значение X'
        
    elif operator == '/':  # ---------- division
        if a == 'X':
            a = int(b) * int(c)
            return f'{a} значение X'
        
        elif b == 'X':
            b = int(a) / int(c)
            
            if int(a) % int(c) == 0:
                b = int(b)
            else:
                b = float(b)
            return f'{b} значение X'
        
        elif c == 'X':
            c = int(a) / int(b)
            
            if int(a) % int(b) == 0:
                c = int(c)
            else:
                c = float(c)
            return f'{c} значение X'
    
    
a, b, operator, c = [input() for _ in range(4)]
print(calculator(a, b, operator, c))
