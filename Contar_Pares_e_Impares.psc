Algoritmo Contar_Pares_e_Impares
	definir n1, q, pares, impares Como Entero
	pares <- 0
	impares <- 0
	escribir " deifna numero limite "
	leer n1
	para q <- 1 hasta n1 con paso 1 Hacer
		si q % 2 = 0 entonces 
			pares <- pares + 1
		SiNo
			impares <- impares + 1
		FinSi
	FinPara
	Escribir " cantidad de numeros pares: ", pares
	escribir " cantidad de numeros impares: ", impares
	
	
FinAlgoritmo
