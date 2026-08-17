from loader import load_data_csv
from cleaner import clean_data
from database import save_to_db, create_table
from report import create_report


def run_pipline():
    df = load_data_csv()
    print(df)
    df = clean_data(df)
    create_table() 
    save_to_db(df)
    create_report()
    



if __name__ == "__main__":
    run_pipline()