-- Base de datos
CREATE DATABASE senatic1

-- Uso de la BD
USE senatic1

-- Tablas con sus columnas y restricciones.
CREATE TABLE programa (id_prog VARCHAR (6) PRIMARY KEY,
nombre VARCHAR (40) not null UNIQUE);

-- Insertar registros
INSERT INTO programa (id_prog, nombre) VALUES
(2020,'Artes plasticas'), 
(2021,'Asistencia administrativa'), 
(2022,'Auxiliar de farmacia'), 
(2023,'Licenciatura en musica'),  
(2024,'Mecanica automotriz'),
(2025,'Mecanica diesel'), 
(2026,'Operario en confección industrial'), 
(2027,'Programacion de software'), 
(2028,'Reparación de aires acondicionados'),   
(2029,'Sistema');


-- Tabla profesor
CREATE TABLE profesor (id_prof VARCHAR (15) PRIMARY KEY,
nombre VARCHAR (50) not null);

-- Insertar registros
INSERT INTO profesor (id_prof, nombre) VALUES
(40, 'Byron Pradera'),
(41, 'Mireya Cabrera'),
(42, 'Carlos Trujillo'),
(43, 'Juan Valencia'),
(44, 'Susana Romero'),
(45, 'Diana Zapata'),
(46, 'Pedro Montero'),
(47, 'Jose Lopez'),
(48, 'Diego Paredes'),
(49, 'Karol Suarez');


-- Tabla Asignatura
CREATE TABLE asignatura (id_asig VARCHAR (6) PRIMARY KEY,
nombre VARCHAR (30) not null UNIQUE, 
id_prog VARCHAR (6) not null, CONSTRAINT fk_programa
FOREIGN KEY (id_prog) REFERENCES programa (id_prog),
id_prof VARCHAR (15) not null, CONSTRAINT fk_profesor 
FOREIGN KEY (id_prof) REFERENCES profesor (id_prof));

-- Insertar registros
INSERT INTO asignatura (id_asig, nombre, id_prog, id_prof) VALUES
(1,'Pintura alternativa',2020, 40), 
(2,'Gestión de bases de datos',2021, 41), 
(3,'Promoción de la salud',2022, 42), 
(4,'Teoria y literatura musical',2023, 43),
(5,'Electronica',2024, 44),
(6,'Hidráulica',2025, 45),
(7,'Indumentaria de textiles',2026, 46), 
(8,'Programacion web',2027, 47),  
(9,'Refrigeracion',2028, 48),   
(10,'Redes de computadores',2029, 49);   


-- Tabla Alumno
CREATE TABLE alumno (id_alum VARCHAR(10) PRIMARY KEY,
nombre VARCHAR (30) not null,
id_prog VARCHAR (6) not null,
id_asig VARCHAR (6) not null);

-- Insertar registros
INSERT INTO alumno (id_alum, nombre, id_prog, id_asig) VALUES
(101,'Sara Castilla',2020, 1),
(102,'Sirena Barco',2021, 2),
(103,'Danilo Pereira',2022, 3),
(104,'Angel Montes',2023, 4),
(105,'Hilda Quispe',2024, 5),
(106,'Karina Mendoza',2025, 6),
(107,'Carlos Saltos',2026, 7),
(108,'Leonel Massa',2027, 8),
(109,'Jorge Barril',2028, 9),
(110,'Pablo Gaviria',2029, 10);


-- Seleccionar por tabla
SELECT * FROM programa
SELECT * FROM profesor
SELECT * FROM asignatura
SELECT * FROM alumno
 

-- -- Añadir la restricción de clave foránea a la tabla alumno
ALTER TABLE dbo.alumno
ADD CONSTRAINT fk_id_programa
FOREIGN KEY (id_prog) REFERENCES programa (id_prog);


-- Inner Join
SELECT profesor.nombre, asignatura.nombre 
FROM profesor
INNER JOIN asignatura ON profesor.id_prof = asignatura.id_prof;

SELECT programa.nombre, asignatura.nombre, profesor.nombre 
FROM programa 
INNER JOIN asignatura ON programa.id_prog = asignatura.id_prog
INNER JOIN profesor ON profesor.id_prof = asignatura.id_prof;
--- where profesor.id_prof !='90034' or programa.nombre = 'tps36';

