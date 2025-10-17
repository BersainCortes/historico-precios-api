CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    unidad VARCHAR(50)
);

CREATE TABLE precios (
    id SERIAL PRIMARY KEY,
    producto_id INT NOT NULL REFERENCES productos(id) ON DELETE CASCADE,
    anio INT NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    fuente VARCHAR(100)
);

CREATE TABLE solicitudes (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(100) NOT NULL,
    anio INT NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    fuente VARCHAR(100),
    comentario TEXT,
    estado VARCHAR(20) DEFAULT 'pendiente',
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
