from flask import Flask, jsonify, request
from connection import supabase
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
            "GET /precios/<id>": "Lista los precios historicos de un producto",
            "GET /anios/<anio>": "Lista precios de todos los productos en un año",
        },
        "aviso": "Los datos son recopilados colaborativamente. No garantizamos exactitud oficial."
    })


if __name__ == '__main__':
    app.run(debug=True)
