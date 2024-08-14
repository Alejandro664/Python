import pandas as pd
import os

class persona:
    nombrePersona = "A Z"



def primero_mostrar():
    # Este sirve para limpiar la terminal
    os.system("clear")

    # Breve explicación de lo que se hace
    print("""
        Esta es una breve aplicación sobre la practica con python.

        En esta aplicaremos muchas cosas para una practica.

        Dale enter para continuar.
        """)

    # Para que muestre el texto de arriva sin que se borre, al darle enter se borra
    input()

    # Este sirve para limpiar la terminal
    os.system("clear")

    # Pedir los datos personales simulando una creación de cuenta.  el "\n" es para hacer un espacio.
    print("Vamos a perdir datos personales para saberlos: \n")


    # "input" es para pedir un dato. si este esta solo el tipo de dato es "str" o cadena de texto.
    # "lower" es para ponerlo todo en minusculas
    # "title" es para poner cada primera letra en mayuscula
    nombre = input("Dame tu nombre completo: \n").lower().title()
    persona.nombrePersona = nombre
            
    print()
            
    # "int" transforma el "input" en entero
    edad = int(input("ingresa tu edad: \n"))
            
    # Creamos un condicinal para saber si su edad exixte, es menor o mayor de edad
    if edad<0:
        i_edad = "Edad no existe" 
    elif edad>=0 and edad<=17:
        i_edad = "Menor de edad"
    elif edad>=18 and edad<=120:
        i_edad = "Mayor de edad"
    else:
        i_edad = "    Error    "
            
    print()
            
    # Pedimos la identificación
    id = input("Dame tu numero de identificación: \n")

    print()

    password = input("Dame una contraseña pero que no se te olvide: \n")
            
    print()
            
    # mostramos la tabla
    data = {
        'Nombre': [nombre],
        'Edad': [edad],
        'IDENTIFICACIÓN': [id],
        'TIPO' : [i_edad],
        'Contraseña' : [password]
    }
    print(pd.DataFrame(data))
            
    # decimos si los datos estan bien o si estan mal para corregirlos
    mirar_datos = input("""
                                
    ¿Los datos ingresados estan bien?
            
    Si estan mal coloca la letra "M" y dale enter, pero si estan bien dale enter o la letra "S"
            
    Respuesta: \n""").upper()
            
    # Ponemos un condicional para mirar la respuesta
    if mirar_datos=="" or mirar_datos=="S" or mirar_datos=="s":
        os.system("clear")
    else:
        # bucle infinito para colocar los datos hasta estar bien
        while True:
            os.system("clear")
                    
            nombre = input("Dame tu nombre completo: \n").lower().title()
            
            print()
                    
            edad = int(input("ingresa tu edad: \n"))
                    
            if edad<0:
                i_edad = "Edad no existe" 
            elif edad<=17:
                i_edad = "Menor de edad"
            elif edad>=18:
                i_edad = "Mayor de edad"
            else:
                i_edad = "    Error    "
                    
            print()
                    
            id = input("Dame tu numero de identificación: \n")
                    
            print()
                    
            data = {
                'Nombre': [nombre],
                'Edad': [edad],
                'IDENTIFICACIÓN': [id],
                'TIPO' : [i_edad]
            }
            print(pd.DataFrame(data))
                    
            mirar_datos = input("""
                                        
            ¿Los datos ingresados estan bien?
                    
            Si estan mal coloca la letra "M" y dale enter, pero si estan bien dale enter o la letra "S"
                    
            Respuesta: \n""").upper()
                    
            # este detiene el ciclo
            if mirar_datos=="" or mirar_datos=="S":
                os.system("clear")
                # "break" sirve para detener la ejecucion
                break
    return persona.nombrePersona