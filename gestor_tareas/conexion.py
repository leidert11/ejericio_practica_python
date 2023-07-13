import mysql.connector

def establecer_conexion():
    # Establecer la conexión con la base de datos
    host = "localhost"
    usuario = "root"
    contraseña = ""
    base_datos = "gestor_tareas"

    conexion = mysql.connector.connect(
        host=host,
        user=usuario,
        password=contraseña,
        database=base_datos
    )

    return conexion

def crear_tabla_tareas():
    conexion = establecer_conexion()

    cursor = conexion.cursor()
    #una vez que se ejecuta comentar la tabla
    # Definir el script para crear la tabla
    """script_creacion =
    CREATE TABLE tareas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        descripcion TEXT,
        completada BOOL DEFAULT 0
    )
    """

    # Ejecutar el script de creación
    # cursor.execute(script_creacion)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

# Llamar a la función para crear la tabla
crear_tabla_tareas()
