class Banco:
    def __init__(self):
        self.clientes = []
        
    def agregar_cliente(self, nombre):
        self.clientes.append(nombre)
        
    def atender_cliente(self):
        if not self.esta_vacio():
            return self.clientes.pop(0)
        else:
            return None
    
    def esta_vacio(self):
        return len(self.clientes) == 0
    

def simulacion_banco():
    banco = Banco()
    continuar = True
    
    while continuar:
        nombre = input("Ingrese el nombre del cliente (o 'salir' para terminar): ")
        
        if nombre.lower() == "salir":
            continuar = False
        else:
            banco.agregar_cliente(nombre)
            
    print("\n--- Atendiendo a los clientes ---")
    
    while not banco.esta_vacio():
        cliente = banco.atender_cliente()
        print("Atendiendo al cliente:", cliente)

simulacion_banco()