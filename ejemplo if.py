persona = {
    "nombre": {},
    "edad": {},
    "ciudad": {},
}

if "edad" in persona and persona ["edad"] >=18:
    print(f"{persona['nombre']} es mayor de edad. ")
else:
    print(f"{persona['nombre']}no es mayor de edad. ")

    if persona["ciudad"]== "madrid":
        print(f"{persona['nombre']}vive en valparaiso")
    else:
        print(f"{persona['nombre']} no vive en valparaiso")