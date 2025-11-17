#Funcion que realiza la carga de datos de cada venta
def cargar_datos(arr_nroentrada,arr_sede,arr_personasentrada,arr_preciototal):
    sede=str(input("Ingrese la sede: "))
    while sede.lower()!="caballito" and sede.lower()!="flores" and sede.lower()!="fin":
        sede=str(input("ERROR: Ingrese la sede: "))
    while sede.lower()!="fin":
        nro=int(input("Ingrese el numero identificativo de la entrada: "))
        while nro>500 or nro<1:
            nro=int(input("ERROR: Ingrese el numero identificativo de la entrada: "))
        personas=int(input("Ingrese el numero de personas incluidas en la entrada: "))
        while personas<=0:
            personas=int(input("ERROR, el numero de personas no puede ser menor a 1: Ingrese el numero de personas incluidas en la entrada: "))
        precio=int(input("Ingrese el precio total de la entrada: "))
        while precio<0:
            precio=int(input("ERROR, el precio de la entrada no puede ser negativo: Ingrese el precio total de la entrada: "))
        
        arr_sede.append(sede)
        arr_nroentrada.append(nro)
        arr_personasentrada.append(personas)
        arr_preciototal.append(precio)

        sede=str(input("Ingrese la sede: "))
        while sede.lower()!="caballito" and sede.lower()!="flores" and sede.lower()!="fin":
            sede=str(input("ERROR: Ingrese la sede: "))

#Funcion que suma las personas segun sede
def suma_sede(arr_personasentrada,arr_sede, a):
    sumador=0
    for i in range (len(arr_personasentrada)):
        if arr_sede[i]==a:
            sumador= sumador+arr_personasentrada[i]
    return sumador

#Funcion que promedia las personas por cada entrada
def promedio_personas(arr_personasentrada):
    contador=0
    divisor=len(arr_personasentrada)
    for i in range (divisor):
        contador= contador + arr_personasentrada[i] 
        i= i + 1       
    contador=contador/divisor
    return contador

#Funcion que busca la entrada con el precio mas alto
def precio_mas_alto(arr_preciototal):
    max=0
    posicionmaxima=0
    for i in range (len(arr_preciototal)):
        if max<arr_preciototal[i]:
            max=arr_preciototal[i]
            posicionmaxima=i
    return posicionmaxima

#Funcion que busca si se vendio una entrada para 10 personas
def busqueda_entrada_diez(arr_personasentrada):
    busqueda=10
    i=0
    while i<len(arr_personasentrada) and arr_personasentrada[i]!=busqueda:
        i= i + 1
    return i

#Funcion que ordena los datos por el numero identificativo
def ordenamiento_datos(arr_nroentrada,arr_sede,arr_personasentrada,arr_preciototal):
    for i in range (0, len(arr_nroentrada) -1, 1):
        for j in range (i + 1, len(arr_nroentrada, 1)):
            if arr_nroentrada[i]>arr_nroentrada[j]:
                
                auxentrada=arr_nroentrada[j]
                arr_nroentrada[j]=arr_nroentrada[i]
                arr_nroentrada[i]=auxentrada

                auxsede=arr_sede[j]
                arr_sede[j]=arr_sede[i]
                arr_sede[i]=auxsede

                auxpersona=arr_personasentrada[j]
                arr_personasentrada[j]=arr_personasentrada[i]
                arr_personasentrada[i]=auxpersona

                auxprecio=arr_preciototal[j]
                arr_preciototal[j]=arr_preciototal[i]
                arr_preciototal[i]=auxprecio


##FUNCION GENERAL

#Definicion de arreglos
arr_nroentrada=[]
arr_sede=[]
arr_personasentrada=[]
arr_preciototal=[]

#Carga de datos
cargar_datos(arr_nroentrada, arr_sede, arr_personasentrada, arr_preciototal)



# Imprimir la suma por sede
personascaballito=suma_sede(arr_personasentrada,arr_sede,"caballito")
personasflores=suma_sede(arr_personasentrada,arr_sede,"flores")
print (f"En caballito hubo un total de {personascaballito} personas")
print (f"En flores hubo un total de {personasflores} personas")

# Imprimir el promedio por entrada
promediototal=promedio_personas(arr_personasentrada)
print (f"El promedio total de personas por entradas es de {promediototal}")

#Imprimir el precio de entrada mas alto y su sede
posicionmaxima=precio_mas_alto(arr_preciototal)
print (f"La entrada con mayor precio fue la entrada {arr_nroentrada[posicionmaxima]} con un precio de {arr_preciototal[posicionmaxima]} en la sede de {arr_sede[posicionmaxima]}")

#Imprimir datos de entrada para 10 personas
entrada10=busqueda_entrada_diez(arr_personasentrada)
if entrada10<(len(arr_personasentrada)):
    print (f"La entrada con 10 personas es la {arr_nroentrada[entrada10]},valio {arr_preciototal[entrada10]} y se vendio en la sede {arr_sede[entrada10]} ")

#Ordenar datos
ordenamiento_datos(arr_nroentrada, arr_sede, arr_personasentrada, arr_preciototal)
