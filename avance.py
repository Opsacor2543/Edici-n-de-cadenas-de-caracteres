import pandas as pd

def recorrer():
    archivos= pd.read_csv('dataset.csv')
    arreglos= archivos('string_a_modificar')
    for arreglo in arreglos:
        print(arreglo);

recorrer()