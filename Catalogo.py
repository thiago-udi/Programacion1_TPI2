import json
from Satelite import Satelite
from funciones_base import obtener_posicion

def leer_catalogo_json(ruta_archivo):
    with open(ruta_archivo, 'r') as f:
        return json.load(f)

def crear_catalogo(registros):
    satelites = []
    for reg in registros:
        nombre = reg.get("nombre")
        catalogo = reg.get("catalogo")
        
        try:
            latitud, longitud, altitud = obtener_posicion(reg)
            sat = Satelite(nombre, catalogo, latitud, longitud, altitud)
            satelites.append(sat)
        except (ValueError, TypeError):
            continue
            
    return satelites

def resumir_por_orbita(lista_satelites):
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
    satelites_en_zona = []
    for sat in lista_satelites:
        if sat.en_zona(lon_min, lat_min, lon_max, lat_max):
            satelites_en_zona.append(sat)
    return satelites_en_zona