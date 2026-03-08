from modelos.libro import Libro 
from modelos.usuario import Usuario

class BibliotecaServicio:
    """Gestiona la lógica del sistema de biblioteca"""
    
    def __init__(self):
        # Diccionario: Clave=ISBN, Valor=Libro (Búsqueda O(1))
        self.libros_disponibles = {}
        
        # Conjunto: IDs únicos de usuarios (Unicidad automática)
        self.ids_usuarios_registrados = set()
        
        # Diccionario: Clave=ID_Usuario, Valor=Usuario
        self.usuarios_registrados = {}
    
    # ========== GESTIÓN DE LIBROS ==========
    
    def agregar_libro(self, libro):
        """Agrega un libro al inventario usando diccionario"""
        isbn = libro.isbn
        self.libros_disponibles[isbn] = libro
        print(f"✓ Libro '{libro.obtener_titulo()}' agregado al inventario")
    
    def buscar_libro(self, isbn):
        """Busca un libro por ISBN (O(1) con diccionario)"""
        return self.libros_disponibles.get(isbn)
    
    def eliminar_libro(self, isbn):
        """Elimina un libro del inventario"""
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"✓ Libro '{libro.obtener_titulo()}' eliminado")
            return True
        print(f"✗ Libro con ISBN {isbn} no encontrado")
        return False
    
    # ========== GESTIÓN DE USUARIOS ==========
    
    def registrar_usuario(self, usuario):
        """Registra un usuario usando conjunto para IDs únicos"""
        id_usuario = usuario.id_usuario
        
        if id_usuario in self.ids_usuarios_registrados:
            print(f"✗ El ID {id_usuario} ya está registrado")
            return False
        
        self.ids_usuarios_registrados.add(id_usuario)
        self.usuarios_registrados[id_usuario] = usuario
        print(f"✓ Usuario '{usuario.nombre}' registrado exitosamente")
        return True
    
    def buscar_usuario(self, id_usuario):
        """Busca un usuario por ID (O(1) con diccionario)"""
        return self.usuarios_registrados.get(id_usuario)
    
    # ========== PRÉSTAMOS Y DEVOLUCIONES ==========
    
    def prestar_libro(self, isbn_libro, id_usuario):
        """Gestiona el préstamo de un libro (Búsquedas O(1))"""
        libro = self.buscar_libro(isbn_libro)
        if not libro:
            print(f"✗ Libro con ISBN {isbn_libro} no disponible")
            return False
        
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            print(f"✗ Usuario con ID {id_usuario} no registrado")
            return False
        
        usuario.prestar_libro(libro)
        self.libros_disponibles.pop(isbn_libro)
        
        print(f"✓ Préstamo exitoso: '{libro.obtener_titulo()}' a {usuario.nombre}")
        return True
    
    def devolver_libro(self, isbn_libro, id_usuario):
        """Gestiona la devolución de un libro"""
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            print(f"✗ Usuario con ID {id_usuario} no encontrado")
            return False
        
        if usuario.devolver_libro(isbn_libro):
            # Obtener el libro del historial del usuario para re-agregarlo
            libros_usuario = usuario.obtener_libros_prestados()
            # Buscar el libro que se acaba de devolver en los libros del usuario
            for libro in libros_usuario:
                if libro.isbn == isbn_libro:
                    self.libros_disponibles[isbn_libro] = libro
                    print(f"✓ Libro ISBN {isbn_libro} devuelto y disponible")
                    return True
            print(f"✓ Libro ISBN {isbn_libro} devuelto")
            return True
        
        return False
    
    # ========== CONSULTAS Y ESTADÍSTICAS ==========
    
    def cantidad_libros_disponibles(self):
        """Retorna el número total de libros disponibles"""
        return len(self.libros_disponibles)
    
    def cantidad_usuarios_registrados(self):
        """Retorna el número total de usuarios registrados"""
        return len(self.ids_usuarios_registrados)
    
    def listar_todos_los_libros(self):
        """Retorna una lista con todos los libros disponibles"""
        return list(self.libros_disponibles.values())
    
    def usuario_tiene_prestamos(self, id_usuario):
        """Verifica si un usuario tiene libros prestados"""
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            return usuario.tiene_prestamos()
        return False
    
    def __str__(self):
        """Representación del estado de la biblioteca"""
        return f"Biblioteca: {self.cantidad_libros_disponibles()} libros disponibles | {self.cantidad_usuarios_registrados()} usuarios registrados"


# ========== EJEMPLO DE USO ==========
if __name__ == "__main__":
    # Crear instancia del servicio
    biblioteca = BibliotecaServicio()
    
    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 
                   "Realismo Mágico", "978-0307474728")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 
                   "Literatura Infantil", "978-0156012195")
    libro3 = Libro("1984", "George Orwell", "Distopía", "978-0451524935")
    
    # Agregar libros al inventario (Diccionario - O(1))
    print("=== AGREGANDO LIBROS ===")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    print(biblioteca)
    
    # Crear y registrar usuarios (Conjunto - Unicidad)
    print("\n=== REGISTRANDO USUARIOS ===")
    usuario1 = Usuario("Carlos Rodríguez", "U001")
    usuario2 = Usuario("Ana Martínez", "U002")
    
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    
    # Intentar registrar ID duplicado (Conjunto lo detecta)
    usuario3 = Usuario("Carlos Duplicate", "U001")
    biblioteca.registrar_usuario(usuario3)
    print(biblioteca)
    
    # Realizar préstamo (Búsquedas O(1))
    print("\n=== REALIZANDO PRÉSTAMO ===")
    biblioteca.prestar_libro("978-0307474728", "U001")
    print(biblioteca)
    
    # Buscar libro por ISBN (O(1) vs O(n))
    print("\n=== BUSCANDO LIBRO ===")
    libro_buscado = biblioteca.buscar_libro("978-0156012195")
    if libro_buscado:
        print(f"Libro encontrado: {libro_buscado}")
    
    # Devolver libro
    print("\n=== DEVOLVIENDO LIBRO ===")
    biblioteca.devolver_libro("978-0307474728", "U001")
    print(biblioteca)