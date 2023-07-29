#Leer csv:
import pandas as pd
dataframe = pd.read_csv('ejemplo.csv')
############################################################################
Leer csv sin header:
dataframe = pd.read_csv('ejemplo.csv', header=None, names =['','','']
############################################################################
#Seleccionar columnas.
data = dataframme[['','']]
############################################################################
#Leer de forma inversa.
df[::-1]
############################################################################
import mplfinance as mpf
import pandas as pd
df = pd.read_csv('goldprices.csv',index_col=0,parse_dates=True)
df['RealClose'] = df['Close'].values  # guardaa los valores de cierre en caso de quererlos más tarde
df['Close'] = df['Low'].values        # establece la columna "cierre" en valores bajos
mpf.plot(df,type='line')              # mostrar plot y tipo
############################################################################
#Seleccionar por fecha
chart = df.loc['2019-6-1':'2020-6-10']
mpf.plot(chart,type='candle')              # mostrar plot y tipo