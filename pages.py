dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))

if divisor != 0:
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)
else:
    print("Error: No se puede dividir entre cero.")





edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales en COP: "))

if edad > 16 and ingresos >= 4000000:
    print("Debe tributar.")
else:
    print("No debe tributar.")




puntuacion = float(input("Ingrese la puntuación obtenida: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = "Puntuación inválida"

if nivel != "Puntuación inválida":
    bonificacion = 2400 * puntuacion
    print("Nivel de rendimiento:", nivel)
    print("Cantidad de dinero a recibir:", bonificacion, "€")
else:
    print("Puntuación inválida. Intente nuevamente.")




edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5000
else:
    precio = 10000

print("El precio de la entrada es:", precio, "COP")




es_vegetariana = input("¿Desea una pizza vegetariana? (s/n): ")

if es_vegetariana == "s":
    print("Ingredientes disponibles: Pimiento, Tofu")
    ingrediente = input("Elija un ingrediente adicional: ")
    pizza = "Vegetariana"
else:
    print("Ingredientes disponibles: Pepperoni, Jamón, Salmón")
    ingrediente = input("Elija un ingrediente adicional: ")
    pizza = "No vegetariana"

print("La pizza elegida es:", pizza)
print("Ingredientes:", "Mozzarella, Tomate,", ingrediente)
