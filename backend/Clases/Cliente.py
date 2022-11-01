import string

class Cliente():
    NIT = string
    nombre_cliente = string
    user = string
    password = string
    direccion = string
    email = string
    lista_Instancias = list


    def __init__(self,NIT,nombre_cliente,user,password,direccion,email,lista_Instancias):
        self.NIT= NIT
        self.nombre_cliente = nombre_cliente
        self.user =user
        self.password = password
        self.direccion = direccion
        self.email = email
        self.lista_Instancias = lista_Instancias
    
    def get_NIT (self):
        return self.NIT 
    
    def set_NIT (self, NIT):
        self.NIT = NIT
    
    def get_nombre_cliente (self):
        return self.nombre_cliente 
    
    def set_nombre_cliente (self, nombre_cliente):
        self.nombre_cliente = nombre_cliente
    
    def get_user (self):
        return self.user 
    
    def set_user (self, user):
        self.user = user
    
    def get_password (self):
        return self.password 
    
    def set_password (self, password):
        self.password = password
    
    def get_direccion (self):
        return self.password 
    
    def set_direccion (self, direccion):
        self.direccion = direccion
    
    def get_email (self):
        return self.email 
    
    def set_email (self, email):
        self.email = email