from gestor_tareas.conexion import establecer_conexion

def eliminar_tarea(id_tarea):
    conexion= establecer_conexion()
    
    try:
        cursor=conexion.cursor()
        query= "DELETE FROM tareas WHERE id = %s"
        valores= (id_tarea,)
        cursor.execute(query, valores)
        
        conexion.commit()
        cursor.close()
        
        print("tarea eliminada exitosamente")
    except Exception as e:
        print(f"error al eliminar la tarea : {e}")
    finally:
        conexion.close()
    
    

# Crear una función llamada "eliminar_tarea" que tome un parámetro para identificar 
# la tarea a eliminar, como un identificador único de tarea.

# Establecer una conexión a la base de datos utilizando el módulo "conexion".

# Utilizar una sentencia SQL DELETE para eliminar la tarea de la base de datos.

# Ejecutar la sentencia SQL utilizando el cursor de la conexión.

# Confirmar los cambios realizados en la base de datos utilizando el método "commit" 
# de la conexión.

# Cerrar la conexión