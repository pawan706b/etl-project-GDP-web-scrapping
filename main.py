# main.py
from src.extract import extract
from src.transform import transform
from src.load import load_to_csv, load_to_db
from src.query import run_query
from src.logger import log_progress

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
log_file = "log_file.txt"
table_name = "Countries_by_GDP"
table_attributes = ["Country", "GDP_USD_millions"]
db_path = "data/World_Economies.db"
csv_path = "data/Countries_by_GDP.csv"
query_statement = "SELECT"

def main():
    # Log the initialization of the ETL process 
    log_progress("ETL Job Started") 
    
    # Log the beginning of the Extraction process 
    log_progress("Extract phase Started") 
    df = extract(url, table_attributes)

    # Log the completion of the Extraction process 
    log_progress("Extract phase Ended") 

    # Log the beginning of the Transformation process 
    log_progress("Transform phase Started") 
    transformed_data = transform(df)
    print("Transformed Data") 
    print(transformed_data) 

    # Log the completion of the Transformation process 
    log_progress("Transform phase Ended") 
    
    # Log the beginning of the Loading process 
    log_progress("Load phase Started") 
    load_to_csv(transformed_data, csv_path)
    load_to_db(transformed_data, db_path)

    # Log the completion of the Loading process 
    log_progress("Load phase Ended") 
    
    # Log the completion of the ETL process 
    log_progress("ETL Job Ended") 

    # Log the beginning of the Loading process 
    log_progress("Querying phase Started") 
    run_query(query_statement, db_path)

if __name__ == "__main__":
    main()