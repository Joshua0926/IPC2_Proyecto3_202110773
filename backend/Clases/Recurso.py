import string

class Recurso():
    id_recurso = string
    nombre_recurso = string
    abreviatura_recurso = string
    metrica = string
    tipo = string
    costo = float

    def __init__(self,id_recurso,nombre_recurso,abreviatura_recurso,metrica,tipo,costo):
        self.id_recurso=id_recurso
        self.nombre_recurso = nombre_recurso
        self.abreviatura_recurso =abreviatura_recurso
        self.metrica =metrica
        self.tipo = tipo
        self.costo = costo