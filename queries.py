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
                        SELECT productos.id, productos.nombre, productos.unidad, precios.precio, precios.fuente
                        FROM precios
                        JOIN productos ON productos.id = precios.producto_id
                        WHERE precios.anio = %s;
                    """
            cur.execute(query, (anio,))
            return cur.fetchall()
    except Exception as e:
        print(e)
