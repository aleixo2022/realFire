import psycopg2

# Conectando ao banco de dados PostgreSQL
def connect():
    conn = psycopg2.connect(
    host="localhost",
    database="newport",
    user="postgres",
    password="musica2000"
    )
    cursor = conn.cursor()
    return cursor