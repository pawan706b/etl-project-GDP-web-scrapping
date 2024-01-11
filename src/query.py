# src/query.py
import pandas as pd

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    output = pd.read_sql(query_statement, sql_connection)
    print(output)