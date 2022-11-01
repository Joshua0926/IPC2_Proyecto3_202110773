import string

class Consumo():
    nit_cliente = string
    id_Instancia = string
    tiempo_consumido = float
    fecha_hora = string

    def __init__(self,nit_cliente,id_Instancia,tiempo_consumido,fecha_hora):
        self.nit_cliente= nit_cliente
        self.id_Instancia = id_Instancia
        self.tiempo_consumido =tiempo_consumido
        self.fecha_hora = fecha_hora