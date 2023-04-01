print("---------------------------------------")
print("--------SUMA ENTEROS0------------------")
print("---------------------------------------")

N = int(input("ingrese la cantidad mumeros que desea sumar:\n "))

i = 1

suma = 0 
 
while i <= N:
    suma = suma + i
    i = i + 1
    print("i = " + str(i))
    print("suma =" +str(suma))

print("la suma de los primeros", N, "numeros naturales es", suma,)