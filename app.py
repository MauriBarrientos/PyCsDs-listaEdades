#importamos pandas

import pandas as pd
from analisis_estadistico import analisis_estadistico

#Obtener la lista de edades
lista_edades = [19,29,19,22,23,19,30,19,19,19,20,20,20,18,22,19,34,34,21,21,22,28,29,19,20,19,25,28,21,22]

results = analisis_estadistico(lista_edades)

print(results)
