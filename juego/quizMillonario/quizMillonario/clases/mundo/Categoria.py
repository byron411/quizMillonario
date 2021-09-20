#Clase enum para representar las categorías
import enum
class Categoria(enum.Enum):
    '''Categorias de las preguntas'''
    BAJO=200000
    MEDIO_BAJO=400000
    MEDIO=800000
    MEDIO_ALTO=2000000
    ALTO=5000000
