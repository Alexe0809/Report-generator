import psycopg2
import config

def connect():
    conn = psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )
    return conn

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS orders (
        order_id  INTEGER PRIMARY KEY,
        date      DATE,
        customer  TEXT,
        product   TEXT,
        quantity  INTEGER,
        price     NUMERIC(10, 2),
        status    TEXT
            );""")
    conn.commit()
    cur.close()
    conn.close()

def save_to_db(df):
    conn = connect()
    cur = conn.cursor()
    rows = list(df.itertuples(index=False, name=None))
    cur.executemany("""
        INSERT INTO orders (order_id, date, customer, product, quantity, price, status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (order_id) DO NOTHING
    """, rows)
    conn.commit()
    print('Data was sucsesfully added')
    cur.close()
    conn.close()
        

if __name__ == "__main__":
    conn = connect()
    print('Connection is sucesfull')
    conn.close()
    create_table()