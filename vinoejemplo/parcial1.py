import pandas as pd

df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

def clasificar(parametro1, parametro2, parametro3):
    for i, n in enumerate(parametro2):
        if n >= parametro1:
            df.loc[i, parametro3] = 'alto'
        else:
            df.loc[i, parametro3] = 'bajo'
    resultado = df.groupby(parametro3).quality.mean()
    return print (resultado)

#Aca se realiza la mediana y se asigna a una variable 
Malcohol = df.alcohol.median()
MpH = df.pH.median()
MResidualSugar = df.residual_sugar.median()
MCitricAcid = df.citric_acid.median()

#Asigancion de nombres 
alcohol = 'alcohol'
ph = 'Ph'
residualSugar= 'residual sugar'
citricAcid = 'citric acid'

#Se envian las variables a la funcion clasificar 
ResultadoAlcohol = clasificar(Malcohol, df.alcohol, alcohol)
ResultadoPh = clasificar(MpH, df.pH, ph)
ResultadoResidual_sugar = clasificar(MResidualSugar, df.residual_sugar, residualSugar)
RresultadoCitric_acid = clasificar(MCitricAcid, df.citric_acid, citricAcid)

