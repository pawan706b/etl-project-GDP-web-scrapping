# src/extract.py
import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''

    # Extract webpage as text
    page = requests.get(url).text
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page, "html.parser")
    # Create empty pandas DataFrame with columns as table attributes
    df = pd.DataFrame(columns=table_attribs)
    #Extract all the attributes of html object
    tables = soup.find_all('tbody')
    rows = tables[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {table_attribs[0]:col[0].a.contents[0],
                             table_attribs[1]: col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)
    return df

