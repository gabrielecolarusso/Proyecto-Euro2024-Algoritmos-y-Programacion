class Estadio:

    def __init__(self, id, name, city, capacity):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getCity(self):
        return self.city
    
    def getCapacity(self):
        return self.capacity
    
    def show(self):
        return """
Id: {}
Nombre: {}
Ciudad: {}
Capacidad: {}
        """.format(self.id,self.name,self.city,self.capacity)
        