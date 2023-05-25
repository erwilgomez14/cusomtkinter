import customtkinter
import tkinter as tk
import os
from PIL import Image
from pymongo import MongoClient

class ItemsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='lightgray')

        # Cargar imágenes
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))

        # Título y botones superiores
        self.item_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.item_frame.grid_columnconfigure(0, weight=10)

        self.create_item_button = customtkinter.CTkButton(self, text="Crear ítem")
        self.create_item_button.grid(row=0, column=0, padx=10, pady=20)

        self.show_items_button = customtkinter.CTkButton(self, text="Mostrar ítems", compound="right")
        self.show_items_button.grid(row=0, column=1, padx=10, pady=20)

        # Etiquetas y campos de entrada
        self.label_nombre = customtkinter.CTkLabel(self, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=20, pady=10)

        self.entry_nombre = customtkinter.CTkEntry(self)
        self.entry_nombre.grid(row=1, column=1, padx=20, pady=10)

        self.label_precio = customtkinter.CTkLabel(self, text="Precio:")
        self.label_precio.grid(row=2, column=0, padx=20, pady=10)

        self.entry_precio = customtkinter.CTkEntry(self)
        self.entry_precio.grid(row=2, column=1, padx=20, pady=10)

        # Botón de guardar
        self.button_guardar = customtkinter.CTkButton(self, text="Guardar", command=self.guardar_item)
        self.button_guardar.grid(row=4, column=1, columnspan=2, pady=10, sticky="nsew")

        # Configuración del pack del widget principal
        self.grid(row=0, column=0, sticky="nsew")

    def guardar_item(self):
        # Obtener los valores de los campos de entrada
        nombre = self.entry_nombre.get()
        precio = float(self.entry_precio.get())

        # Crear conexión con la base de datos MongoDB
        client = MongoClient('mongodb+srv://spynter:3WkWIELVSzicnuDe@cluster0.la6e0.mongodb.net/MakiSushi')
        db = client['MakiSushi']
        collection = db['Items']

        # Crear documento del ítem
        item = {
            'nombre': nombre,
            'precio': precio
        }

        # Insertar el documento en la colección
        collection.insert_one(item)

        # Cerrar la conexión con MongoDB
        client.close()

        # Imprimir mensaje de éxito
        print("Ítem guardado correctamente en MongoDB.")
        # Imprimir los valores
        print(f"nombre: {nombre}")
        print(f"precio: {precio}")

        # Borrar los campos de entrada
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)


