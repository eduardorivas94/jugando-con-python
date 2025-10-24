import random
palabras = [
    "cerveza",
    "videojuego",
    "hamburguesa",
    "infante",
    "horror",
    "pantalon",
    "celular",
    "cobija",
    "teclado",
    "television",
    "zapato"
]
palabra_azar = random.choice(palabras)
vidas=3
aciertos=[]
palabra_pantalla = ["_"] * len(palabra_azar)

print ("bienvenido a mi juego del ahorcado")
print("la palabra es:", "".join(palabra_pantalla))

while vidas > 0:
    print("\nvidas restantes: ", vidas)
    print("palabra: ", "".join(palabra_pantalla))

    letra_ingresada= input("ingresa una letra: ").lower()
    if len (letra_ingresada) !=1 or not letra_ingresada.isalpha():
        print("porfavor ingresa una letra")
        continue

    if letra_ingresada in aciertos:
        print("aa perrillo le atinaste pon otra")
        continue
    aciertos.append(letra_ingresada)
    if letra_ingresada in palabra_azar:
        print ("la letra esta en la palabra")
        for i in range(len(palabra_azar)):
            if palabra_azar[i]== letra_ingresada:
                palabra_pantalla[i]= letra_ingresada
    else:
        vidas -= 1
        print("tonto esa no es, tenga cocazo")
    if "_" not in palabra_pantalla:
        print("felicidades! le atinaste a la palabra ", palabra_azar)
        break
    if vidas == 0:
        print ("perdiste nimodo mi chavo")
        print("la palabra secreta era: ", palabra_azar)

