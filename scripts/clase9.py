#Clase 9:

# Data frames de Pandas
import pandas as pd
import numpy as np

       columns=["columna_1", "columna_2"],
                     index=['a','b','c'])


produccion = pd.Series([5, 11, 4, 7, 2],
    index= ['gen1', 'gen2', 'gen3','gen4', 'gen5'],
    name='production')

    index=['gen1', 'gen2', 'gen3', 'gen5'],
    name='costos')



##Ejercicio 1:

produccion = pd.Series([5, 11, 4, 7, 2],
        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
        name='produccion')

        index=['gen1', 'gen2', 'gen3', 'gen5'],
                    name='costos')

                'produccion': produccion})
costo_beneficio['costo unitario']=costo_beneficio.costos/costo_beneficio.produccion
print(costo_beneficio)