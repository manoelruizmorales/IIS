import os
from IIS import IISManagement, Site


#Limpiar Terminal
os.system('cls')

# Crear una instancia de IISManagement
iis_manager = IISManagement()

# Obtener y mostrar la lista de sitios
sitios = iis_manager.GetSites()


if sitios:
    for sitio in sitios:       
        print(f"ID: {sitio.ID}, Nombre: {sitio.Name}, Bindings: {sitio.Bindings}, Estado: {sitio.State}")
else:
    print("No se pudo obtener la lista de sitios.")
