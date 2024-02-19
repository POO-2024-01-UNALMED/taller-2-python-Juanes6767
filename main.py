class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos, marca, motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca= marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        count=0
        for i in self.asientos:
            if i!=None:
                count+=1
        return count

    def verficarIntegridad(self):
        comun=self.Asientos[0]
        for i in self.asientos:
            if comun!=i:
                mensaje="Las piezas no son originales"
        if (comun==self.registro==Motor.registro):
            mensaje="Auto original"
        else:
            mensaje="Las piezas no son originales"
        return mensaje
class Asiento:
    def __init__(self,color, precio, registro):
        self.color=color
        self.color=precio
        self.color=registro
    def cambiarColor(self,color):
        if (color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color
        else:
            self.color=self.color

class Motor:
    def __init__(self,numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self, registro):
        self.registro=registro
    def asignarTipo(self,tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo=tipo