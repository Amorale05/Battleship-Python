"""BATTLESHIP PROYECTO"""
#Por: Adrián M. y Juan H.
import random

tablero = [[' ','a','b','c','d','e','f','g'],[1,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0],[3,0,0,0,0,0,0,0],[4,0,0,0,0,0,0,0],[5,0,0,0,0,0,0,0],[6,0,0,0,0,0,0,0],[7,0,0,0,0,0,0,0]]
mi_tablero = [[' ','a','b','c','d','e','f','g'],[1,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0],[3,0,0,0,0,0,0,0],[4,0,0,0,0,0,0,0],[5,0,0,0,0,0,0,0],[6,0,0,0,0,0,0,0],[7,0,0,0,0,0,0,0]]

def facil():
    print('ELIGE UNA CASILLA')
    barco1x = random.randint(1,7)
    barco1y = random.randint(1,7)
    intentos = 0
    puntaje = 100 + (100/49)
    #print(str(barco1x) + str(barco1y))
    while tablero[barco1y][barco1x] == 0:
        for renglon in tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()

        columna = (ord(input('Columna (a-g) = '))-96)
        fila = int(input('Fila (1-7) = '))
        while columna > 7 or columna < 1 or fila > 7 or fila < 1:
            print('Por favor elija una casilla dentro del tablero.')
            columna = (ord(input('Columna (a-g) = '))-96)
            fila = int(input('Fila (1-7) = '))

        tablero[fila][columna] = '-'
        intentos += 1
        puntaje -= (100/49)
        print('Intentos: ' + str(intentos))
        print('')
    tablero[fila][columna] = 'X'
    for renglon in tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()
    print('GANASTE')
    print('Intentos: ' + str(intentos))
    print('Puntaje: ' + str(puntaje))
    
def medio():
    print('ELIGE UNA CASILLA')
    barco1x = random.randint(1,7)
    barco1y = random.randint(1,7)
    barco2x = random.randint(1,7)
    barco2y = random.randint(1,7)
    barco3x = random.randint(1,7)
    barco3y = random.randint(1,7)
    hundidos = 0
    intentos = 0
    puntaje = 100 + (100/49)
    #print(str(barco1x) + str(barco1y))
    #print(str(barco2x) + str(barco2y))
    #print(str(barco3x) + str(barco3y))
    while hundidos < 3:
        for renglon in tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()
        print('Barcos hundidos: ' + str(hundidos) + '/3')

        columna = (ord(input('Columna (a-g) = '))-96)
        fila = int(input('Fila (1-7) = '))
        while columna > 7 or columna < 1 or fila > 7 or fila < 1:
            print('Por favor elija una casilla dentro del tablero.')
            columna = (ord(input('Columna (a-g)= '))-96)
            fila = int(input('Fila (1-7)= '))    
        if columna == barco1x and fila == barco1y:
            tablero[fila][columna] = 'X'
            hundidos += 1
        elif columna == barco2x and fila == barco2y:
            tablero[fila][columna] = 'X'
            hundidos += 1
        elif columna == barco3x and fila == barco3y:
            tablero[fila][columna] = 'X'
            hundidos += 1
        else:
            tablero[fila][columna] = '-'
        intentos += 1
        puntaje -= (100/49)
        print('Intentos: ' + str(intentos))
        print('')
            
    for renglon in tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()
    print('Barcos hundidos: ' + str(hundidos) + '/3')
    print('GANASTE')
    print('Intentos: ' + str(intentos))
    print('Puntaje: ' + str(puntaje))

def dificil():
    print('COLOCA TU BARCO')
    for renglon in mi_tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()
    mi_columna = (ord(input('Columna (a-g) = '))-96)
    mi_fila = int(input('Fila (1-7) = '))
    while mi_columna > 7 or mi_columna < 1 or mi_fila > 7 or mi_fila < 1:
            print('Por favor elija una casilla dentro del tablero.')
            mi_columna = (ord(input('Columna (a-g) = '))-96)
            mi_fila = int(input('Fila (1-7) = '))
    mi_tablero[mi_fila][mi_columna] = 'V'
    print('TU TABLERO')
    for renglon in mi_tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()
    print(" ")
    print('ELIGE UNA CASILLA')

    barco1x = random.randint(1,7)
    barco1y = random.randint(1,7)
    #print(str(barco1x) + str(barco1y))
    intentos = 0
    puntaje = 100 + (100/49)
    while (tablero[barco1y][barco1x] == 0) and (mi_tablero[mi_fila][mi_columna] == 'V'):
        print('TABLERO ENEMIGO')
        for renglon in tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()

        columna = (ord(input('Columna (a-g) = '))-96)
        fila = int(input('Fila (1-7) = '))
        while columna > 7 or columna < 1 or fila > 7 or fila < 1:
            print('Por favor elija una casilla dentro del tablero.')
            columna = (ord(input('Columna (a-g) = '))-96)
            fila = int(input('Fila (1-7) = '))

        tablero[fila][columna] = '-'
        pcx = random.randint(1,7)
        pcy = random.randint(1,7)
        while mi_tablero[pcy][pcx] == '-':
            pcx = random.randint(1,7)
            pcy = random.randint(1,7)
        mi_tablero[pcy][pcx] = '-'
        intentos += 1
        puntaje -= (100/49)
        print('Intentos: ' + str(intentos))
        print('TU TABLERO')
        print('Tiro de la computadora: ' + chr(pcx + 96) + str(pcy))
        for renglon in mi_tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()
        print("")
    if barco1y == fila and barco1x == columna:
        tablero[fila][columna] = 'X'
        for renglon in tablero:
            for valor in renglon:
                print(valor, end=" ")
            print()
        print('GANASTE')
        print('Intentos: ' + str(intentos))
        print('Puntaje: ' + str(puntaje))
    elif mi_tablero[pcy][pcx] != 'V':
        print('PERDISTE')

        
def juego():
    logo = open("logo_battleship.txt")
    print(logo.read())
    logo.close()
    modo = 0
    print('Elige tu modo de juego:')
    print('Fácil (1 Barco) = 1')
    print('Medio (3 Barcos) = 2')
    print('Difícil (Tu Vs. PC) = 3')

    modo = int(input())
    if modo == 1:
        print("")
        facil()
    if modo == 2:
        print("")
        medio()
    if modo == 3:
        print("")
        dificil()
    
juego()
