"""
1) Realiza un algoritmo que imprima  solamente  su nombre
en la pantalla y seguidamente finalice  la aplicacion
"""

##nombre= "Julio"
##print(nombre)

"""
2) Realice un algoritmo que solicite al usuario que escriba 
su nombre y seguidamente envíe la siguiente frase a la salida 
estándar: "Su nombre es: [nombre del usuario]".

"""

##nombre = input("Digita tu nombre: ")
##print("Su nombre es:"+ str(nombre))

"""
3) Realice un algoritmo que solicite el nombre y la edad del 
usuario., seguidamente, envíe la siguiente frase a la consola: 
"El nombre es <nombre> y su edad es <edad>"
"""

##nombre=input("Nombre: ")
##edad =int(input("Edad: "))

##print("El nombre es %s y su edad es %i" %(nombre,edad))


"""
4) Realice un algoritmo que solicite al usuario informar un número.
Seguidamente, almacene a este número en una variable. Por último,
envíe a ese número a la salida estándar.
"""

##numero = int(input("Digita un numero: "))
##variNum = numero
##print("El valor de la varible es: ",variNum)


"""
5) Realice un algoritmo que solicite al usuario informar un número. 
Seguidamente, escriba el siguiente mensaje  "El número escrito fue: "
"""

##numero = int(input("Digita un numero: "))
##print("El numero escrito fue: ",numero)

"""
6) Realice un algoritmo que solicite al usuario informar 3 números. Seguidamente, sume los 
valores y envíe a la salida estándar la siguiente frase "La suma total es:  ".
"""

#numero1=int(input("Digite primer numero: "))
#numero2=int(input("Digite segundo numero: "))
#numero3=int(input("Digite tercero numero: "))
#suma=numero1+(numero2+numero3)
#print("La suma total es: ",suma)

"""
7) Realice un algoritmo que solicite al usuario informar 2 números. Seguidamente, sume
los valores y envíe a la salida estándar la siguiente frase: "La suma entre <X> e <Y> es
igual a <total>"
"""

##numero1 = int(input("Digita un numero: "))
##numero2 = int(input("Digita un numero: "))
##print("Se digito dos numero: %i y %i " %(numero1,numero2))
##suma= numero1+numero2
##print("La suma entre %i e %i es igual a %i" %(numero1, numero2, suma))


"""
8) Realice un algoritmo que solicite las notas de las 4 pruebas semestrales al usuario. 
Seguidamente, calcule la media y envíe el valor resultante a la salida estándar:

"""
##prueba1= float(input("Digita calificacion 1: "))
##prueba2= float(input("Digita calificacion 2: "))
##prueba3= float(input("Digita calificacion 3: "))
##prueba4= float(input("Digita calificacion 4: "))
#probedio=(prueba1+prueba2+prueba3+prueba4)/4

#print("La calificacion total es: ", probedio)

"""
9) Realice un algoritmo que solicite al usuario que informe una medida en metros.
Seguidamente, convierta a esta medida de metros a centímetros y envíela a la salida estándar.

metro=1 => 100 cm
formula

m*(cm/m)

"""
#metros = float(input("Digite la longitud en metros: "))
#conversion= metros*(100/1)
#print("Este metro %f a cemtrimetros equivale a: %i cm" %(metros, conversion))

"""
10) Realice un algoritmo que calcule el cubo y el cuadrado de un determinado número:
"""

##numero  = int(input("Digite un numero: "))
##cuadrado = numero**2
##cubo= numero**3
##print("El cuadrado de %i es: %i" %(numero, cuadrado))
##print("El cubo de %i es: %i" %(numero, cubo ))

"""

11) Realice un algoritmo que solicite al usuario que escriba 2 números. Seguidamente, imprima
el total de la división en números decimales y el total de la división en números enteros 
( es decir, sin casillas decimales).
"""

#numero1 = float(input("Digite un numero: "))
#numero2 = float(input("Digite un numero: "))
#division= numero1/numero2
#divisionEntero= numero1//numero2
#print("La division es: ", division)
#print("La division es: ", divisionEntero)

"""
12) Realice un algoritmo que solicite al usuario la longitud y la altura de un cuadrado. 
Seguidamente, imprima para el usuario cuántos metros cuadrados posee el área total del cuadrado.
"""
##print("Calcular el area de un cuadrado\n")
##longitud= float(input("Digite longitud: "))
##altura= float(input("Digite altura: "))
##area= longitud* altura
##print("El  area total del cuadrado es: ", area)


"""
13) Realice un algoritmo que solicite al usuario informar una cantidad de días,
horas, minutos y segundos. Seguidamente, convierta todo a segundos.

Minuto (1) = 60 segundos (1 min = 60 segundos)
Hora (1) = 60 minutos (1 h = 60 minutos)
Día (1) = 24 horas (1440 minutos)
"""


"""
14) Realice un algoritmo que solicite al usuario informar el valor de una compra.Seguidamente,
aplique un 18% de descuento e imprima en la pantalla tanto el valor total como el valor con el
descuento aplicado.
"""

print("Compra en tienda")

costoT= int(input("Digite el consto total del producto: "))
conversion = 18/100
descuento = conversion * costoT
total = costoT-descuento

print("El descuento es %i peso y el total a pagar es: %i pesos" %(descuento,total))










