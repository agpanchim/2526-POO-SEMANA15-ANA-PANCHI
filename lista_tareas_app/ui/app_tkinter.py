# ui/app_tkinter.py
import tkinter as tk
from tkinter import messagebox
from servicios.tareas_servicios import TareasServicios


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas - GUI")
        self.servicio = TareasServicios()

        # Componente Entry para la descripción de la tarea
        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=10)

        # MANEJO DE EVENTO DE TECLADO:
        # Se vincula la tecla Enter (<Return>) para disparar la función añadir.
        self.entrada.bind("<Return>", lambda event: self.añadir_tarea_gui())

        # Botones de la interfaz
        self.btn_añadir = tk.Button(root, text="Añadir Tarea", command=self.añadir_tarea_gui)
        self.btn_añadir.pack(pady=5)

        # Listbox para visualizar las tareas
        self.lista_visual = tk.Listbox(root, width=50, height=10)
        self.lista_visual.pack(pady=10, padx=10)

        # MANEJO DE EVENTO DE RATÓN:
        # Se vincula el Doble Clic (<Double-1>) para marcar la tarea como completada.
        self.lista_visual.bind("<Double-1>", lambda event: self.completar_tarea_gui())

        # Contenedor para botones de acción
        marco = tk.Frame(root)
        marco.pack(pady=10)

        tk.Button(marco, text="Marcar Completada", command=self.completar_tarea_gui).grid(row=0, column=0, padx=5)
        tk.Button(marco, text="Eliminar", command=self.eliminar_tarea_gui).grid(row=0, column=1, padx=5)

    def refrescar_lista(self):
        """Actualiza la visualización y aplica el feedback visual solicitado."""
        self.lista_visual.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            if tarea.completada:
                texto = f"[Hecho] {texto}"

            self.lista_visual.insert(tk.END, texto)

            # Feedback Visual: Si está completada, el texto se vuelve gris.
            if tarea.completada:
                self.lista_visual.itemconfig(tk.END, fg="gray")

    def añadir_tarea_gui(self):
        """Interacción para añadir tareas."""
        if self.servicio.añadir_tarea(self.entrada.get()):
            self.entrada.delete(0, tk.END)
            self.refrescar_lista()
        else:
            messagebox.showwarning("Atención", "La descripción no puede estar vacía.")

    def completar_tarea_gui(self):
        """Interacción para marcar tareas como completadas."""
        try:
            indice = self.lista_visual.curselection()[0]
            self.servicio.completar_tarea(indice)
            self.refrescar_lista()
        except IndexError:
            messagebox.showwarning("Error", "Selecciona una tarea de la lista.")

    def eliminar_tarea_gui(self):
        """Interacción para eliminar tareas."""
        try:
            indice = self.lista_visual.curselection()[0]
            self.servicio.eliminar_tarea(indice)
            self.refrescar_lista()
        except IndexError:
            pass