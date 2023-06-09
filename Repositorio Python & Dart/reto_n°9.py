class Pila:
    def __init__(self):
        self.pila = []
        
    def apilar(self, libro):
        self.pila.append(libro)
        
    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return None
    
    def esta_vacia(self):
        return len(self.pila) == 0
    

def apilar_libros():
    pila = Pila()
    continuar = True
    
    while continuar:
        titulo = input("Ingrese el título del libro (o 'salir' para terminar): ")
        
        if titulo.lower() == "salir":
            continuar = False
        else:
            pila.apilar(titulo)
            
    return pila


def desapilar_libros(pila):
    while not pila.esta_vacia():
        libro = pila.desapilar()
        print("Se sacó el libro:", libro)

pila_libros = apilar_libros()
print("\n--- Sacando libros de la pila ---")
desapilar_libros(pila_libros)