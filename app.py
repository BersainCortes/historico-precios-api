from flask import Flask, jsonify, request
from queries import get_productos, get_precio_historico, get_productos_anio, get_info_producto
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "nombre": "historico-precios-api",
        "descripcion": "API abierta de precios historicos en Mexico",
        "autor": "zen",
        "version": "1.0",
        "endpoints": {
            "GET /productos": "Lista todos los productos registrados",
            "GET /productos/<id>": "Información sobre un producto en especifico",
            "GET /precios/<id>": "Lista los precios historicos de un producto",
            "GET /anios/<anio>": "Lista precios de todos los productos en un año",
        },
        "aviso": "Los datos son recopilados colaborativamente. No garantizamos exactitud oficial."
    })

@app.route("/productos")
def productos():
    data = get_productos()
    return jsonify([{ "id": id, "nombre": nombre, "unidad": unidad } for id, nombre, unidad in data])

@app.route("/productos/<int:id_producto>")
def info_producto(id_producto):
    data = get_info_producto(id_producto)
    return jsonify([{ "id": id, "nombre": nombre, "unidad": unidad } for id, nombre, unidad in data])

@app.route("/precios/<int:id_producto>")
def precios_producto(id_producto):
    data = get_precio_historico(id_producto)
    return jsonify([{ "anio": anio, "precio": precio, "fuente": fuente } for anio, precio, fuente in data])

@app.route("/anios/<int:anio>")
def productos_anio(anio):
    data = get_productos_anio(anio)
    return jsonify([{ "producto_id": producto_id, "nombre": nombre, "unidad": unidad, "precio": precio, "fuente": fuente } for producto_id, nombre, unidad, precio, fuente in data])

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
