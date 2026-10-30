import pytest
from Satelite import Satelite

def test_creacion_satelite_valido():
    sat = Satelite("ISS", 25544, 10.5, -45.2, 420.5)
    assert sat.nombre == "ISS"
    assert sat.catalogo == 25544
    assert sat.latitud == 10.5
    assert sat.longitud == -45.2
    assert sat.altitud == 420.5

def test_excepciones_validacion():
    with pytest.raises(TypeError):
        Satelite("ISS", "25544", 0, 0, 500)
    
    with pytest.raises(ValueError):
        Satelite("", 123, 0, 0, 500)
    with pytest.raises(ValueError):
        Satelite("   ", 123, 0, 0, 500)

    with pytest.raises(ValueError):
        Satelite("ISS", 123, 95, 0, 500)

    with pytest.raises(ValueError):
        Satelite("ISS", 123, 0, -190, 500)

    with pytest.raises(ValueError):
        Satelite("ISS", 123, 0, 0, 50)

def test_tipos_orbita():
    assert Satelite("LEO", 1, 0, 0, 1500).tipo_orbita() == "LEO"
    assert Satelite("MEO", 2, 0, 0, 20000).tipo_orbita() == "MEO"
    assert Satelite("GEO", 3, 0, 0, 35786).tipo_orbita() == "GEO"
    assert Satelite("HEO", 4, 0, 0, 40000).tipo_orbita() == "HEO"

def test_str_y_zona():
    sat = Satelite("ISS", 25544, -40.0, -70.0, 420.0)
    assert str(sat) == "ISS | 25544 | LEO | 420.0 km"
    
    assert sat.en_zona(-75.0, -45.0, -65.0, -35.0) is True
    assert sat.en_zona(0.0, 0.0, 10.0, 10.0) is False