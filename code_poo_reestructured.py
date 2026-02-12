#Clase
class Libro:
    # El constructor
    def __init__(self, titulo, autor, isbn):
        # self es la referencia al objeto que se está creando
        self.titulo = titulo   
        self.autor = autor     
        self.isbn = isbn       # La "cédula" única del libro
        self.disponible = True 

    # Metodo =  Lo que se puede hacer con el libro 
    def prestar(self):
        # El libro revisa su propio estado
        if self.disponible:
            self.disponible = False # Cambia a ocupado
            return True             # Si se puede prestar
        return False                # En caso de que no este disponible

#Clase
class Biblioteca:
    def __init__(self):
        # Lista de objetos de tipo Libro
        self.libros = []

    # Metodo para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)
        return "Libro agregado"

    # Metodo
    def realizar_prestamo(self, isbn, id_usuario):
        # Ciclo for
        for libro in self.libros:
            # CComparación
            if libro.isbn == isbn:
                # Si esta el isbn ejecutamos el metodo prestar del libro encontrado
                if libro.prestar():
                    return "Prestamo exitoso"
                #Si el falso, retorna el mensaje
                return "Libro no disponible"
        # Si no existe
        return "Libro no encontrado"


# Objeto de la clase Biblioteca
mi_biblioteca = Biblioteca()

#Llenamos los datos del libro a traves del constructor de la clase Libro
nuevo_libro = Libro("1984", "Orwell", "123")



# Agregamos el libro a la biblioteca usando el metodo agregar_libro, que recibe un objeto de tipo Libro
print(mi_biblioteca.agregar_libro(nuevo_libro))

#ejecutamos el metodo realizar_prestamo, que recibe el isbn y el id del usuario, y retorna un mensaje dependiendo del resultado del prestamo
print(mi_biblioteca.realizar_prestamo("123", 1))