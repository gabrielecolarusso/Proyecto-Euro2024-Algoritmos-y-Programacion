from Partido import Partido

class InfoPartido(Partido):
    def __init__(self, equipo_Local, equipo_Visitante, fecha_partido, stadium_id):
        Partido.__init__(self, equipo_Local, equipo_Visitante, fecha_partido, stadium_id)

    def show(self):
        return f"""
INFORMACION DEL PARTIDO:
Equipo Local: {self.equipo_Local.getName()}
Equipo Visitante: {self.equipo_Visitante.getName()}
Fecha del partido: {self.fecha_partido}
Estadio: {self.stadium_id.getName()}
"""
