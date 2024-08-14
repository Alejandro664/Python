def Calculadora_promedio():
    import os
    os.system("clear")
    print("""
    Esta es una calculadora donde nada mas tienes que poner la operacion completa,
    pero esta soluciona solo operaciones simples, ejemplo:

    123+587/9658-547896

    Este seria el maximo de operaciones que serian 3, la cantidad de numero si 
    puede ser cualquiera.

    Ahora copia la operacion:
    """)

    dato_operacion = input()
    numeros_totales = len(dato_operacion)

    contadorr=0
    for i in dato_operacion:
        if i == "+" or i=="-" or i=="*" or i=="/":
            contadorr +=1
            
    print()

    if contadorr == 1:
        cambiar_ope = dato_operacion.replace("-", "+").replace("*", "+").replace("/", "+")
        resultado_operacion = cambiar_ope.split("+")
        
        resultado_operacion[0] = int(resultado_operacion[0])
        resultado_operacion[1] = int(resultado_operacion[1])

        for g in dato_operacion:
            if g=="+":
                mostrar = resultado_operacion[0] + resultado_operacion[1]
            elif g=="-":
                mostrar = resultado_operacion[0] - resultado_operacion[1]
            elif g=="*":
                mostrar = resultado_operacion[0] * resultado_operacion[1]
            elif g=="/":
                mostrar = resultado_operacion[0] / resultado_operacion[1]
        
        print(f"""El resultado es: {mostrar}
        """)
    elif contadorr == 2:
        cambiar_ope = dato_operacion.replace("-", "+").replace("*", "+").replace("/", "+")
        resultado_operacion = cambiar_ope.split("+")
        
        resultado_operacion[0] = int(resultado_operacion[0])
        resultado_operacion[1] = int(resultado_operacion[1])
        resultado_operacion[2] = int(resultado_operacion[2])
        
        
        sgnomas = dato_operacion.find("+")
        sgnomenos = dato_operacion.find("-")
        sgnodivi = dato_operacion.find("/")
        sgnomulti = dato_operacion.find("*")
        
        if sgnomas==-1:
            sgnomas=100000
        if sgnomenos==-1:
            sgnomenos=100000
        if sgnodivi==-1:
            sgnodivi=100000
        if sgnomulti==-1:
            sgnomulti=100000
        
        if sgnomas<sgnomenos and sgnomas<sgnodivi and sgnomas<sgnomulti:
            for k in dato_operacion:
                if k=="-":
                    mostrar = resultado_operacion[0] + resultado_operacion[1] - resultado_operacion[2]
                elif k=="/":
                    mostrar = resultado_operacion[0] + resultado_operacion[1] / resultado_operacion[2]
                elif k=="*":
                    mostrar = resultado_operacion[0] + resultado_operacion[1] * resultado_operacion[2]
                elif k=="+":
                    mostrar = resultado_operacion[0] + resultado_operacion[1] + resultado_operacion[2]
        
        if sgnomenos<sgnomas and sgnomenos<sgnodivi and sgnomenos<sgnomulti:
            for k in dato_operacion:
                if k=="+":
                    mostrar = resultado_operacion[0] - resultado_operacion[1] + resultado_operacion[2]
                elif k=="/":
                    mostrar = resultado_operacion[0] - resultado_operacion[1] / resultado_operacion[2]
                elif k=="*":
                    mostrar = resultado_operacion[0] - resultado_operacion[1] * resultado_operacion[2]
                elif k=="-":
                    mostrar = resultado_operacion[0] - resultado_operacion[1] - resultado_operacion[2]
                    
        if sgnodivi<sgnomas and sgnodivi<sgnomenos and sgnodivi<sgnomulti:
            for k in dato_operacion:
                if k=="+":
                    mostrar = resultado_operacion[0] / resultado_operacion[1] + resultado_operacion[2]
                elif k=="-":
                    mostrar = resultado_operacion[0] / resultado_operacion[1] - resultado_operacion[2]
                elif k=="*":
                    mostrar = resultado_operacion[0] / resultado_operacion[1] * resultado_operacion[2]
                elif k=="/":
                    mostrar = resultado_operacion[0] / resultado_operacion[1] / resultado_operacion[2]

        if sgnomulti<sgnomas and sgnomulti<sgnomenos and sgnomulti<sgnodivi:
            for k in dato_operacion:
                if k=="+":
                    mostrar = resultado_operacion[0] * resultado_operacion[1] + resultado_operacion[2]
                elif k=="-":
                    mostrar = resultado_operacion[0] * resultado_operacion[1] - resultado_operacion[2]
                elif k=="/":
                    mostrar = resultado_operacion[0] * resultado_operacion[1] / resultado_operacion[2]
                elif k=="*":
                    mostrar = resultado_operacion[0] * resultado_operacion[1] * resultado_operacion[2]
        
        print(f"""El resultado es: {mostrar}
        """)
        print()
    input("Dale enter....")
    os.system("clear")