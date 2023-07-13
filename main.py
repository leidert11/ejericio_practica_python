#ejercicio calculadora

# from calculadora.operaciones import suma, restar, multi, dividir

# resultado_suma = suma()
# print(f"Resultado de la suma: {resultado_suma}")

# resultado_resta = restar()
# print(f"Resultado de la resta: {resultado_resta}")

# resultado_multi = multi()
# print(f"Resultado de la multiplicacion: {resultado_multi}")

# resultado_dividir = dividir()
# print(f"Resultado de la division: {resultado_dividir}")


#----------------------------------------------------------------

#ejercicio traductor de ingles a español

# import os
# # print(os.getcwd())   Imprime el directorio de trabajo actual
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Usuario\OneDrive\Documentos\ejercicios_python\traductor\translate-390205-d67127cea639.json"

# from traductor.translator import traducir_ingles_a_espanol

# frase_ingles = input("Ingresa una frase en inglés: ")
# traduccion_espanol = traducir_ingles_a_espanol(frase_ingles)

# print(f"Traducción al español:  {traduccion_espanol}")

#----------------------------------------------------------------

#manipulador de archivos txt

# from manejador_archivos import lector_archivos

# contenido = lector_archivos.leer_archivo()

# if contenido:
#     print("Contenido del archivo:")
#     print(contenido)

# texto_anexar = input("Ingresa el texto a anexar al archivo: ")
# lector_archivos.anexar_archivo(texto_anexar)


#----------------------------------------------------------------


#crud de tareas con MySQL

# from gestor_tareas.crear_tarea import crear_tarea
# from gestor_tareas.leer_tarea import leer_tarea
# from gestor_tareas.actualizar_tarea import actualizar_tarea
# from gestor_tareas.eliminar_tarea import eliminar_tarea

# Crear una tarea
# crear_tarea("aguanta", "aguantar a la mamona.", True)

# Leer una tarea
# leer_tarea(2)

# Actualizar una tarea
# actualizar_tarea(1, "mamona 1", "mamona 1", True)

# Eliminar una tarea
# eliminar_tarea(2)
