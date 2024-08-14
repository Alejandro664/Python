def Calculadora_Basica():
    import os
    os.system("clear")
    a = int(input("Dame el primer numero: "))
    print()
    b = input("Dame la operacion matematica: ")
    print()
    z = int(input("Dame el segundo numero: "))
    print()
    
    if b == "+":
        res = a+z
    elif b == "-":
        res = a-z
    elif b == "*":
        res = a*z
    elif b == "/":
        res = a/z
    
    print(f"El resultado es: {res}")
    print()
    input("Dale enter....")
    os.system("clear")