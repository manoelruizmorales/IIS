import subprocess
import re
import os


class IISManagement:

    def __init__(self):
         pass

    def extraer_informacion(self, cadena):

        if not isinstance(cadena, str):
            return None
        
        # Expresión regular para extraer la información
        patron = r'SITE\s+"(?P<nombre>[^"]+)"\s+\(id:(?P<id>\d+),bindings:(?P<bindings>[^,]+),state:(?P<estado>[^)]+)\)'

        # Buscar coincidencias
        #print("====================>", cadena)
        coincidencias = re.search(patron, cadena)

        # Extraer información si se encuentra una coincidencia
        if coincidencias and cadena:

            informacion = {
                'nombre': coincidencias.group('nombre'),
                'id': coincidencias.group('id'),
                'bindings': coincidencias.group('bindings'),
                'estado': coincidencias.group('estado')
            }

            return informacion
        
        else:

            return None

    def GetSites(self):
        # Lista para almacenar los objetos Site
        lista_sitios_regresar = []
      

        # Ejecutar el comando y capturar la salida
        result = subprocess.run(
            ['c:\\windows\\system32\\inetsrv\\appcmd.exe', 'list', 'site'], 
            stdout=subprocess.PIPE,
            text=True  # Asegura que la salida sea una cadena de texto
        )

        
        # Convertir la salida en un arreglo de cadenas, cada línea como un elemento
        lista_sitios = result.stdout.splitlines() 
        print(result.stdout)
        # Iterar sobre cada sitio y crear objetos Site
        for sitio in lista_sitios:
            info = self.extraer_informacion(sitio)
            if info:
                site_id = info['id']
                name = info['nombre']
                bindings = info['bindings']
                state = info['estado']
                
                # Crear objeto Site y agregarlo a la lista
                if site_id:# is not None and name is not None and state is not None:
                    site_obj = Site(site_id, name, bindings, state)
                    lista_sitios_regresar.append(site_obj)
        
        return lista_sitios_regresar




class Site:
    def __init__(self, site_id, name, bindings, state):
        self.ID = site_id
        self.Name = name
        self.Bindings = bindings
        self.State = state







