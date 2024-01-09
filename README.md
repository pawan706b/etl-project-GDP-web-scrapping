# ETL Project: GDP Data Extraction, Transformation, and Loading

This project focuses on Extracting, Transforming, and Loading (ETL) Gross Domestic Product (GDP) data. The goal is to retrieve GDP information from "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29", transform the data into 'Billion USD' from 'Million USD', load it into a CSV file and a database, run a predefined query on the database, and log the progress with timestamps.

## Project Structure

- **`src/`**: Contains the source code for the ETL process.
  - `extract.py`: Implements the data extraction function.
  - `transform.py`: Transforms GDP information from 'Million USD' to 'Billion USD'.
  - `load.py`: Loads transformed information into a CSV file and a database.
  - `query.py`: Runs a predefined query on the database.
  - `logger.py`: Logs the progress of the code with timestamps.

- **`data/`**: Placeholder for input and output data files.
  - `input_data.csv`: Input CSV file containing GDP information.
  - `output_data.csv`: Output CSV file with transformed GDP information.
  - `database.db`: SQLite database file.

- **`requirements.txt`**: List of Python dependencies needed for the project.

- **`main.py`**: Main script to execute the entire ETL process.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/pawan706b/etl-project-GDP-web-scrapping.git
   cd etl-project-GDP-web-scrapping
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Execute the ETL process:
    ```bash
    python main.py
Configuration
Modify the configuration parameters in **config.py** to customize the behavior of the ETL process.

Logging
The progress of the ETL process is logged with appropriate timestamps. View the logs in the logs/ directory.

Notes
- Ensure internet connectivity for data extraction from the specified URL.
- Make sure to configure the database connection details in config.py before running the project.
- Feel free to explore and adapt the code to suit your specific requirements. If you encounter any issues or have suggestions for improvement, please create an issue on the GitHub repository.

Happy ETL-ing!