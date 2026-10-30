import sys
from Catalogo import leer_catalogo_json, crear_catalogo, resumir_por_orbita, obtener_satelites_en_zona

def main():
    if len(sys.argv) < 3:
        print("Uso correcto:")
        print("  python consultar_satelites.py <ruta_json> resumen")
        print("  python consultar_satelites.py <ruta_json> zona <lon_min> <lat_min> <lon_max> <lat_max>")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    accion = sys.argv[2]

    try:
        registros = leer_catalogo_json(ruta_archivo)
        satelites = crear_catalogo(registros)
    except Exception as e:
        print(f"Error al cargar el archivo o catálogo: {e}")
        sys.exit(1)

    if accion == "resumen":
        resumen = resumir_por_orbita(satelites)
        for tipo, datos in resumen.items():
            print(f"Órbita {tipo}:")
            print(f"  Cantidad: {datos['cantidad']}")
            print(f"  Altitud mínima: {datos['min']:.1f} km")
            print(f"  Altitud máxima: {datos['max']:.1f} km")
            print(f"  Altitud promedio: {datos['promedio']:.1f} km")

    elif accion == "zona":
        if len(sys.argv) < 7:
            print("Error: Faltan argumentos para la zona (lon_min, lat_min, lon_max, lat_max).")
            sys.exit(1)
        try:
            lon_min = float(sys.argv[3])
            lat_min = float(sys.argv[4])
            lon_max = float(sys.argv[5])
            lat_max = float(sys.argv[6])
        except ValueError:
            print("Error: Las coordenadas de la zona deben ser números válidos.")
            sys.exit(1)

        satelites_zona = obtener_satelites_en_zona(satelites, lon_min, lat_min, lon_max, lat_max)
        print(f"Cantidad de satélites en la zona: {len(satelites_zona)}")
        for sat in satelites_zona:
            print(sat)
    else:
        print(f"Acción desconocida: '{accion}'. Use 'resumen' o 'zona'.")
        sys.exit(1)

if __name__ == "__main__":
    main()