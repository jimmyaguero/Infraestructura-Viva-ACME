-- 1. Creación de la tabla con el esquema de ACME
CREATE TABLE ventas_acme (
    id_venta INTEGER PRIMARY KEY,
    producto TEXT,
    monto REAL,
    departamento TEXT
);

-- 2. Inserción de datos de prueba para la demo
INSERT INTO ventas_acme (producto, monto, departamento) 
VALUES ('Suscripción Cloud', 1500.00, 'Ventas'),
       ('Soporte Técnico', 500.00, 'Soporte');

-- 3. Consulta de validación (Métrica: 3-5 consultas probadas)
SELECT departamento, SUM(monto) AS total 
FROM ventas_acme 
GROUP BY departamento;
