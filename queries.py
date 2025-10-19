from connection import create_connection

def get_productos():
    try:
        con = create_connection()
        with con.cursor() as cur:
            cur.execute("SELECT * FROM productos")
            return cur.fetchall()
    except Exception as e:
        print(e)

def get_precio_historico(id_producto):
    try:
        con = create_connection()
        with con.cursor() as cur:
            query = """
                        SELECT anio, precio, fuente FROM precios WHERE producto_id = %s ORDER BY anio ASC;
                    """
            cur.execute(query, (id_producto,))
            return cur.fetchall()
    except Exception as e:
        print(e)

def get_productos_anio(anio):
    try:
        con = create_connection()
        with con.cursor() as cur:
            query = """
                        SELECT p.nombre, p.unidad, pr.precio, pr.fuente FROM precios pr
                        JOIN productos p ON p.id = pr.id_producto WHERE pr.anio = %s
                        ORDER BY p.nombre;
                    """
            cur.execute(query, (anio,))
            return cur.fetchall()
    except Exception as e:
        print(e)
