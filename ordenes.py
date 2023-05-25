import customtkinter
import tkinter as tk
import os
from PIL import Image
from pymongo import MongoClient

class OrdenesVentaView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='lightgray')

        # Cargar imágenes
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))

        # Título y botones superiores
        self.orden_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.orden_frame.grid_columnconfigure(0, weight=10)

        self.create_orden_button = customtkinter.CTkButton(self, text="Crear orden")
        self.create_orden_button.grid(row=0, column=0, padx=10, pady=20)

        self.show_ordenes_button = customtkinter.CTkButton(self, text="Mostrar órdenes", compound="right")
        self.show_ordenes_button.grid(row=0, column=1, padx=10, pady=20)

        # Etiquetas y campos de entrada
        self.label_cliente = customtkinter.CTkLabel(self, text="Cliente:")
        self.label_cliente.grid(row=1, column=0, padx=20, pady=10)

        self.entry_cliente = customtkinter.CTkEntry(self)
        self.entry_cliente.grid(row=1, column=1, padx=20, pady=10)

        self.label_producto = customtkinter.CTkLabel(self, text="Producto:")
        self.label_producto.grid(row=2, column=0, padx=20, pady=10)

        self.entry_producto = customtkinter.CTkEntry(self)
        self.entry_producto.grid(row=2, column=1, padx=20, pady=10)

        self.label_cantidad = customtkinter.CTkLabel(self, text="Cantidad:")
        self.label_cantidad.grid(row=3, column=0, padx=20, pady=10)

        self.entry_cantidad = customtkinter.CTkEntry(self)
        self.entry_cantidad.grid(row=3, column=1, padx=20, pady=10)

        # Botón de guardar
        self.button_guardar = customtkinter.CTkButton(self, text="Guardar", command=self.guardar_orden)
        self.button_guardar.grid(row=5, column=1, columnspan=2, pady=10, sticky="nsew")

        # Configuración del pack del widget principal
        self.grid(row=0, column=0, sticky="nsew")

    def guardar_orden(self):
        # Obtener los valores de los campos de entrada
        cliente = self.entry_cliente.get()
        producto = self.entry_producto.get()
        cantidad = int(self.entry_cantidad.get())

        # Crear conexión con la base de datos MongoDB
        client = MongoClient('mongodb+srv://spynter:3WkWIELVSzicnuDe@cluster0.la6e0.mongodb.net/MakiSushi')
        db = client['MakiSushi']
        collection = db['OrdenesVenta']

        # Crear documento de la orden de venta
        orden = {
            'cliente': cliente,
            'producto': producto,
            'cantidad': cantidad
        }

        # Insertar el documento en la colección
        collection.insert_one(orden)

        # Cerrar la conexión con MongoDB
        client.close()

        # Imprimir mensaje de éxito
        print("Orden de venta guardada correctamente en MongoDB.")
        # Imprimir los valores
        print(f"Cliente: {cliente}")
        print(f"Producto: {producto}")
        print(f"Cantidad: {cantidad}")

        # Borrar los campos de entrada
        self.entry_cliente.delete(0, tk.END)
        self.entry_producto.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
