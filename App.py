from Estadio import Estadio
from ProductoComida import ProductoComida
from ClienteGeneral import ClienteGeneral
from ClienteVip import ClienteVip
from Equipo import Equipo
from Partido import Partido
from InfoPartido import InfoPartido
from Producto import Producto
from ProductoBebida import ProductoBebida
import random
import requests

class App():
    def __init__(self):
        self.estadio = []
        self.productos = []
        self.clientesGeneral = []
        self.clientesVip = []
        self.equipo = []
        self.partido = []
        self.partido_activo = []
        self.info_partido = []
        self.paises = []
        self.gastosVip = 0
        self.cantidad_productos_vendidos = {}
        self.cliente_compra = {}

    #Obtenemos la informacion de la API de forma interactiva seleccionando 1 de las opciones
    def get_info_api(self, parametro):
        #parametroetro de la API (String): puede ser 'matches', 'teams' o 'stadiums' accediendo a todos los datos
        #Retorno (Dictionary): diccionario con la informacion de la API
        url = f"https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/{parametro}.json"
        if parametro == "stadiums":
            response = requests.request("GET", url)
            return response.json()
        elif parametro == "teams":
            response = requests.request("GET", url)
            return response.json()
        else:
            response = requests.request("GET", url)
            return response.json()
    def registrar_estadios(self):
        estadios = self.get_info_api("")
    
    def buscar_partidos(self):
        #Esta funcion permitira buscar todos los partidos de un pais, Buscar todos los partidos que se jugarán en un estadio específico, Buscar todos los partidos que se jugarán en una fecha determinada
 
        while True:
            opcion = input("""Escriba al numero correspondiente a la busqueda que desea realizar:
    1. Buscar todos los partidos de un pais
    2. Buscar todos los partidos que se jugarán en un estadio específico
    3. Buscar todos los partidos que se jugarán en una fecha determinada
""")
            if opcion != "1" and opcion != "2" and opcion != "3":
                print("Error.")
                continue
            else:
                break

        if opcion == "1":
            partidos_encontrados = []
            while True:
                pais = input("Introduzca el nombre del pais que desea buscar: ").title()
                if pais == "":
                    pais = input("Error. Introduzca el nombre del pais que desea buscar: ").title()
                else:
                    break
                for partido in self.partido:
                    if partido.get_home_team().get_pais() == pais or partido.get_away_team().get_pais() == pais:
                        partidos_encontrados.append(partido)
                        print(f" {pais} jugara los siguientes partidos: {partidos_encontrados}")
    
        if opcion == "2":
            partidos_encontrados = []
            while True:
                estadio = input("Introduzca el nombre del estadio que desea buscar: ").title()
                if estadio == "":
                    estadio = input("Error. Introduzca el nombre del estadio que desea buscar: ").title()
                else:
                    break
                for partido in self.partido:
                    if partido.get_home_team().get_stadium_name() == estadio or partido.get_away_team().get_stadium_name() == estadio:
                        partidos_encontrados.append(partido)
                        print(f"En el estadio: {estadio} se jugaran los siguientes partidos: {partidos_encontrados}")

        if opcion == "3":
            partidos_encontrados = []
            while True:
                fecha = input("Introduzca la fecha que desea buscar: [AAAA-MM-DD] ")
                if fecha == "":
                    fecha = input("Error. Introduzca la fecha que desea buscar: ")
                else:
                    break
                for partido in self.partido:
                    if partido.get_date() == fecha:
                        partidos_encontrados.append(partido)
                        print(f"En la fecha: {fecha} se jugaran los siguientes partidos: {partidos_encontrados}")

    def comprar_entradas(self):
    # Esta funcion permitira al usuario comprar las entradas para los partidos disponibles
        print("BIENVENIDO, Ingrese los siguientes datos solicitados por el sistema: ")
        nombre = input("Introduzca su nombre: ").title()
        while True:
            try: 
                cedula = int(input("Introduzca su cedula: "))
                if cedula < 0:
                    print("Error. La cedula no debe ser negativa.")
                    continue
                if not cedula.isnumeric():
                    print("Error. Introduzca un numero valido")
                    continue
                else:
                    break
            except:
                print("Error. Introduzca un numero valido")
                continue
        while True:
            try: 
                edad = int(input("Introduzca su edad: "))
                if edad < 0:
                    print("Error. La edad no debe ser negativa.")
                    continue
                if not edad.isnumeric():
                    print("Error. Introduzca un numero valido")
                    continue
                else:
                    break
            except:
                print("Error. Introduzca un numero valido")
                continue

        #Se imprimen los partidos disponibles para comprar las entradas
        print("Partidos disponibles:")
        for i, partido in enumerate(self.partido):
            print(f"{i+1}. {partido.get_home_team().get_nombre()} vs {partido.get_away_team().get_nombre()}, {partido.get_date()}")
            print(f"Estadio: {partido.get_home_team().get_stadium_name()}")
        #Seleccionar un partido disponible
        while True:
            try:
                seleccion = int(input("Seleccione el numero del partido que desea comprar la entrada: "))
                if seleccion < 1 or seleccion > len(self.partido):
                    print("Error. Seleccione un numero valido.")
                    continue
                else:
                    break
            except:
                print("Error. Introduzca un numero valido")
                continue

        #Comprar la entrada al partido
        partido_seleccionado = self.partido[seleccion - 1]
        print(f"Ha seleccionado el partido: {partido_seleccionado.get_home_team().get_nombre()} vs {partido_seleccionado.get_away_team().get_nombre()}, {partido_seleccionado.get_date()}")

        #Permite al usuario seleccionar su tipo de entrada
        while True:
            tipo_de_entrada = input("""Ingresa el tipo de entrada la cual quieres comprar para el partido: 
1. General 
2. Vip 
""")
            if tipo_de_entrada != "1" and tipo_de_entrada != "2":
                print("Error. Tipo de entrada invalido")
                continue
            else:
                break

        if tipo_de_entrada == "1":


        #Seleccionar un partido disponible
        
        print("Gracias por comprar la entrada. Espero que disfrute el partido!")