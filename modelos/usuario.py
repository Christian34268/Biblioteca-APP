class Usuario:
    """Representa a un usuario registrado en la biblioteca"""
    
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista mutable para libros prestados (datos dinámicos)
        self.libros_prestados = []
    
    def prestar_libro(self, libro):
        """Agrega un libro a la lista de préstamos"""
        self.libros_prestados.append(libro)
        print(f"✓ Libro '{libro.obtener_titulo()}' prestado a {self.nombre}")
    
    def devolver_libro(self, isbn):
        """Elimina un libro de la lista de préstamos por su ISBN"""
        for i, libro in enumerate(self.libros_prestados):
            if libro.isbn == isbn:
                libro_devuelto = self.libros_prestados.pop(i)
                print(f"✓ Libro '{libro_devuelto.obtener_titulo()}' devuelto por {self.nombre}")
                return True
        print(f"✗ Libro con ISBN {isbn} no encontrado")
        return False
    
    def obtener_libros_prestados(self):
        """Retorna la lista completa de libros prestados"""
        return self.libros_prestados
    
    def cantidad_libros_prestados(self):
        """Retorna el número de libros actualmente prestados"""
        return len(self.libros_prestados)
    
    def tiene_prestamos(self):
        """Verifica si el usuario tiene libros prestados"""
        return len(self.libros_prestados) > 0
    
    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario} | Libros prestados: {self.cantidad_libros_prestados()}"


# EJEMPLO DE USO
if __name__ == "__main__":
    # Importar clase Libro
    from modelos.libro import Libro
    
    # Crear usuario
    usuario1 = Usuario("Carlos Rodríguez", "U001")
    
    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 
                   "Realismo Mágico", "978-0307474728")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 
                   "Literatura Infantil", "978-0156012195")
    
    # Realizar préstamos
    print(usuario1)
    usuario1.prestar_libro(libro1)
    usuario1.prestar_libro(libro2)
    print(usuario1)
    
    # Consultar libros prestados
    print(f"\nLibros prestados:")
    for libro in usuario1.obtener_libros_prestados():
        print(f"  - {libro}")
    
    # Devolver un libro
    print("\nDevolviendo libro...")
    usuario1.devolver_libro("978-0307474728")
    print(usuario1)