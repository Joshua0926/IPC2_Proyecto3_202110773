import string

class Configuracion():
    id_config = string
    nombre_config = string
    descripcion_config = string
    lista_recursos = list

    def __init__(self,id_config,nombre_config,descripcion_config,lista_recursos):
        self.id_config=id_config
        self.nombre_config = nombre_config
        self.descripcion_config =descripcion_config
        self.lista_recursos = lista_recursos
    
    def get_id_config (self):
        return self.id_config 
    
    def set_id_config (self, id_config):
        self.id_config = id_config
    
    def get_nombre_config (self):
        return self.nombre_config 
    
    def set_nombre_config (self, nombre_config):
        self.nombre_config = nombre_config
    
    def get_descripcion_config (self):
        return self.descripcion_config 
    
    def set_descripcion_config (self, descripcion_config):
        self.descripcion_config = descripcion_config