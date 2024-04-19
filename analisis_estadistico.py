import pandas as pd

def analisis_estadistico(lista_edades):
    # Validar que lista_edades sea una lista
    if not isinstance(lista_edades, list):
        raise ValueError("El argumento 'lista_edades' debe ser una lista")
    
    # Verificar si todos los elementos de lista_edades son numéricos
    for elemento in lista_edades:
        if not isinstance(elemento, (int, float)):
            raise ValueError("La lista 'lista_edades' debe contener solo valores numéricos")

    def calculo_fi(lista_edades):
        #Cálculo de la frecuencia absoluta simple
        serie_edades = pd.Series(lista_edades)
        fi = serie_edades.value_counts()
        #Ordenar de menor a mayor
        fi_sort = dict(sorted(fi.items()))
        #Crear el dataframe
        df = pd.DataFrame(list(fi_sort.items()), columns=['Edades', 'fi'])

        return df
    
    def calculo_Fi(df):
        #Cálculo de la frecuencia absoluta acumulada
        df['Fi'] = df['fi'].cumsum()
        return df
    
    #Calculo de la frecuencia relativa simple
    def calculo_ri(df):
        df['ri'] = (df['fi'] / df['fi'].sum()).round(4)
        return df
    
    #Calculo de la frecuencia relativa acumulada
    def calculo_Ri(df):
        df['Ri'] = df['ri'].cumsum()
        return df
    
    def calculo_pi(df):
        df['pi%'] = (df['ri'] * 100).round(4)
        return df
    
    def calculo_Pi(df):
        df['Pi%'] = df['Ri'] * 100
        return df
    
    #Llamar a las funciones de cálculo
    df = calculo_fi(lista_edades)
    df = calculo_Fi(df)
    df = calculo_ri(df)
    df = calculo_Ri(df)
    df = calculo_pi(df)
    df = calculo_Pi(df)

    return df
