import customtkinter
import tkinter as tk
from tkinter import ttk
import os
from PIL import Image
from pymongo import MongoClient

class UsuariosView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg='lightgray')

        #cargar imagenes
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))

        #titulo y botones superiores
        #self.label_titulo = customtkinter.CTkLabel(self, text="Sección Usuarios")
        #self.label_titulo.grid(row=0, column=0)

        self.usuario_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.usuario_frame.grid_columnconfigure(0, weight=10)

        #self.usuario_frame_large_image_label = customtkinter.CTkLabel(self, text="", image=self.large_test_image)
        #self.usuario_frame_large_image_label.grid(row=0, column=0, padx=20, pady=0)


        self.second_frame_button_1 = customtkinter.CTkButton(self, text="crear usuario")
        self.second_frame_button_1.grid(row=0, column=0, padx=10, pady=20)

        self.second_frame_button_2 = customtkinter.CTkButton(self, text="mostrar usuarios", compound="right", command=self.mostrar_usuarios)
        self.second_frame_button_2.grid(row=0, column=1, padx=10, pady=20)

        
        # Etiquetas y campos de entrada
        self.label_correo = customtkinter.CTkLabel(self, text="Correo:")
        self.label_correo.grid(row=1, column=0, padx=20, pady=10)
        
        self.entry_correo = customtkinter.CTkEntry(self)
        self.entry_correo.grid(row=1, column=1, padx=20, pady=10)
        
        self.label_nombre = customtkinter.CTkLabel(self, text="Nombre:")
        self.label_nombre.grid(row=2, column=0, padx=20, pady=10)
        
        self.entry_nombre = customtkinter.CTkEntry(self)
        self.entry_nombre.grid(row=2, column=1, padx=20, pady=10)

        self.label_contraseña = customtkinter.CTkLabel(self, text="Contraseña:")
        self.label_contraseña.grid(row=3, column=0, padx=20, pady=10)
        
        self.entry_contraseña = customtkinter.CTkEntry(self)
        self.entry_contraseña.grid(row=3, column=1, padx=20, pady=10)
        
        # Botón de guardar
        self.button_guardar = customtkinter.CTkButton(self, text="Guardar", command=self.guardar_usuario)
        self.button_guardar.grid(row=5, column=1, columnspan=2, pady=10, sticky="nsew")

        # Tabla de usuarios
        self.table = ttk.Treeview(self, columns=("correo", "nombre", "contraseña"), show="headings")
        self.table.heading("correo", text="Correo")
        self.table.heading("nombre", text="Nombre")
        self.table.heading("contraseña", text="Contraseña")
        self.table.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

         # Configuración del pack del widget principal
        self.grid(row=0, column=0, sticky="nsew")

        
    def guardar_usuario(self):
        # Aquí puedes agregar la lógica para guardar los datos del inventario en tu base de datos
        correo = self.entry_correo.get()
        nombre = self.entry_nombre.get()
        contraseña = self.entry_contraseña.get()
         # Crear conexión con la base de datos MongoDB
        client = MongoClient('mongodb+srv://spynter:3WkWIELVSzicnuDe@cluster0.la6e0.mongodb.net/MakiSushi')
        db = client['MakiSushi']
        collection = db['Usuarios']
        
        # Crear documento del cliente
        cliente = {
            'correo': correo,
            'nombre': nombre,
            'contraseña': contraseña
        }
        
        # Insertar el documento en la colección
        collection.insert_one(cliente)
        
        # Cerrar la conexión con MongoDB
        client.close()
        
        # Imprimir mensaje de éxito
        print("inventario guardado correctamente en MongoDB.")
        # Obtener los valores de los campos de entrada

        # Imprimir los valores
        print(f"correo: {correo}")
        print(f"nombre: {nombre}")
        print(f"contraseña: {contraseña}")
        
        # Borrar los campos de entrada
        self.entry_correo.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_contraseña.delete(0, tk.END)
        
    def mostrar_usuarios(self):
        # Limpiar tabla
        self.table.delete(*self.table.get_children())

        # Conectar a la base de datos y obtener la colección de usuarios
        client = MongoClient('mongodb+srv://spynter:3WkWIELVSzicnuDe@cluster0.la6e0.mongodb.net/MakiSushi')
        db = client['MakiSushi']
        collection = db['Usuarios']

        # Obtener todos los documentos de la colección
        usuarios = collection.find()

        # Mostrar los usuarios en la tabla
        for usuario in usuarios:
            correo = usuario.get('correo', '')
            nombre = usuario.get('nombre', '')
            contraseña = usuario.get('contraseña', '')
            self.table.insert("", tk.END, values=(correo, nombre, contraseña))

        # Cerrar la conexión con MongoDB
        client.close()