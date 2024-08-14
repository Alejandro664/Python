import os
from prim_most import persona
from primer_nom import primer_nombre
from cal_basic import Calculadora_Basica
from cal_prom import Calculadora_promedio
from juego_ppt import j_ppt
from juego_futbol import Juego_de_futbol


p_n = primer_nombre(persona.nombrePersona)

def menu_opcion():
    while True:
        print(f"""
        Hola {p_n} Gracias por confiar en nosotros.

        {p_n} estas son las opcciones que tienes para acceder a nuestro aplicación:

            1. Calculadora Basica
            2. Calculadora promedio
            3. Juego de piedra, papel y tijera
            4. Juego de futbol
            5. Salir

        Escoje el insiso que desea:
        """)

        resultado_insiso = input()

        if resultado_insiso=="1":
            Calculadora_Basica()
        elif resultado_insiso=="2":
            Calculadora_promedio()
        elif resultado_insiso=="3":
            j_ppt()
        elif resultado_insiso=="4":
            Juego_de_futbol()
        elif resultado_insiso=="5":
            os.system("clear")
            break
        else:
            print()
            print("Vuelve a intertarlo, Dale enter...")
            input()
            os.system("clear")
        