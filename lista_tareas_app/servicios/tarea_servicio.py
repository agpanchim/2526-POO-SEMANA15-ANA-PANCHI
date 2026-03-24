# servicios/tareas_servicios.py
from modelos.tarea import Tarea

class TareasServicios:
    """Clase de la capa de servicios que gestiona la lógica de las tareas."""
    def __init__(self):
        # Lista que almacena los objetos de tipo Tarea
        self.lista_tareas = []

    def añadir_nueva_tarea(self, descripcion):
        """Lógica para crear y guardar una tarea."""
        if descripcion.strip():
            nueva = Tarea(descripcion)
            self.lista_tareas.append(nueva)
            return True
        return False

    def listar_tareas(self):
        """Retorna todas las tareas almacenadas."""
        return self.lista_tareas

    def marcar_tarea_como_hecha(self, indice):
        """Lógica para completar una tarea por su posición."""
        if 0 <= indice < len(self.lista_tareas):
            self.lista_tareas[indice].marcar_completada()

    def eliminar_tarea_del_registro(self, indice):
        """Lógica para remover una tarea de la lista."""
        if 0 <= indice < len(self.lista_tareas):
            self.lista_tareas.pop(indice)