Algoritmo Ejercicio_04letra
	Escribir  'Indique monto total de compras'
	Leer MT
	Si MT > 3000 Entonces
	D = MT * 0.1
	SiNo
	D = MT * 0.05
	Fin Si
	PF = MT - D
	Escribir 'El descuento es:', D
	Escribir 'El precio final es:', PF
FinAlgoritmo
