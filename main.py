from loader import load_data_csv
from cleaner import clean_data
from database import save_to_db, create_table


def main():
    df = load_data_csv()
    print(df)
    df = clean_data(df)
    create_table() 
    save_to_db(df)
    



if __name__ == "__main__":
    main()