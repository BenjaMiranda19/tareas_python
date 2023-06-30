class Nodo:
    def __init__(self, titulo, autor, duracion):
        self.titulo = titulo
        self.autor = autor
        self.duracion = duracion
        self.siguiente = None
        self.anterior = None

class ListaReproduccionVideo:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def esta_vacia(self):
        return self.primero is None
    
    def agregar_video(self, titulo, autor, duracion):
        nuevo_video = Nodo(titulo, autor, duracion)
        if self.esta_vacia():
            self.primero = nuevo_video
            self.ultimo = nuevo_video

        else:
            nuevo_video.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_video
            self.ultimo = nuevo_video

    def eliminar_video(self, titulo):
        actual = self.primero
        while actual is not None:
            if actual.titulo == titulo:
                #if actual.anterior is not None: (Error: al dejarlo como "is not None" me elimina todos
                # los titulos anteriores al que yo solicito mas el que quiero y me deja solo los que siguen)
                if actual.anterior is None:
                    self.primero = actual.siguiente
                    if self.primero is not None:
                        self.primero.anterior = None

                else:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente is not None:
                        actual.siguiente.anterior = actual.anterior
                
                if actual == self.ultimo:
                    self.ultimo = self.anterior

                break
            
            actual = actual.siguiente
        
    def mostrar_ListaVideo(self):
        actual = self.primero
        while actual is not None:
            print(f"Titulo: {actual.titulo}, Autor: {actual.autor}, Duracion: {actual.duracion}")
            actual = actual.siguiente


listareproduccionvideo = ListaReproduccionVideo()

#Ejemplo de uso:

listareproduccionvideo.agregar_video("Una noche en Medellín", "Cris Mj", "2:34 minutos")
listareproduccionvideo.agregar_video("Primer dia de clases", "Mora", "2:27 minutos")
listareproduccionvideo.agregar_video("Algún dia volverás", "Santaferia", "4:14 minutos")
listareproduccionvideo.agregar_video("Ella baila sola", "Eslabon aramado, Peso pluma", "2:46 minutos")

listareproduccionvideo.mostrar_ListaVideo()

listareproduccionvideo.eliminar_video("Algún dia volverás") #Aqui me imprimio varias veces la misma lista por no poner el tilde en la u y en la a
print()
print("Nueva lista")
print()
listareproduccionvideo.mostrar_ListaVideo()