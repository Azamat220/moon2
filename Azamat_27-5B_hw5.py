def mult(*args):
    ans = 1
    for i in args:
        ans *= i
    return ans

def mirror( word = 'hello'):
    return s == s[::-1]

def calculator(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '**':
        return num1 ** num2
    elif (oper == '%' or oper == '/' or oper == '//') and num2 == 0:
        return "CANT DIVIDE TO ZERO"
    elif oper == '%':
        return num1 % num2
    elif oper == '/':
        return num1 / num2
    elif oper == '//':
        return num1 // num2


print(calculator(5, '/', 2))

some_text = 'hello'