class Satelite:
    def __init__(self, nombre, catalogo, latitud, longitud, altitud):
        if not isinstance(catalogo, int):
            raise TypeError("El número de catálogo debe ser un entero.")
        if not nombre or not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no debe estar vacío.")
        if not (-90 <= latitud <= 90):
            raise ValueError("La latitud debe estar entre -90 y 90.")
        if not (-180 <= longitud <= 180): 
            raise ValueError("La longitud debe estar entre -180 y 180.")
        if altitud < 100:
            raise ValueError("La altitud debe ser de al menos 100 km.")

        self.nombre = nombre
        self.catalogo = catalogo
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def tipo_orbita(self):
        if self.altitud < 2000:
            return "LEO"
        elif 2000 <= self.altitud < 34000:
            return "MEO"
        elif 34000 <= self.altitud <= 37000:
            return "GEO"
        else:
            return "HEO"

    def __str__(self):
        return f"{self.nombre} | {self.catalogo} | {self.tipo_orbita()} | {self.altitud} km"

    def en_zona(self, lon_min, lat_min, lon_max, lat_max):
        return (lon_min <= self.longitud <= lon_max) and (lat_min <= self.latitud <= lat_max)