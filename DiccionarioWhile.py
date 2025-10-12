DiccionarioWhile= {
    "color": "naranja",
    "animal": "perro",
    "genero": "masculino"
}
while True:
    clave = input("introduce una clave para buscar en el diccionario(o escribe salir para terminar)")
        
    if clave.lower() == 'salir':
        print ("¡adios!")
        break 
    
    if clave in DiccionarioWhile:
        print(f"el valor para la clave es '{clave}' es {DiccionarioWhile[clave]}")
    else:
        print(f"la clave '{clave}no se encuentra en el diccionario")


