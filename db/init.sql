-- La estructura también la garantiza SQLAlchemy al iniciar la aplicación.
-- Este archivo se conserva como script de base de datos solicitado por el laboratorio.
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    rol VARCHAR(20) NOT NULL DEFAULT 'usuario',
    password_hash VARCHAR(255) NOT NULL,
    requiere_codigo BOOLEAN NOT NULL DEFAULT TRUE
);
