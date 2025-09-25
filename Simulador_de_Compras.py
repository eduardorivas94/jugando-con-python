print("°°°°°°°SIMULADOR DE COMPRA DE PLAYSTATION EN LINEA°°°°°°°")
print("seleccione el articulo que desea comprar")
print("1.sony playstation 4")
seleccion = (input ("seleccion: "))
if seleccion == ("1"):
    print("°°°°°°°carrito de compras°°°°°°°")
    Lista_de_Compras=int (input ("cuantos productos vas a ingresar?:") )
    Lista_Productos=[]
    print("seleccione una salida de pago")
    print("1. calcular el precio unitario dado un precio y cantidad")
    print("2.calcular total con iva")
    opcion= input ("opcion (1-2)")
    for i in range (Lista_de_Compras):

        print(f"ingresando productos # {i+1}")
        Precio_de_Productos=float(input(f"precio: "))
if opcion==("1"):
    Precio_Total= (Lista_de_Compras*Precio_de_Productos)
    print(f"tu total es de {Precio_Total}")
    print("gracias vuelva pronto")
elif opcion==("2"):
    print("desea agregar un cupon de descuento? ") 
decision= input ("")
if decision==("si"):
    descuento=0.0
     
    codigo=input("")
    if codigo == "verano":
        descuento=0.10
    elif codigo=="saldos":
        descuento=0.35
    elif codigo=="bbva":
        descuento=0.5
    elif codigo=="banorte25":
        descuento=0.25
           
    iva=float(input(f"iva: "))
    Precio_Total=(Lista_de_Compras*Precio_de_Productos*1+iva-descuento)
    print(f"tu total es de {Precio_Total:.2f}")
elif decision==("no"): 
        iva=float(input(f"iva: "))
        Precio_Total=float (Lista_de_Compras*Precio_de_Productos)*1+iva
        print(f"tu total es de {Precio_Total}")
        print("muchas gracias regrese pronto")




    


