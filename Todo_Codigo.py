# Este sirve para interatuar con la terminal
import os
# Para mostrar la barra de carga
import time


# <-------------------------------->


from prim_most import primero_mostrar
from programa_barra import progress_bar



# 1...........
primero_mostrar()


#--------------------

n = 50

for i in range (n + 1):
    time. sleep (0.1)
    print (progress_bar(i,n,20), end='\r')
    
os.system("clear")
        
#-----------------------

from Menu import menu_opcion
menu_opcion()