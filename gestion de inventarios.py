import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        productos = {}
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        codigo, nombre, cantidad = linea.strip().split(',')
                        productos[codigo] = {'nombre': nombre, 'cantidad': int(cantidad)}
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al cargar el inventario: {e}")
        return productos

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for codigo, info in self.productos.items():
                    file.write(f"{codigo},{info['nombre']},{info['cantidad']}\n")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, codigo, nombre, cantidad):
        self.productos[codigo] = {'nombre': nombre, 'cantidad': cantidad}
        self.guardar_inventario()
        print(f"Producto {nombre} añadido exitosamente.")

    def actualizar_producto(self, codigo, nombre=None, cantidad=None):
        if codigo in self.productos:
            if nombre is not None:
                self.productos[codigo]['nombre'] = nombre
            if cantidad is not None:
                self.productos[codigo]['cantidad'] = cantidad
            self.guardar_inventario()
            print(f"Producto {codigo} actualizado exitosamente.")
        else:
            print("El producto no existe.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print(f"Producto {codigo} eliminado exitosamente.")
        else:
            print("El producto no existe.")

def main():
    inventario = Inventario()

    # Añadir productos
    inventario.añadir_producto('001', 'Producto A', 10)
    inventario.añadir_producto('002', 'Producto B', 5)

    # Actualizar producto
    inventario.actualizar_producto('001', cantidad=15)

    # Eliminar producto
    inventario.eliminar_producto('002')

if __name__ == "__main__":
    main()

