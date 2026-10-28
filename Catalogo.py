import json
from Satelite import Satelite
from funciones_base import obtener_posicion

def leer_catalogo_json(ruta_archivo):
    """Lee el archivo JSON y devuelve la lista de registros crudos."""
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def crear_catalogo(registros):
    """
    Recibe la lista de registros del JSON, calcula su posición actual 
    usando funciones_base y devuelve una lista de objetos Satelite válidos.
    """
    satelites = []
    for reg in registros:
        # Extraemos los datos básicos del registro
        nombre = reg.get("nombre")
        catalogo = reg.get("catalogo")
        
        # Intentamos obtener la posición (latitud, longitud, altitud)
        try:
            latitud, longitud, altitud = obtener_posicion(reg)
            # Creamos la instancia de la clase Satelite
            sat = Satelite(nombre, catalogo, latitud, longitud, altitud)
            satelites.append(sat)
        except (ValueError, TypeError):
            # Si algún satélite tiene datos corruptos o falla el cálculo, lo omitimos
            continue
            
    return satelites

def resumir_por_orbita(lista_satelites):
    """
    Agrupa los satélites por tipo de órbita y calcula cantidad, 
    altitud mínima, máxima y promedio.
    """
    resumen = {}
    
    for sat in lista_satelites:
        tipo = sat.tipo_orbita()
        if tipo not in resumen:
            resumen[tipo] = {
                "cantidad": 0,
                "altitudes": []
            }
        resumen[tipo]["cantidad"] += 1
        resumen[tipo]["altitudes"].append(sat.altitud)
        
    # Calculamos min, max y promedio para cada órbita
    resultado_final = {}
    for tipo, datos in resumen.items():
        altitudes = datos["altitudes"]
        resultado_final[tipo] = {
            "cantidad": datos["cantidad"],
            "min": min(altitudes),
            "max": max(altitudes),
            "promedio": sum(altitudes) / len(altitudes)
        }
        
    return resultado_final

def obtener_satelites_en_zona(lista_satelites, lon_min, lat_min, lon_max, lat_max):
    """Filtra y devuelve una lista con los satélites que se encuentran dentro de la zona."""
    satelites_en_zona = []
    for sat in lista_satelites:
        if sat.en_zona(lon_min, lat_min, lon_max, lat_max):
            satelites_en_zona.append(sat)
    return satelites_en_zona