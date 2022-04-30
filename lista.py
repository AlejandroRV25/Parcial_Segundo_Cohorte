lista=[]
lista_invertida = lista[: -1]

def llenar_lista():
    n = int(input("Ingrese el número de datos que desea enlistar: "))
    for i in range(n):
        numero=input("Ingrese el número: ")
        lista.append(numero) 

llenar_lista()
print(lista)
print(lista_invertida)
