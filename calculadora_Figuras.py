#from math import * #Nos importamos toda la librería
#from math import sqrt, pi #aquí importamos la función de raíz cuadrada y el valor de pi
from math import pi #importamos solo el valor de la constate pi

print("---- Bienvenida a mi Calculadora de Figuras ---")
print("-°-°-°- Menú de figuras -°-°-°-")
print("1. Cubo")
print("2. Prisma")
print("3. Pirámide")
print("4. Cilindro")
print("5. Cono")
print("6. Esfera")

figura = input("Figura (1-6): ")

print("-°-°-°- Menú de opciones -°-°-°-")
print("1. Calcular el área")
print("2. Calcular el volumen")
print("3. Calcular ambos")


opcion = input("Opción (1-3): ")

if figura == "1": #Este if controla qué quiere el usuario calcular.
    if opcion == "1": #Este if aninado controla la figura para calcular el área.
        lado = float(input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2f}")
elif figura == "2":
    if opcion == "1": 
        largo = float(input ("largo (cm)"))
        ancho = float(input ("ancho(cm)"))
        altura = float(input ("altura (cm)"))
        areaPrisma = 2*(largo*ancho+ancho*altura+largo*altura)
        print(f"El área del prisma es: {areaPrisma:.2f}")
elif figura == "3":
    if opcion == "1":
         Base=float(input("base (b)"))
         Altura_Base=float(input("altura base(ab)"))
         AreaBase=Base*Altura_Base
         Peri_Base=float(input("perimetro base(pb)"))
         Altu_Incli=float(input("altura inclinada (ai)"))
         Area_Lateral=Peri_Base*Altu_Incli
         Area_Total=AreaBase + Area_Lateral
         print(f"el area total de la piramide es: {Area_Total:.2f}")
elif figura == "4":
     if opcion == "1":
          pi=3.14159
          radio=float(input("radio(r)"))
          altura=float(input("altura(a)"))
          Area_Cilindro=2*pi*radio*(radio+altura)
          print(f"el area de el cilindro es de: {Area_Cilindro:.3f}")
elif figura == "5":
     if opcion == "1":
          pi=3.14159
          radio=float(input("radio (r)"))
          generatriz=float(input("generatriz(g)"))
          A_Base=pi*radio**2
          A_Lateral=pi*radio*generatriz
          A_Total=A_Base+A_Lateral
          print(f"el area de un cono es: {A_Total:.3f}")
elif figura == ("6"):
     if opcion == ("1"):
          radio=float(input("radio(r)"))
          pi=3.14159
          Area_Esfera=4*pi*(radio**2)
          print(f"el area de una esfera es: {Area_Esfera:.2f} ")
if figura == "1":
    if opcion == "2": #Este if aninado controla la figura para calcular el volumen.
        lado = float(input("Lado (cm):"))
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.4f}")
elif figura == "2":
    if opcion == "2":
        largo = float(input("largo (cm):"))
        ancho = float(input("ancho (cm):"))
        altura = float(input("altura (cm):"))
        volumenPrisma= largo*ancho*altura
        print(f"el volumen del prisma es: {volumenPrisma:.4f}")
elif figura == "3":
    if opcion == "2":
        A_Base=float(input("area base(ab)"))
        altura=float(input("altura(a)"))
        Vol_Pir=(A_Base*altura)/3
        print(f"el volumen de la piramide es {Vol_Pir:.3f}")
elif figura == "4":
    if opcion=="2":
        pi=3.14159
        altura=float(input("altura(a)"))
        radio=float(input("radio(r)"))
        V_Cil=pi*radio**2*altura
        print(f"el volumen de un cilindro es {V_Cil:.3f}")
elif figura == "5":
    if opcion == "2":
        pi=3.14159
        radio=float(input("radio(r)"))
        altura=float(input("altura(a)"))
        V_Con=(1/3)*pi*radio**2*altura
        print(f"el volumen de un cono es{V_Con:.3f}")
elif figura == "6":
    if opcion == "2":
        pi=3.14159
        radio=float(input("radio(r)"))
        V_Esf=(4/3)*pi*radio**3
        print(f"el volumen de la esfera es {V_Esf:.3f}")
if figura == "1":
    if opcion == "3": #Este if aninado controla la figura para calcular ambos.
        lado = float(input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:.2f}")
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.2f}")
elif figura == "2":
    if opcion == "3":
        largo = float(input ("largo (cm)"))
        ancho = float(input ("ancho(cm)"))
        altura = float(input ("altura (cm)"))
        areaPrisma = 2*(largo*ancho+ancho*altura+largo*altura)
        volumenPrisma= largo*ancho*altura
        print(f"El área del prisma es: {areaPrisma:.2f}")
        print(f"el volumen del prisma es: {volumenPrisma:.4f}")
elif figura == "3":
    if opcion == "3":
        Base=float(input("base (b)"))
        Altura_Base=float(input("altura base(ab)"))
        AreaBase=Base*Altura_Base
        Peri_Base=float(input("perimetro base(pb)"))
        Altu_Incli=float(input("altura inclinada (ai)"))
        Area_Lateral=Peri_Base*Altu_Incli
        Area_Total=AreaBase + Area_Lateral
        print(f"el area total de la piramide es: {Area_Total:.2f}")
        A_Base=float(input("area base(ab)"))
        altura=float(input("altura(a)"))
        Vol_Pir=(A_Base*altura)/3
        print(f"el volumen de la piramide es {Vol_Pir:.3f}")
elif figura == "4":
    if opcion == "3":
        pi=3.14159
        radio=float(input("radio(r)"))
        altura=float(input("altura(a)"))
        Area_Cilindro=2*pi*radio*(radio+altura)
        print(f"el area de el cilindro es de: {Area_Cilindro:.3f}")
        pi=3.14159
        altura=float(input("altura(a)"))
        radio=float(input("radio(r)"))
        V_Cil=pi*radio**2*altura
        print(f"el volumen de un cilindro es {V_Cil:.3f}")
        
elif figura == "5":
    if opcion == "3":
        pi=3.14159
        radio=float(input("radio (r)"))
        generatriz=float(input("generatriz(g)"))
        A_Base=pi*radio**2
        A_Lateral=pi*radio*generatriz
        A_Total=A_Base+A_Lateral
        print(f"el area de un cono es: {A_Total:.3f}")
        pi=3.14159
        radio=float(input("radio(r)"))
        altura=float(input("altura(a)"))
        V_Con=(1/3)*pi*radio**2*altura
        print(f"el volumen de un cono es{V_Con:.3f}")
elif figura == "6":
    if opcion == "3":
        radio=float(input("radio(r)"))
        pi=3.14159
        Area_Esfera=4*pi*(radio**2)
        print(f"el area de una esfera es: {Area_Esfera:.2f} ")
        pi=3.14159
        radio=float(input("radio(r)"))
        V_Esf=(4/3)*pi*radio**3
        print(f"el volumen de la esfera es {V_Esf:.3f}")
        
    
       