import string


class Instancia():
    id_instance = string
    id_configuracion = string
    nombre_instance = string
    fecha_inicio = string
    fecha_final = string
    estado_instancia = string


    def __init__(self,id_instance,id_configuracion,nombre_instance,fecha_inicio,fecha_final,estado_instancia):
        self.id_instance= id_instance
        self.id_configuracion = id_configuracion
        self.nombre_instance =nombre_instance
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.estado_instancia = estado_instancia
    
    def get_id_instance (self):
        return self.id_instance 
    
    def set_id_instance (self, id_instance):
        self.id_instance = id_instance
    
    def get_id_configuracion (self):
        return self.id_configuracion 
    
    def set_id_configuracion (self, id_configuracion):
        self.id_configuracion = id_configuracion
        
    def get_nombre_instance (self):
        return self.nombre_instance 
    
    def set_nombre_instance (self, nombre_instance):
        self.nombre_instance = nombre_instance
    
    def get_fecha_inicio (self):
        return self.fecha_inicio 
    
    def set_fecha_inicio (self, fecha_inicio):
        self.fecha_inicio = fecha_inicio
    
    def get_fecha_final (self):
        return self.fecha_final 
    
    def set_fecha_final (self, fecha_final):
        self.fecha_final = fecha_final
    
    def get_estado_instancia (self):
        return self.estado_instancia 
    
    def set_estado_instancia (self, estado_instancia):
        self.estado_instancia = estado_instancia