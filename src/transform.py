# src/transform.py
import numpy as np

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''

    data_list = df['GDP_USD_millions'].tolist()
    data_list = [float("".join(x.split(','))) for x in data_list]
    data_list = [np.round(x/1000,2) for x in data_list]
    df['GDP_USD_millions'] = data_list
    df = df.rename(columns={'GDP_USD_millions':'GDP_USD_billions'})
    print(df['GDP_USD_billions'])
    return df

