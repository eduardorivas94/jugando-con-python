print("---- Calculadora de palabras----")
print("Menu de opciones")
print("1. Contar caracteres")
print("2. Pasar a MAYUSCULAS")
print("3. Pasar a minusculas")
print("4. Contar cuantas veces aparece una letra")
print("5. Remplazar una letra por otra")
print("6. Unir cada letra con guiones ")
print("7. Sumar la longitud de dos sentencias")
print("8. salir")

texto = input("ingresa una palabra o sentencia:")
opcion = input("Elige una opcion del menu (1-8):")

if opcion == "1":
    #len=length
    #Identacion, es caracteristica principal de Python
    #Nos indican que estas lineas dependen de la "linea padre"
    #La linea que esta no Indentada anterior
    #Esta linea es un texto por tanto no se ejecuta
    #ConteoCaracteres= len(texto)
    conteoCaracteres = len(texto)
    print("numero de caracteres:  "+str(len(texto)))
    print("Numero de caracteres:", conteoCaracteres)
    print(f"Numero de caracteres: {conteoCaracteres}")
    print(f"numero de caraceteres {len(texto)}")

elif opcion == "2":
    print("ahi esta tu texto en letras grandotas:  "+str.upper(texto))
elif opcion == "3":
    print("ahi esta tu texto en letras minusculas:  "+str.lower(texto))
elif opcion == "4":
    letra= input("que letra quieres cambiar?:  ")
    print(f"la letra {letra} aparece {texto.count(letra)}veces")
elif opcion == "5":
    print("se reemplazara la letra o por z", texto.replace("o","z"))
elif opcion== "6":
    print ("unir las palabras","#".join(texto))
elif opcion == "7":
   texto2= input ("ingresa segunda palabra u oracion")
   print (len (texto+texto2))
else:
    print("Opcion incorrecta,debes elegir una opcion del menu,ADIOS!")