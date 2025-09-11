Algoritmo Numeros_Amigos
	definir n1, n2, cont, sum1, sum2, q, divisor  Como Entero
	escribir " bienvenido a mi programita de los numeros que son amigos "
	escribir" 2 numeros porfavor "
	leer n1, n2
	//inicialisamos la suma
	sum1 <- 0
	sum2 <- 0
	para q=1 hasta n1/2 con paso 1 hacer
		divisor = num1 % q
		si divisor = 0 entonces
			sum1 = sum1 + q
		FinSi
	FinPara
	para q = 1 hasta n2/2 con paso 1 Hacer
		divisor = n2 % q
		si divisor = 0 Entonces
			sum2 = sum2 + q
		FinSi
	FinPara
	// verificamos si son numeros amigos
	si sum1 = n2 y sum2 = n1 Entonces
		escribir " los numeros ", num1, " y ", n2, " son numeros amigos "
	SiNo
		escribir " los numeros ", n1, " y ", n2, " no son numeros amigos "
	FinSi
FinAlgoritmo
