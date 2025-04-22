# Contador Binario:
# Escriban un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria.
# Extensión: Utilicen un retardo (por ejemplo, con time.sleep) para simular el conteo de un circuito.

import time

def convertir_a_binario(numero): 
    '''
    esta funcion convierte un numero que le demos en su equivalente binario
    '''
    if numero == 0:
        return '0'
    binario = '' #cadena vacia que arma el numero binario
    while numero > 0:
        binario = str(numero % 2) + binario #convertimos a texto el bit obtenido del resto ("numero" % 2) y se lo agregamos al principio del string "binario"
        numero //= 2 #aca vamos reduciendo "numero" hasta llegar a 0
    return binario

def contador(tiempo, digitos = 4, retardo = 1):
    '''
    funcion que imprime numeros desde 0 hasta (tiempo - 1) y su equivalente binario
    tres parametros:    tiempo o hasta donde cuenta -1
                        digitos que se mostraran en pantalla
                        retardo que simularian ser los segundos de intervalo entre cada print
    '''
    if tiempo <= 0:
        print('El valor de tiempo debe ser positivo')
        return
    for i in range (tiempo):
        binario = convertir_a_binario(i).zfill(digitos) #zfill es lo que hace que se muestren en pantalla "x" digitos fijos
        print(f'{i} = {binario} en binario') 
        time.sleep(retardo)

contador(16, 4, 1)

################################################################

'''
Integrantes:
            Kevin Gastaldello
            Franco Joel Ghilardi Armijo
'''