class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Usamos una tupla para el título y el autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[0]} por {self.datos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y libro como valor
        self.usuarios_registrados = set()  # Conjunto de IDs de usuarios únicos
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
        else:
            print("Este ID de usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.usuarios[id_usuario]
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles[isbn]
            usuario.prestar_libro(libro)
            del self.libros_disponibles[isbn]
        else:
            print("Usuario o libro no disponible.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(libro)
                    self.libros_disponibles[isbn] = libro
                    break
            else:
                print("El libro no está prestado por este usuario.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self, filtro, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if filtro == 'titulo' and valor in libro.datos[0]:
                resultados.append(libro)
            elif filtro == 'autor' and valor in libro.datos[1]:
                resultados.append(libro)
            elif filtro == 'categoria' and valor == libro.categoria:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            return None


# Ejemplo de uso
# Crear algunos libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "123456789")
libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "987654321")

# Crear la biblioteca
biblioteca = Biblioteca()

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar un usuario
usuario1 = Usuario("Juan Pérez", 1)
biblioteca.registrar_usuario(usuario1)

# Prestar un libro
biblioteca.prestar_libro(1, "123456789")

# Listar los libros prestados por el usuario
prestados = biblioteca.listar_libros_prestados(1)
for libro in prestados:
    print(libro)

# Devolver un libro
biblioteca.devolver_libro(1, "123456789")

# Buscar un libro por título
resultados_busqueda = biblioteca.buscar_libro("titulo", "Quijote")
for libro in resultados_busqueda:
    print(libro)
