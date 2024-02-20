import pandas as pd

indice = {}
combinaciones = []


def recorrer():
    #buscamos el archivo y declaramos variables 
    df = pd.read_csv("dataset.csv")
    secuencia = df["string_a_modificar"].iloc[0]
    ventana = 10
    desplazamiento = 5
    #recorremos el arreglo con la ventana
    for i in range(0, len(secuencia), desplazamiento):
        ventana_actual = secuencia[i:i+ventana]
        #identificamos las alteraciones para la ventana
        alteraciones = df["alteracion"][df["posicion"].isin(range(i, i+ventana))]
        #crea todas las combinaciones para la ventana
        for alteracion in alteraciones:
            combinacion = ventana_actual.replace("referencia",alteracion)
            #guardamos las combinaciones en un arreglo y a su ves en un indice 
            combinaciones.append(combinacion)
        indice[i] = combinaciones

#creamos la funcion para mostrar las combinaciones realizadas 
def Mostrar_combinaciones():
    aux=0
    print("combinaciones realizadas:")
    for combinacion in combinaciones:
        print("combinacion N.",aux,":",combinacion)
        aux=aux+1
    
        
def combinaciones_rango():
    #cargamos el documento para hacer de guia sobre lo que se debe de combinar
    df = pd.read_csv("dataset.csv")
    #creamos un arreglo que guardara las combinaciones y declaramos variables
    combinaciones_rango= []
    aux=0
    ventana = 10
    desplazamiento = 5
    #pedimos al usuario que indique donde comenzara la combinacion y dodne terminara
    valor1 = int(input("ingresa donde comenzara el recorrido: "))
    valor2 = int(input("ingresa donde terminara: "))
    #identificamos los valores en arreglo y definimos el rango
    for i in range(valor1,valor2):
        #recorremos el arreglo con la ventana
        for i in range(0, len(combinaciones), desplazamiento):
            #identificamos las alteraciones para la ventana
            ventana_actual = combinaciones[i:i+ventana]
            cadena= ''.join(ventana_actual)
            alteraciones = df["alteracion"][df["posicion"].isin(range(i, i+ventana))]
            #crea todas las combinaciones para la ventana
            for alteracion in alteraciones:
                combinacion_rango = cadena.replace("referencia",alteracion)
                combinaciones_rango.append(combinacion_rango)
    #creamos la funcion para mostrar las combinaciones realizadas 
    for combinacion_rango in combinaciones_rango:
        print("combinacion","{:.1f}".format(aux),":",combinacion_rango)
        aux=aux+0.1

def combinaciones_todo():
    #declaramos los valores iniciales para que cubra todo el arreglo 
    df = pd.read_csv("dataset.csv")
    combinaciones_rango= []
    aux=0
    ventana = 10
    desplazamiento = 5
    valor1 = 0
    valor2 = 125
    for i in range(valor1,valor2):
        for i in range(0, len(combinaciones), desplazamiento):
            ventana_actual = combinaciones[i:i+ventana]
            cadena= ''.join(ventana_actual)
            alteraciones = df["alteracion"][df["posicion"].isin(range(i, i+ventana))]

            for alteracion in alteraciones:
                combinacion_rango = cadena.replace("referencia",alteracion)
                combinaciones_rango.append(combinacion_rango)
    for combinacion_rango in combinaciones_rango:
        print("combinacion","{:.1f}".format(aux),":",combinacion_rango)
        aux=aux+0.1

def combinaciones_entrada():
    df = pd.read_csv("dataset.csv")
    combinaciones_uno_a_uno=[]
    combinaciones_finales = []
    com1= int(input("ingrese N. combinacion: "))
    com2= int(input("ingrese N. combinacion con la que desea combinar: "))
    combinacion1= indice[com1]
    combinacion2= indice[com2]
    combinaciones_finales.append(combinacion1)
    combinaciones_finales.append(combinacion2)
    ventana = 10
    desplazamiento = 5
    aux=0
    for i in range(com1,com2):
        for j in range(0, len(combinaciones_finales), desplazamiento):
            ventana_actual = combinaciones_finales[i:i+ventana]
            cadena= ''.join(ventana_actual)
            alteraciones = df["alteracion"][df["posicion"].isin(range(i, i+ventana))]

            for alteracion in alteraciones:
                combinacion_uno_a_uno = cadena.replace("referencia",alteracion)
                combinaciones_uno_a_uno.append(combinaciones_finales)
                        
        for combina_uno_a_uno in combinaciones_uno_a_uno:
            print("combinacion","{:.1f}".format(aux),":",combina_uno_a_uno)
            aux=aux+0.1

    

recorrer()
combinaciones_entrada()
#combinaciones_todo()
#combinaciones_rango()
#Mostrar_combinaciones()
