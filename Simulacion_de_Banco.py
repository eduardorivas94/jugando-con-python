print("°°°°°°°°BIENVENIDO A BANCO PLATA°°°°°°°°")
print("seleccione una de nuestras opciones")
print("1. depositar efectivo")
print("2. consultar saldo")
print("3. retiro sin tarjeta")
print("4. salir")
opciones = input ("opciones (1-4): ")

if opciones == ("1"):
    num_Cuenta= 6
    saldo_En_Cuenta= 1000
    texto_Usuario= ""
    texto_Usuario1= ""
    texto_Usuario=input(f" porfavor ingrese un numero de cuenta no menor ni mayor a {num_Cuenta} ")
    if len (texto_Usuario)< num_Cuenta:
        print(f"el numero de cuenta no puede ser menor a {num_Cuenta} digitos. ")
    elif len (texto_Usuario)> num_Cuenta:
        print(f"el numero de cuenta no puede ser mayor a {num_Cuenta} digitos. ")
    elif len (texto_Usuario) == num_Cuenta:
     monto= float(input("ingresa el monto a depositar: "))
     if monto > 0:
        saldo_En_Cuenta+= monto
    print(f"se depositaron ${monto}. tu nuevo saldo es: ${saldo_En_Cuenta}")
    print("gracias por usar banco plata que tenga buen dia ")
    
elif opciones == ("2"):
    num_Cuenta= 6
    saldo_En_Cuenta= 1000
    texto_Usuario= ""
    texto_Usuario1= ""
    print (f"tu saldo es de ${saldo_En_Cuenta}")
    print("gracias por usar banco plata que tenga buen dia ")
    
elif opciones == ("3"):
    num_Cuenta= 6
    saldo_En_Cuenta= 1000
    texto_Usuario= ""
    texto_Usuario1= ""
    monto= float(input("ingresa el monto a retirar: "))
    if monto>1000:
        print("saldo insuficiente")
    elif monto > 0:
        saldo_En_Cuenta-= monto
        print(f"se retiraron ${monto}. tu nuevo saldo es: ${saldo_En_Cuenta}")
        print("gracias por usar banco plata que tenga buen dia ")
        
    
elif opciones== ("4"):
    print("gracias por usar banco plata que tenga buen dia ")
    
   
     
            
          
            
            

