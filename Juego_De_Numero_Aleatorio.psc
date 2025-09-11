
Algoritmo Juego_De_Numero_Aleatorio
	definir numal, numus, int Como Entero
	definir max, min Como Entero
	// asiganmos valores maximos y minimos o damos un rango limite a nuestro programa 
	min <- 1
	max <- 100
	int <- 0
	numal <- azar (max - min + 1) + min
	escribir "bienvenido a mi juego de azar"
	escribir "adivina el numero secreto del 1 al 100"
	repetir
	leer numus	
	int <- int +1//con esto agregamos un contador para que el usuario sepa cuantos intentos le tomo
	si numus < numal Entonces// aqui condicioanamos que lance el mensaje de es mayor o menor como pista al usuario del numero al azar
		escribir "el numero secreto es mayor"
	sino
		si numus > numal Entonces
			
			escribir" el numero secreto es menor"
			
		FinSi
	FinSi
Hasta Que numus=numal // esta funcion al usar el repetir de mas arriba es como por asi decirlo una funcion constante que se repetira hasta que el numer que ingrese el usuario sea igualal aleatorio del programa
escribir "acerto el numero bravoooooo!!", numal
escribir " lo hiciste en ", int, " intentos " 
FinAlgoritmo
