from connect import get_db_connection

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS profesores (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100)
    );
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    create_table()