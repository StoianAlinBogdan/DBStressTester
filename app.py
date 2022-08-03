import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="alstoian",
        password="Admin1234"
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print(ver)