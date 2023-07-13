class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.prestado = False

    def prestar(self):
        if self.prestado:
            print("El libro ya está prestado.")
        else:
            self.prestado = True
            print("Libro prestado con éxito.")

    def devolver(self):
        if not self.prestado:
            print("El libro no está prestado.")
        else:
            self.prestado = False
            print("Libro devuelto correctamente.")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print("Lista de libros:")
        for libro in self.libros:
            print(f"Título: {libro.titulo} | Autor: {libro.autor} | Género: {libro.genero}")


# Creación de instancias de libros
libro1 = Libro("1984", "George Orwell", "Ciencia ficción")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela")
libro3 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía")

# Creación de instancia de biblioteca
biblioteca = Biblioteca()

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Mostrar la lista de libros en la biblioteca
biblioteca.mostrar_libros()

# Prestar un libro
libro1.prestar()

# Intentar prestar un libro ya prestado
libro1.prestar()

# Devolver un libro
libro1.devolver()

# Mostrar la lista de libros actualizada
biblioteca.mostrar_libros()
