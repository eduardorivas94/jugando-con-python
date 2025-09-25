print("bienvenid@ a mi conversor de unidades")
print("1.celsius a farenheit")
print("2.farenheit a celsius")
print("3.metros a centimetros")
print("4.centimetros a metros")
print("5.kilogramos a gramos")
print("6.gramos a kilogramos")
print("7.salir")
opciones= input ("opciones (1-7)")
if opciones==("1"):
    Centigrados = int (input ("centigrados(C)"))
    Conversion_Cel_Far = Centigrados*1.8+32 
    print(f"el resultado de convertir {Centigrados} grados centigrados a farenheit es {Conversion_Cel_Far}")
elif opciones==("2"):
    Farenheit = int (input ("farenheit(f)"))
    Conversion_Far_Cel= Farenheit-32/1.8
    print(f"el resultado de convertir {Farenheit} grados farenheit a celsius es {Conversion_Far_Cel} grados celsius")
elif opciones==("3"):
    Metros= int (input ("metros(m)"))
    Conv_Me_Ce= Metros*100
    print(f"la conversion de {Metros} metros a centimetros es {Conv_Me_Ce} cm ")
elif opciones==("4"):
    Centimetros= int (input ("centimetros(cm)"))
    Conv_Ce_Me= Centimetros/100
    print (f"la conversion de {Centimetros} centimetros a metros es {Conv_Ce_Me} metros")
elif opciones==("5"):
    kilometros= int (input ("kilometros(km)"))
    Kil_Gra= kilometros*1000
    print(f"la conversion de {kilometros} km a gramos es {Kil_Gra} gramos ")
elif opciones== ("6"):
    gramos= int(input ("gramos(g)"))
    Gra_Kil=gramos/1000
    print(f"la conversion de {gramos} a kilogramos es {Gra_Kil} kilogramos ")
elif opciones==("7"):
    print("bye gracias por probar mi programa")