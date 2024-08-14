import random
import os

def j_ppt():
    os.system("clear")
    while True:
        print("""
        Este juego trata sobre piedra, papel o tijera donde tienes que escojer
        uno y la maquina escoje otro y se mira quien gana, aqui te dejo la tabla:
        
        Gana     |    Pierde
        ----------------------
        Piedra   |    Tijera
        Papel    |    Piedra
        Tijera   |    Papel
        
        Dime cual vas a escojer:
        
        """)
        objectPersona = input().lower().title()
        
        numeros = [1, 2, 3]
        
        numero_aleatorio = random.choice(numeros)
        if numero_aleatorio==1:
            objetoMaquina = "Piedra"
        elif numero_aleatorio==2:
            objetoMaquina = "Papel"
        elif numero_aleatorio==3:
            objetoMaquina = "Tijera"
        
        if objectPersona=="Piedra" and objetoMaquina=="Papel":
            print(f"""
            Tú escojiste {objectPersona} y la maquina escojio {objetoMaquina}
            
            PERDISTE!!!!
            
            """)
        elif objectPersona=="Tijera" and objetoMaquina=="Piedra":
            print(f"""
            Tú escojiste {objectPersona} y la maquina escojio {objetoMaquina}
            
            PERDISTE!!!!
            
            """)
        elif objectPersona=="Papel" and objetoMaquina=="Tijera":
            print(f"""
            Tú escojiste {objectPersona} y la maquina escojio {objetoMaquina}
            
            PERDISTE!!!!
            
            """)
        elif objectPersona=="Papel" and objetoMaquina=="Piedra":
            print(f"""
            Tú escojiste {objectPersona} y la maquina escojio {objetoMaquina}
            
            GANASTE!!!!
            
            """)
        elif objectPersona=="Piedra" and objetoMaquina=="Tijera":
            print(f"""
            Tú escojiste {objectPersona} y la maquina escojio {objetoMaquina}
            
            GANASTE!!!!
            
            """)
        elif objectPersona=="Tijera" and objetoMaquina=="Papel":
            print(f"""
            Tú escojiste {objectPersona} y la maquina escojio {objetoMaquina}
            
            GANASTE!!!!
            
            """)
        else:
            print(f"""
            Tú escojiste {objectPersona} y la maquina escojio {objetoMaquina}
            
            EMPATE!!!!
            
            """)
            
        print("Quieres seguir Jugando?\n")
        
        seguir = input().lower().title()
        
        if seguir=="" or seguir=="si" or seguir=="Si" or seguir=="SI":
            os.system("clear")
        else:
            os.system("clear")
            break