import tkinter as tk
import bd

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Registro de Usuarios")
        
        # Variables para almacenar los datos ingresados
        self.nombre = tk.StringVar()
        self.correo = tk.StringVar()
        self.contraseña = tk.StringVar()
        
        # Crear los elementos de la interfaz de usuario
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.pack()
        
        self.label_correo = tk.Label(self, text="Correo:")
        self.label_correo.pack()
        self.entry_correo = tk.Entry(self, textvariable=self.correo)
        self.entry_correo.pack()
        
        self.label_contraseña = tk.Label(self, text="Contraseña:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(self, textvariable=self.contraseña, show="*")
        self.entry_contraseña.pack()
        
        self.button_guardar = tk.Button(self, text="Guardar", command=self.guardar_usuario)
        self.button_guardar.pack()
        
    def guardar_usuario(self):
        nombre = self.nombre.get()
        correo = self.correo.get()
        contraseña = self.contraseña.get()
        
        # Guardar en la base de datos
        bd.guardar_usuario(nombre, correo, contraseña)
        
        # Limpiar los campos de entrada
        self.nombre.set("")
        self.correo.set("")
        self.contraseña.set("")

if __name__ == "__main__":
    app = App()
    app.mainloop()