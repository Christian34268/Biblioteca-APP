

from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicios import BibliotecaServicio


def mostrar_menu():
   #Muestra el menú principal del sistema
    print("\n" + "="*50)
    print("       SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("="*50)
    print("1. Agregar libro al inventario")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro por ISBN")
    print("6. Listar libros disponibles")
    print("7. Ver estadísticas")
    print("8. Salir")
    print("="*50)


def agregar_libro(biblioteca):
    """Función para agregar libros al inventario"""
    print("\n--- AGREGAR LIBRO ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoría: ")
    isbn = input("ISBN: ")

    libro = Libro(titulo, autor, categoria, isbn)
    biblioteca.agregar_libro(libro)


def registrar_usuario(biblioteca):
    """Función para registrar nuevos usuarios"""
    print("\n--- REGISTRAR USUARIO ---")
    nombre = input("Nombre completo: ")
    id_usuario = input("ID de usuario: ")

    usuario = Usuario(nombre, id_usuario)
    biblioteca.registrar_usuario(usuario)


def prestar_libro(biblioteca):
    """Función para gestionar préstamos"""
    print("\n--- PRESTAR LIBRO ---")
    isbn = input("ISBN del libro: ")
    id_usuario = input("ID del usuario: ")

    biblioteca.prestar_libro(isbn, id_usuario)


def devolver_libro(biblioteca):
    """Función para gestionar devoluciones"""
    print("\n--- DEVOLVER LIBRO ---")
    isbn = input("ISBN del libro: ")
    id_usuario = input("ID del usuario: ")

    biblioteca.devolver_libro(isbn, id_usuario)


def buscar_libro(biblioteca):
    """Función para buscar libros por ISBN (O(1))"""
    print("\n--- BUSCAR LIBRO ---")
    isbn = input("ISBN a buscar: ")

    libro = biblioteca.buscar_libro(isbn)
    if libro:
        print(f"\n✓ Libro encontrado:")
        print(f"  {libro}")
    else:
        print(f"\n✗ Libro con ISBN {isbn} no encontrado")


def listar_libros(biblioteca):
    """Función para listar todos los libros disponibles"""
    print("\n--- LIBROS DISPONIBLES ---")
    libros = biblioteca.listar_todos_los_libros()

    if libros:
        for i, libro in enumerate(libros, 1):
            print(f"  {i}. {libro}")
    else:
        print("  No hay libros disponibles")


def ver_estadisticas(biblioteca):
    """Función para mostrar estadísticas del sistema"""
    print("\n--- ESTADÍSTICAS ---")
    print(f"  Libros disponibles: {biblioteca.cantidad_libros_disponibles()}")
    print(f"  Usuarios registrados: {biblioteca.cantidad_usuarios_registrados()}")
    print(f"  {biblioteca}")


def main():
    """Función principal del programa"""
    print("\n" + "="*50)
    print("   SISTEMA DE BIBLIOTECA DIGITAL - POO")
    print("   Arquitectura por Capas")
    print("="*50)

    # Inicializar el servicio de biblioteca
    biblioteca = BibliotecaServicio()

    # Menú interactivo
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-8): ").strip()

        try:
            if opcion == "1":
                agregar_libro(biblioteca)
            elif opcion == "2":
                registrar_usuario(biblioteca)
            elif opcion == "3":
                prestar_libro(biblioteca)
            elif opcion == "4":
                devolver_libro(biblioteca)
            elif opcion == "5":
                buscar_libro(biblioteca)
            elif opcion == "6":
                listar_libros(biblioteca)
            elif opcion == "7":
                ver_estadisticas(biblioteca)
            elif opcion == "8":
                print("\n✓ Gracias por usar el Sistema de Gestión de Biblioteca")
                print("  ¡Hasta pronto!\n")
                break
            else:
                print("\n✗ Opción no válida. Intente nuevamente.")
        except KeyboardInterrupt:
            print("\n\n✗ Operación cancelada por el usuario")
        except Exception as e:
            print(f"\n✗ Error: {e}")


if __name__ == "__main__":
    main()