from google.cloud import translate_v2 as translate

def traducir_ingles_a_espanol(frase):
    # Crea una instancia del cliente de traducción
    cliente = translate.Client()

    # Configura los parámetros de traducción
    contenido = [frase]
    target_language = "es"

    # Realiza la traducción
    respuesta = cliente.translate(
        contenido,
        target_language=target_language
    )

    # Obtiene y devuelve la traducción
    traduccion = respuesta[0]['translatedText']
    return traduccion