# main.py
import sqlite3
from src.extract import extract
from src.transform import transform
from src.load import load_to_csv, load_to_db
from src.query import run_query
from src.logger import log_progress

def main():
    url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
    log_file = "./log_file.txt"
    table_name = "Countries_by_GDP"
    table_attributes = ["Country", "GDP_USD_millions"]
    db_path = "data/World_Economies.db"
    csv_path = "data/Countries_by_GDP.csv"
    query_statement = "SELECT"
    log_progress("Preliminaries complete. Initiating ETL process.", log_file)

    # Log the initialization of the ETL process 
    log_progress("ETL Job Started", log_file) 
    
    # Log the beginning of the Extraction process 
    log_progress("Extract phase Started", log_file) 
    df = extract(url, table_attributes)

    # Log the completion of the Extraction process 
    log_progress("Extract phase Ended", log_file) 

    # Log the beginning of the Transformation process 
    log_progress("Transform phase Started", log_file) 
    transformed_data = transform(df)
    print("Transformed Data") 
    print(transformed_data) 

    # Log the completion of the Transformation process 
    log_progress("Transform phase Ended", log_file) 
    
    # Log the beginning of the Loading process 
    log_progress("Load to csv phase Started", log_file) 
    load_to_csv(transformed_data, csv_path)

    # Log the completion of the Loading process 
    log_progress("Load to csv phase Ended", log_file) 

    # Log the beginning of the Loading process 
    log_progress("Load to db phase Started", log_file) 
    conn = sqlite3.connect(db_path)
    load_to_db(transformed_data, conn, table_name)

    # Log the completion of the Loading process 
    log_progress("Load to db phase Ended", log_file) 
    
    # Log the completion of the ETL process 
    log_progress("ETL Job Ended", log_file) 

    # Log the beginning of the Querying process 
    log_progress("Querying phase Started", log_file) 
    query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
    run_query(query_statement, db_path)

    # Log the completion of the Querying process
    log_progress("Query process completed", log_file) 

if __name__ == "__main__":
    main()