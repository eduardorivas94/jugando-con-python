Algoritmo Factorial_De_Un_Numero_Usando_Para
	// el factorial se obtiene multiplicando una cantidad por todas las cantidades anteriores a el ejemplo : 5=120 y se saca 5*4+3+2+1
	definir dig1 como entero
	 escribir "hola usuario, ingrese porfavor un digito"
	leer dig1
	factorial <- 1
	para q <- 1 hasta dig1 con paso 1 hacer factorial <- factorial * q 
		// definimos que nuestra variable numerica va desde 1 hasta el numero que ingrese el usuario y que este mismo se vaya multiplicando por todos los anteriores hasta regresar a 1 y asi obtenemos nuestro resultado
	FinPara
	escribir " el factorial de " ConvertirATexto(dig1) " es " ConvertirATexto(factorial)
FinAlgoritmo
