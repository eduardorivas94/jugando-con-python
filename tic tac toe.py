import random
tablero= ['1', '2', '3', '4', '5', '6', '7', '8', '9']
Para_Ganar=[
    (0, 1, 2), (3, 4, 5), (6, 7, 8)
    (7, 5, 2), (1, 8, 3), (6, 4, 0)
    (0, 7, 2), (2, 6, 1)
   ]
player1= 'X'
game_Over= False
game_Mode=''
print("bienvenido a tic tac toe")
print("elige un modo")
game_Mode= input ("jugador vs jugador\n2. jugador vs CPU\nIngresa 1 o 2:")
while not game_Over:
    print("\n")
    print(f"{tablero [0]} | {tablero[1]} | {tablero[2]}")
    print("_______")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("_______")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")
    print("\n")
    if game_Mode == '2' and player1 == 'O':
        posicion = random.randint (1, 9)
        while tablero[posicion - 1] in ('X', 'O'):
            posicion = random.randit(1, 9)
        print(f"la cpu juega en la posicion {posicion}")
    else:
        try:
            posicion_str= input(f"jugador {player1}, elige una posicion (1-9):")
            posicion = int(posicion_str)
        except ValueError:
            print("entrada no valida")
            continue
        if not (1 <= posicion <= 9) or tablero[posicion -1] in ('X', 'O'):
            print("posicion invalida")
            continue
        tablero[posicion - 1] = player1
        gano= False
        for comb in Para_Ganar:
            if tablero[comb[0]] == tablero [comb[1]] == tablero[comb[2]]:
                print("\n")
                print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
                print("__________")
                print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
                print("__________")
                print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")
                print("\n")
                print(f"felicidades {player1} has ganado")
                gano=True
                game_Over=True
                break
        if gano:
            break
        if all (x in ('X', 'O') for x in tablero):
            print("\n")
            print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
            print("__________")
            print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
            print("__________")
            print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")
            print("\n")
            print(f"es un empate")
            game_Over =True
            break
    if player1=='X':
        player1='O'
    else:
        player1='X'
        print("gracias por jugar")


           


