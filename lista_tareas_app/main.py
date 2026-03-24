# main.py
import tkinter as tk
from ui.app_tkinter import VentanaPrincipal

if __name__ == "__main__":
    # Creación de la ventana principal de Tkinter
    root = tk.Tk()
    # Inicio de la aplicación con la clase de la interfaz
    app = VentanaPrincipal(root)
    # Bucle de eventos para mantener la aplicación abierta
    root.mainloop()