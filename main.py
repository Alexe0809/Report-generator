from loader import load_data_csv
from cleaner import clean_data


def main():
    df = load_data_csv()
    df = clean_data(df)
    print(df)


if __name__ == "__main__":
    main()