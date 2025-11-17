#1. Se quiere llevar el control de ventas de dos productos: tazas y termos. Se guardan
#las cantidades vendidas en una semana (7 días). Para ello se cargan dos arreglos,
#uno por cada producto. Las tazas tienen un precio de $6750 y los termos de $8075.
#La carga finaliza con cantidad = 0, y puede haber más de una venta por día
#Se pide:
#a) Ingresar el tipo de producto TZ para tazas y TE para termos.
#b) Ingresar la cantidad vendida según el producto seleccionado.
#c) Realizar una función que calcule el máximo de ventas en cantidad para un
#producto dado y mostrar el monto correspondiente.
#d) Calcular el promedio semanal vendido en cantidad.
#e) Validar los datos de entrada, no permitir cantidades negativas
#dia=0
#tazasvendidas=[]
#termosvendidos=[]
#PRECIO_TAZAS=6750
#PRECIO_TERMOS=8075
#while dia!=7:
#    print (f"--- Dia={dia+1} ---")
#    tipoproducto=str(input("Ingrese el tipo de producto. TZ para tazas y TE para termos: "))
#    cantidad=int(input("Ingrese la cantidad vendida: "))
#    if cantidad>0:
#        if tipoproducto.lower()=="tz":
#            tazasvendidas.append(cantidad)
#        elif tipoproducto.lower()=="te":
#            termosvendidos.append(cantidad)    
#    elif cantidad==0 or tipoproducto==0:
#        print ("Fin de venta diaria, 0 ingresado")
#        dia+=1
#    else:
#        print ("El numero ingresado no puede ser negativo")
#for dia in range (7):
#    print (f"--- Dia={dia+1} ---")
#    ventashoy=int(input("Cuantas ventas tuvo hoy?: "))
#    for i in range (ventashoy):
#        tipoproducto=str(input("Ingrese el tipo de producto. TZ para tazas y TE para termos: "))
#        cantidad=int(input("Ingrese la cantidad vendida: "))
    
        
#        if tipoproducto.lower()=="tz":
#            tazasvendidas.append(cantidad)
#        elif tipoproducto.lower()=="te":
#            termosvendidos.append(cantidad)    
#        elif cantidad==0:
#            print ("Fin de ventas, 0 ingresado")
#        else:
#            print ("El numero ingresado no puede ser negativo")

#if len(tazasvendidas)>1:
#    print (f"La cantidad de tazas vendidas fueron: {tazasvendidas}")
#elif len(termosvendidos)>1:
#    print (f"La cantidad de termos vendidas fueron: {termosvendidos}")

#def calcularmáximodeventas(a):
#    if len(a)==0:
#        return 0
#def cargardatosdescarte(arrayidiomascursados,arraynrosidentificación,arrayedadestudiante):
#    idiomacursada=str(input("Ingrese el idioma cursado: "))
#    while idiomacursada.lower()!="stop":
#        if idiomacursada.lower()!="i" and idiomacursada.lower()!="p" and idiomacursada.lower()!="t":
#            print ("El idioma solo puede ser i p o t, el arreglo no sera guardado")
#        nroidentificacion=int(input("Ingrese el numero de identficación del estudiante: "))
#        if nroidentificacion<0 or nroidentificacion>10000:
#            print ("El nro de identificación no puede ser mayor a 10000 ni menor a 0, el arreglo no sera guardado")
#        edadestudiante=int(input("Ingrese la edad del estudiante: "))
#        if edadestudiante<=16:
#            print ("La edad del estudiante debe ser mayor a 16, el arreglo no sera guardado")
#        if (nroidentificacion>0 and nroidentificacion<10000) and (edadestudiante>16) and (idiomacursada.lower()=="i" or idiomacursada.lower()=="p" or idiomacursada.lower()=="t"):
#            arrayidiomascursados.append(idiomacursada)
#            arraynrosidentificación.append(nroidentificacion)
#            arrayedadestudiante.append(edadestudiante)
#        idiomacursada=str(input("Ingrese el idioma cursado: "))
#    return

#cargardatos(arrayidiomascursados,arraynrosidentificación,arrayedadestudiante)

#Funcion para cargar los datos pedidos
def cargardatosinsistir(arrayidiomascursados,arraynrosidentificación,arrayedadestudiantes):
    idiomacursada=str(input("Ingrese el idioma cursado: "))
    while idiomacursada.lower()!="i" and idiomacursada.lower()!="p" and idiomacursada.lower()!="t" and idiomacursada.lower()!="stop":
        idiomacursada=str(input("ERROR: Ingrese un idioma valido: "))
    while idiomacursada.lower()!="stop":
        nroidentificación=int(input("Ingrese numero de identificación: "))
        while nroidentificación>=10000 or nroidentificación<=0:
            nroidentificación=int(input("ERROR: Ingrese un numero de identificación valido: "))
        edadestudiante=int(input("Ingrese la edad del estudiante: "))
        while edadestudiante<=16:
            edadestudiante=int(input("ERROR: La edad debe ser mayor a 16: "))
        
        arrayedadestudiantes.append(edadestudiante)
        arrayidiomascursados.append(idiomacursada)
        arraynrosidentificación.append(nroidentificación)
        
        idiomacursada=str(input("Ingrese el idioma cursado: "))
        while idiomacursada.lower()!="i" and idiomacursada.lower()!="p" and idiomacursada.lower()!="t" and idiomacursada.lower()!="stop":
            idiomacursada=str(input("ERROR: Ingrese un idioma valido: "))

#Promedio total de edades en la universidad (punto b)
def calcular_promedio_edad(arrayedadestudiantes):
    acumulador=0
    cantidad_total=(len(arrayedadestudiantes))
    for i in range (cantidad_total):
        acumulador= acumulador + arrayedadestudiantes[i]
    acumulador= acumulador/cantidad_total
    return acumulador

#Sumar edades por cada materia (punto a)
def suma_edades(arrayedadestudiantes,arrayidiomascursados,letra):
    sumador=0
    for i in range (len(arrayedadestudiantes)):
        if arrayidiomascursados[i]==letra:
            sumador= sumador+arrayedadestudiantes[i]
    return sumador    

#Encontrar el estudiante mas joven (punto c)
def estudiante_mas_joven (arrayedadestudiantes):
    minimaedad=arrayedadestudiantes[0]
    posicionminima=0
    for i in range (1, len(arrayedadestudiantes)):
        if minimaedad>arrayedadestudiantes[i]:
            minimaedad=arrayedadestudiantes[i]
            posicionminima=i
    return posicionminima

#Buscar el estudiante con id 1000(punto d)
def busqueda_estudiante_1000(arraynrosidentificación):
    valorbuscado=1000
    i=0
    while (i <len(arraynrosidentificación)) and arraynrosidentificación[i]!=valorbuscado :
        i=+1
    return i

#Encontrar al estudiante mas viejo, luego se van a borrar sus datos
def busqueda_estudiante_viejo(arrayedadestudiantes):
    maxedad=arrayedadestudiantes[0]
    posicionmaxima=0
    for i in range (1, len(arrayedadestudiantes)):
         if maxedad<arrayedadestudiantes[i]:        
             maxedad=arrayedadestudiantes[i]
             posicionmaxima=i
    return posicionmaxima

def intercambiar_datos_por_edad(arrayedadestudiantes,arrayidiomascursados,arraynrosidentificación):
    for i in range (0, len (arrayedadestudiantes) -1, 1):
        for j in range (i + 1, len(arrayedadestudiantes), 1):
            if arrayedadestudiantes[j]<arrayedadestudiantes[i]:
                
                aux_edad=arrayedadestudiantes[j]
                arrayedadestudiantes[j]=arrayedadestudiantes[i]
                arrayedadestudiantes[i]=aux_edad

                aux_nombres=arraynrosidentificación[j]
                arraynrosidentificación[j]=arraynrosidentificación[i]
                arraynrosidentificación[i]=aux_nombres

                aux_idiomas=arrayidiomascursados[j]
                arrayidiomascursados[j]=arrayidiomascursados[i]
                arrayidiomascursados[i]=aux_idiomas






##EJECUCIÓN GENERAL
arrayidiomascursados=[]
arraynrosidentificación=[]
arrayedadestudiantes=[]

#iniciar el programa
cargardatosinsistir(arrayidiomascursados,arraynrosidentificación,arrayedadestudiantes)

if len(arrayedadestudiantes)!=0:
    #mostrar el promedio de edades
    acumulador=calcular_promedio_edad(arrayedadestudiantes)
    print (f"El promedio de todas las edades de la univerisdad es de {acumulador}")


    #mostrar la edad por materia
    edad_i=suma_edades(arrayedadestudiantes,arrayidiomascursados,"i")
    print (f"La suma de las edades de ingles es de {edad_i}")

    edad_p=suma_edades(arrayedadestudiantes,arrayidiomascursados,"p")
    print (f"La suma de las edades de portugues es {edad_p}")

    edad_t=suma_edades(arrayedadestudiantes,arrayidiomascursados,"t")
    print (f"La suma de las edades de italiano es {edad_t} ")


    #mostrar al estudiante mas joven
    posicionminima=estudiante_mas_joven(arrayedadestudiantes)
    print (f"""El numero de identificación del estudiante mas joven es {arraynrosidentificación[posicionminima]} 
            tiene {arrayedadestudiantes[posicionminima]} años y estudia {arrayidiomascursados[posicionminima]} """)

    #mostrar el estudiante de id 1000
    posicion1000=busqueda_estudiante_1000(arraynrosidentificación)
    if posicion1000<(len(arraynrosidentificación)):
        print (f"El estudiante con id 1000 estudia {arrayidiomascursados[posicion1000]} y tiene {arrayedadestudiantes[posicion1000]} años ")
    else:
        print ("No se encontro el estudiante con id 1000")

    #Ordenar arreglos
    intercambiar_datos_por_edad(arrayedadestudiantes,arrayidiomascursados,arraynrosidentificación)
    #Eliminar el estudiante mas viejo
    posicionviejo=busqueda_estudiante_viejo(arrayedadestudiantes)
    arrayedadestudiantes.pop(posicionviejo)
    arrayidiomascursados.pop(posicionviejo)
    arraynrosidentificación.pop(posicionviejo)

