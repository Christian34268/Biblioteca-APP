class Libro:   #Esta Funcion Representa un libro denttro del sistema de la biblioteca 
    
    def __init__(self, titulo, autor, categoria, isbn):
        # Se aplica la colección de Tuplas para almacenar los datos del libro, estos iran datos inmutables.   
        self.informacion_inicial = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    #-------------------------------------
    #   Método de Acceso
    #-------------------------------------
    
    def obtener_titulo(self):
        return self.informacion_inicial[0] # Se obtiene el titulo a través de el
    
    def obtener_autor(self):
        return self.informacion_inicial[1]# Se obtiene el autor a traves de el 
    
    def obtener_informacion(self):
        return self.informacion_inicial # Se obtiene toda la información a través de l tupla completa 
    
    #-------------------------------------
    #   Método de Representación
    #-------------------------------------

    def __str__(self):
        titulo, autor = self.informacion_inicial
        return f"'{titulo}' por {autor} | ISBN: {self.isbn} | Categoría: {self.categoria}"


if __name__ == "__main__":

    libro1 = Libro(
        titulo="1984",
        autor="George Orwell",
        categoria="Ciencia Ficción",
        isbn = "1984 9786586064537"
    )
    # Acceder a datos
    print(libro1)
    print(f"Título: {libro1.obtener_titulo()}")
    print(f"Autor: {libro1.obtener_autor()}")
    print(f"Información Inicial (tupla): {libro1.obtener_informacion()}")
    
    # Intentar modificar la tupla (generará error)
    try:
        libro1.informacion_inicial[0] = "Nuevo Título"
    except TypeError as e:
        print(f"\nError esperado: {e}")
        print("✓ La tupla es inmutable (seguridad de datos)")
