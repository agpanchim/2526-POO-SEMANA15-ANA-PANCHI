# modelos/tarea.py

class Tarea:
    """Clase que representa una única tarea en el sistema."""
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """Cambia el estado de la tarea a completada."""
        self.completada = True