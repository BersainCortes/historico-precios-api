from connection import create_connection

def get_productos():
    try:
        con = create_connection()
        with con.cursor() as cur:
            cur.execute("SELECT * FROM productos")
            return cur.fetchall()
    except Exception as e:
        print(e)
