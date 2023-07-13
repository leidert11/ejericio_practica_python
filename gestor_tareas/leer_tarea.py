from gestor_tareas.conexion import establecer_conexion

def leer_tarea(id_tarea):
    conexion = establecer_conexion()

    try:
        cursor = conexion.cursor()
        query = "SELECT * FROM tareas WHERE id = %s"
        valores = (id_tarea,)
        cursor.execute(query, valores)

        tarea = cursor.fetchone()

        if tarea:
            tarea_dict = {
                "id": tarea[0],
                "titulo": tarea[1],
                "descripcion": tarea[2],
                "completada": tarea[3]
            }

            return tarea_dict
        else:
            print("No se encontró ninguna tarea con el ID proporcionado.")
            return None
    except Exception as e:
        print(f"Error al leer la tarea: {e}")
        return None
    finally:
        conexion.close()

# Crear una función llamada "leer_tarea" que tome un parámetro para filtrar las
# tareas a leer, como un identificador único de tarea o cualquier otro criterio.

# Establecer una conexión a la base de datos utilizando el módulo "conexion".

# Utilizar una sentencia SQL SELECT para obtener las tareas que cumplan con el 
# criterio especificado.

# Ejecutar la sentencia SQL utilizando el cursor de la conexión.

# Recuperar los resultados de la consulta utilizando métodos como 
# "fetchone" o "fetchall".

# Retornar los resultados obtenidos.

# Cerrar la conexión.