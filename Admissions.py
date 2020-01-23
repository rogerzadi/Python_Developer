import pandas as pd 
import numpy as np

admissions = pd.read_csv('data/Admission_Predict.csv')
admissions.columns = admissions.columns.str.rstrip()
print(admissions.isna().sum()) #Vemos que columnas estan vacias

admissions.set_index('Serial No.', inplace=True) #Colocamos la calumna  'Seriañ No.' como index "
print(admissions["GRE Score"].value_counts()) # Vemos cuantos valores iguales  hay en la columna GRE Score
admissions.reset_index(inplace=True)

print(admissions[(admissions.CGPA>9) & (admissions.Research==1)]) #Filtrado de info donde la calificacion sea mayor a 9 y la columna Research sea 1

deff=admissions[(admissions.CGPA>9) & (admissions.SOP<3.5)]  #Asignación de varible donde se le otorgan los alumnos que tengas mas de 9 en CGPA pero menos de 3.5 en SOP
