from sqlalchemy import Column, Integer, String, Boolean, Date
from db import Base

# Creamos una clase llamada Tarea
# Esta clase será el modelo de datos de la tarea que ingresa el usuario (luego servirá para la base de datos)
# Esta clase almacena todo lo relacionado con las tareas.
class Tarea(Base):
    __tablename__ = 'tarea'
    id = Column(Integer, primary_key=True)  # Identificador único de cada tarea.
    # No puede haber dos tareas con el mismo id por eso es primary_key.
    contenido = Column(String(200), nullable=False)  # Contenido máximo de caracteres: 200
    hecha = Column(Boolean, default=False)  # Este Booleano indica si la tarea está hecha o no.
    categoria = Column(String(100), nullable=False)  # Definición correcta del campo categoría
    fecha_limite = Column(Date, nullable=False)  # Definición correcta del campo fecha_límite

    def __init__(self, contenido, hecha, categoria, fecha_limite):
        # Recordatorio que el id lo genera SQL automáticamente
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.fecha_limite = fecha_limite

    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)

    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)
