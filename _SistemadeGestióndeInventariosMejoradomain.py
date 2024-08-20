
# inventario.py

from producto import Producto

class Inventario:
    def __init__(self, archivo):
        self.productos = []
        self.archivo = archivo

        # Cargar productos del archivo al iniciar el programa
        self.cargar_inventario()

    def agregar_producto(self, producto):
        self.productos.append(producto)
self.guardar_inventario()

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.obtener_id() != id]
        self.guardar_inventario()

def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.obtener_id() == id:
                if cantidad is not None:
                    p.establecer_cantidad(cantidad)
                if precio is not None:
                    p.establecer_precio(precio)

self.guardar_inventario()

    def guardar_inventario(self):
        with open(self.archivo, 'w') as file:
            for p in self.productos:

file.write(f"{p.obtener_id()},{p.obtener_nombre()},{p.obtener_cantidad()},{p.obtener_precio()}\n")

 def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split(',')
                    producto = Producto(int(id), nombre, int(cantidad), float(precio))

self.productos.append(producto)
        except FileNotFoundError:
            # Crear el archivo si no existe
            open(self.archivo, 'w').close()
        except PermissionError:
            print("Error: Permiso denegado para acceder al archivo de inventario.")
 def mostrar_productos(self):
        for p in self.productos:
            print(f"ID: {p.obtener_id()}, Nombre: {p.obtener_nombre()}, Cantidad: {p.obtener_cantidad()}, Precio: {p.obtener_precio()}")
