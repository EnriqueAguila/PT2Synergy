import csv #Se importa datos del archivo csv Enrique Aguilar Martinez

lista_datos = [] #crer listas para guardar datos

#Lectura de el archivo para guardar en lista 
with open('synergy_logistics_database.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    skip = 0
    for linea in lector:
        if skip == 0:
            skip += 1
        else:
            lista_datos.append(linea)

# Tarea 1
        

#Haciendo registro de las rutas
#Generando variable de busqueda de sentido 
def rutas_demanda(direccion): #Definiendo una función que haga el listado 1
    rutas_conteo = [] # Lista para guardar la ruta y cuantas veces se repite
    contador = 0 # Variable para contar el número de veces que una ruta se presenta
    valor = 0 #Variable para sumar el valor de la exportacion
    rutas_contadas = [] #Lista para guardar las listas que estan registradas
    
    for ruta in lista_datos:
        ruta_actual  = [ruta[2],ruta[3]]
        if ruta[1] == direccion and ruta_actual not in rutas_contadas:
            for movimiento in lista_datos:
                if ruta_actual == [movimiento[2],movimiento[3]] and movimiento[1] == direccion:
                    contador += 1
                    valor += int(movimiento[9])        
                    rutas_contadas.append(ruta_actual)
            formato = [ruta[2],ruta[3],contador,valor]
            rutas_conteo.append(formato)
            contador = 0
            valor = 0
    
    sorted(rutas_conteo,reverse=True,key=lambda x:x[2]) #Ordenando las rutas por su conteo
    count = 0
    for i in rutas_conteo:
        if count < 10:    
            print(i[0],i[1])
            count += 1
    print('')
#Consigna 2

def transportes_demanda(direccion): #Definiendo una función que genere las listas 
    transporte_valor = [] # Lista para guardar la ruta y su valor total por sentido logistico
    valor = 0 # Variable para contar el número de veces que una ruta se presenta
    transporte_valuado = [] #Lista para guardar las listas que ya han sido registradas
    
    for transporte in lista_datos: #creando a lista de los transportes y valor
        transporte_actual  = [transporte[7]]
        if transporte[1] == direccion and transporte_actual not in transporte_valuado:
            for movimiento in lista_datos:
                if transporte_actual == [movimiento[7]] and movimiento[1] == direccion:
                    valor += int(movimiento[9])        
                    transporte_valuado.append(transporte_actual)
            formato = [transporte[7],valor]
            transporte_valor.append(formato)
            valor = 0
    
    sorted(transporte_valor,reverse=True,key=lambda x:x[1]) #Ordenando las rutas por conteo
    
    print(f'Los 3 transportes más importantes de los {direccion}')
    count = 0
    for i in transporte_valor:
        if count < 3:    
            print(i[0],i[1])
            count += 1
    print('')
#Consigna 3

def paises_demanda(direccion): #Definiendo una función que genere las listas
    pais_valor = [] # Lista para guardar el pais y su valor total por sentido logistico
    pais_porcentaje = []
    valor = 0 # Variable para contar el número de veces que una ruta se presenta
    pais_valuado = [] #Lista para guardar las listas que estan registradas
    suma_total = 0
    if direccion == 'Exports':
        indice = 2
    elif direccion == 'Imports':
        indice = 3
    for pais in lista_datos:
        pais_actual  = pais[indice]
        if pais[1] == direccion and pais_actual not in pais_valuado:
            for movimiento in lista_datos:
                if pais_actual == movimiento[indice] and movimiento[1] == direccion:
                    valor += int(movimiento[9])
                    suma_total += int(movimiento[9])
                    pais_valuado.append(pais_actual)
            formato = [pais_actual,valor]
            pais_valor.append(formato)
            valor = 0
    suma_total
    pais_valor.sort(reverse=True,key=lambda x:x[1]) #Ordenando las rutas por su conteo
    porcentaje = 0  
    for pais in pais_valor: # creando un alista ordenada solo con los paises que suman al 80%
        if porcentaje < 80:
            porc = (pais[1]/suma_total)*100
            pais_porcentaje.append([pais[0],porc])
            porcentaje += porc
    print(f'Los países con el 80% del valor de los {direccion}')
    for i in pais_porcentaje:
        print(i[0],f'{i[1]}%')
    print("")
    return pais_porcentaje

selec = input('Selecciona la consigna que desees analizar 1|2|3')
valid = 0
while valid == 0:
    if selec == '1':
        rutas_demanda('Exports') 
        rutas_demanda('Imports') 
        valid = 1
    elif selec == '2':
        transportes_demanda('Exports') 
        transportes_demanda('Imports') 
        valid = 1
    elif selec == '3':
        paises_demanda('Exports') 
        paises_demanda('Imports') 
        valid = 1
    else :
        selec = input('Selecciona una consigna válida')

        


