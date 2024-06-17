from Equipo import Equipo

class Partido(Equipo):
    def __init__(self, id, code, name, id_partido, num_partido, equipo_Local, equipo_Visitante, fecha_partido, grupo_partido, stadium_id):
        Equipo.__init__(self,id, code, name)
        self.id_partido = id_partido
        self.num_partido = num_partido
        self.equipo_Local = equipo_Local
        self.equipo_Visitante = equipo_Visitante
        self.fecha_partido = fecha_partido
        self.grupo_partido = grupo_partido
        self.stadium_id = stadium_id

    def getIdPartido(self):
        return self.id_partido
    
    def getNumPartido(self):
        return self.num_partido
    
    def getEquipoLocal(self):
        return self.equipo_Local
    
    def getEquipoVisitante(self):
        return self.equipo_Visitante
    
    def getFechaPartido(self):
        return self.fecha_partido
    
    def getGrupoPartido(self):
        return self.grupo_partido
    
    def getStadium_Id(self):
        return self.stadium_id
    
    def getOpponents(self):
        return f"{self.equipo_Local.getName()} vs. {self.equipo_Visitante.getName()}"
    
    def getStadium_Name(self):
        return self.equipo_Local.getStadium_Name()

    def show(self):
        return f"Partido: {self.equipo_Local.getName()} vs. {self.equipo_Visitante.getName()}\nEstadio: {self.equipo_Local.getStadium_Name()}"