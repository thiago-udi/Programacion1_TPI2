import json
import pytest
from Satelite import Satelite
import Catalogo
from Catalogo import leer_catalogo_json, crear_catalogo, resumir_por_orbita, obtener_satelites_en_zona

def test_leer_catalogo_json(tmp_path):
    archivo_temp = tmp_path / "satelites_test.json"
    datos_ejemplo = [{"nombre": "PRUEBA", "catalogo": 123}]
    archivo_temp.write_text(json.dumps(datos_ejemplo), encoding='utf-8')

    resultado = leer_catalogo_json(str(archivo_temp))
    assert len(resultado) == 1
    assert resultado[0]["nombre"] == "PRUEBA"

def test_crear_catalogo(monkeypatch):
    monkeypatch.setattr(Catalogo, "obtener_posicion", lambda reg: (0.0, 0.0, 500.0))
    
    registros = [{"nombre": "SAT1", "catalogo": 123}]
    satelites = crear_catalogo(registros)
    
    assert len(satelites) == 1
    assert satelites[0].nombre == "SAT1"
    assert satelites[0].altitud == 500.0

def test_resumir_por_orbita():
    lista = [
        Satelite("S1", 1, 0, 0, 500),
        Satelite("S2", 2, 0, 0, 1000),
        Satelite("S3", 3, 0, 0, 25000),
    ]
    resumen = resumir_por_orbita(lista)
    
    assert resumen["LEO"]["cantidad"] == 2
    assert resumen["LEO"]["min"] == 500
    assert resumen["LEO"]["max"] == 1000
    assert resumen["LEO"]["promedio"] == 750.0
    
    assert resumen["MEO"]["cantidad"] == 1
    assert resumen["MEO"]["min"] == 25000

def test_obtener_satelites_en_zona():
    lista = [
        Satelite("Dentro", 1, -40.0, -70.0, 500),
        Satelite("Fuera", 2, 10.0, 20.0, 500),
    ]
    zona = obtener_satelites_en_zona(lista, -75.0, -45.0, -65.0, -35.0)
    assert len(zona) == 1
    assert zona[0].nombre == "Dentro"

def test_crear_catalogo_con_error(monkeypatch):
    def mock_obtener_posicion_error(reg):
        raise ValueError("Error simulado de órbita")
    
    monkeypatch.setattr(Catalogo, "obtener_posicion", mock_obtener_posicion_error)
    
    registros = [{"nombre": "SAT_ROTO", "catalogo": 999}]
    satelites = crear_catalogo(registros)
    
    assert len(satelites) == 0