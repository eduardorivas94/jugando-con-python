print("°°°°°°°°Base de datos de claificaciones UAZ°°°°°°°°")
print("que deseas obtener")
print("1.promedio general ")
print("2.promedio final con ponderaciones")
opcion=input ("opciones (1-2: ")
if opcion ==("1"):
   
    print(" ingresa tu calificacion de los 3 parciales ")
    Cal_1=float (input ("primer parcial:" ))
    Cal_2=float (input ("segundo parcial:" ))
    Cal_3=float (input("tercer parcial:" ))
    notas=[Cal_1, Cal_2, Cal_3]
    Nota_Baja=min(notas)
    Nota_Alta= max(notas)
    Min_Apro=7
    prom_Fin=(Cal_1+Cal_2+Cal_3)/3
    
    print(f"tu promedio final es {prom_Fin} y tu calificacion mas baja fue {Nota_Baja} y la mas alta {Nota_Alta}")
    if prom_Fin>=Min_Apro:
        print(" !!felicidades aprobaste el semestre eres libre de todo pecado en hora buena¡¡ ")
    else:
        print(" lamentamos informar que no alcancaste el promedio minimo favor de presentarte a ordinario en las fechas solicitadas :,c ")
elif opcion==("2"):
    print(" ingresa tu calificacion de los 3 parciales ")
    Cal_1=float (input ("primer parcial:" ))
    Cal_2=float (input ("segundo parcial:" ))
    Cal_3=float (input("tercer parcial:" ))
    print("ingresa el peso o ponderacion por parcial de tu materia usando decimales por ejemplo (0.10) siendo la maxima 0.100")
    Peso_1=float (input(" ponderacion 1: "))
    Peso_2=float (input("ponderacion 2: "))
    Peso_3=float (input("ponderacion 3: "))
    notas=[Cal_1, Cal_2, Cal_3]
    Nota_Baja=min(notas)
    Nota_Alta= max(notas)
    Min_Apro=7
    Prom_Fin= (Cal_1*Peso_1)+(Cal_2*Peso_2)+(Cal_3*Peso_3)
    print(f"tu promedio final aplicando las ponderaciones es {Prom_Fin} y tu nota mas baja fue {Nota_Baja} y la maxima {Nota_Alta}")