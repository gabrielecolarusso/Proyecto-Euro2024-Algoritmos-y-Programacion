from Cliente import Cliente

class ClienteVIP(Cliente):
    def __init__(self,nombre,cedula,edad,partido,asiento):
        Cliente.__init__(self,nombre,cedula,edad,partido,asiento)
        self.tipo_entrada = "VIP"
        self.costo_entrada = 75
        self.costo_iva = self.costo_entrada * 0.16
        self.costo_total = self.costo_entrada + self.costo_iva

    def getNombre(self):
        return self.nombre
    
    def getCedula(self):
        return self.cedula
    
    def getEdad(self):
        return self.edad
    
    def getPartido(self):
        return self.partido
    
    def getAsiento(self):
        return self.asiento
    
    def id_vampiro(self,cedula):
        if cedula < 10 or cedula % 2 == 0:
            return False

        for i in range(2, int(cedula ** 0.5) + 1):
            if cedula % i == 0:
                mitad_izq = [int(digit) for digit in str(i)]
                mitad_der = [int(digit) for digit in str(cedula // i) if int(digit) not in mitad_izq]
                if len(mitad_izq) > 0 and len(mitad_der) > 0:
                    product = int(''.join(str(digit) for digit in mitad_izq + mitad_der))
                    if product == cedula:
                        return True

        return False

    def get_costo_total(self):
        if self.id_vampiro():
            discount = self.costo_total * 0.5
            return self.costo_total - discount
        else:
            return self.costo_total
        
    def show(self):
        return f"""\nInformacion de la entrada:
Nombre: {self.nombre}
Cedula: {self.cedula}
Partido: {self.partido}
Tipo: {self.tipo_entrada}
Asiento: {self.asiento}
Costo:
    Subtotal: {self.costo_entrada}
    Iva: {self.costo_iva}
    Total: {self.get_costo_total()}
"""