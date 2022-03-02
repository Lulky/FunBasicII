#Ejercicio #1
def regresivo(num):
    array = []
    for x in range (num, -1, -1):
        array.append(x)
    return array
    
        

reg = regresivo(5)
print(reg)

#Ejercicio #2


list = [1, 2]
def recibe(a):
    print(a[0])
    return a[1]

boy = recibe(list)
print(boy)

#Ejercicio #3


arr = [1, 2, 3, 4, 5]
def longitud(b):
    return b[0] + len(b)

reto = longitud(arr)
print(reto)

#Ejercicio #4

arreglo = [5,2,3,2,1,4]
arreglo2 =[]
def mayor(c):
    for x in arreglo:
        if(len(arreglo) < 2 ):
            return False
        elif(x > arreglo[1]):
            arreglo2.append(x)      
    print(len(arreglo2))
    return arreglo2

get_right = mayor(arreglo)
print(get_right)

#Ejercicio 5


def arrow(tamaño, valor):
    last =[]
    for x in range(0, tamaño):
        last.append(valor)
        
    return last


back = arrow(4,7)
pent = arrow(6,2)
print(back)
print(pent)















