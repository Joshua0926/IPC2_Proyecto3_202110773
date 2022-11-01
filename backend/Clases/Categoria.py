import string

class Categoria():
    id_categoria = string
    nombre_categoria = string
    descripcion_categoria = string
    carga_de_trabajo = string
    lista_configuraciones = list
    
    
    def __init__(self,id_categoria,nombre_categoria,descripcion_categoria,carga_de_trabajo,lista_configuraciones):
        self.id_categoria=id_categoria
        self.nombre_categoria = nombre_categoria
        self.descripcion_categoria =descripcion_categoria
        self.carga_de_trabajo = carga_de_trabajo
        self.lista_configuraciones = lista_configuraciones
    
    
    def get_id_categoria (self):
        return self.id_categoria 
    
    def set_id_categoria (self, id_categoria):
        self.id_categoria = id_categoria
    
    def get_nombre_categoria (self):
        return self.nombre_categoria 
    
    def set_nombre_categoria (self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
    
    def get_descripcion_categoria (self):
        return self.descripcion_categoria 
    
    def set_descripcion_categoria (self, descripcion_categoria):
        self.descripcion_categoria = descripcion_categoria
    
    def get_carga_de_trabajo (self):
        return self.carga_de_trabajo 
    
    def set_carga_de_trabajo (self, carga_de_trabajo):
        self.carga_de_trabajo = carga_de_trabajo