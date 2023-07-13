from gestor_tareas.conexion import establecer_conexion

def crear_tarea(titulo,descripcion,completada):
    conexion=establecer_conexion()
    
    try:
        cursor = conexion.cursor()
        query = "insert into tareas (titulo,descripcion,completada) values(%s,%s,%s)" 
        valores = (titulo,descripcion,completada)
        cursor.execute(query,valores)
        
        conexion.commit()
        cursor.close()
        
        print("trea creada exitosamente. ")
    except Exception as e:
        print(f"Error al crear la tarea {e}")
    finally:
        conexion.close()
# Crear una función llamada "crear_tarea" que tome los parámetros
# necesarios para definir una nueva tarea, como el título, la descripción,
# completada, etc.

# Establecer una conexión a la base de datos utilizando el módulo "conexion"
# que has creado.

# Utilizar una sentencia SQL INSERT para insertar la nueva tarea en la tabla 
# correspondiente de la base de datos.

# Ejecutar la sentencia SQL utilizando el cursor de la conexión.

# Confirmar los cambios realizados en la base de datos utilizando el método
# "commit" de la conexión.

# Cerrar la conexión.