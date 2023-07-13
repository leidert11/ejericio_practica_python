from gestor_tareas.conexion import establecer_conexion
from gestor_tareas.leer_tarea import leer_tarea

def actualizar_tarea(id_tarea, titulo, descripcion, completada):
    conexion = establecer_conexion()

    try:
        tarea_actual = leer_tarea(id_tarea)  # Leer la tarea actual para comparar con los nuevos valores

        # Validar si los nuevos valores son iguales a los valores actuales de la tarea
        if tarea_actual["titulo"] == titulo and tarea_actual["descripcion"] == descripcion and tarea_actual["completada"] == completada:
            print("La tarea ya contiene los mismos valores que se desean ingresar.")
            return

        cursor = conexion.cursor()
        query = "UPDATE tareas SET titulo = %s, descripcion = %s, completada = %s WHERE id = %s"
        valores = (titulo, descripcion, completada, id_tarea)
        cursor.execute(query, valores)

        conexion.commit()
        cursor.close()

        if cursor.rowcount > 0:
            print("La tarea se ha actualizado correctamente.")
            leer_tarea(id_tarea)
        else:
            print("No se encontró ninguna tarea con el ID proporcionado.")
    except Exception as e:
        print(f"Error al actualizar la tarea: {e}")
    finally:
        conexion.close()



# Crear una función llamada "actualizar_tarea" que tome los parámetros necesarios 
# para identificar la tarea a actualizar, así como los nuevos valores para los 
# atributos de la tarea.

# Establecer una conexión a la base de datos utilizando el módulo "conexion".

# Utilizar una sentencia SQL UPDATE para actualizar los valores de la tarea
# en la base de datos.

# Ejecutar la sentencia SQL utilizando el cursor de la conexión.

# Confirmar los cambios realizados en la base de datos utilizando
# el método "commit" de la conexión.

# Cerrar la conexión.