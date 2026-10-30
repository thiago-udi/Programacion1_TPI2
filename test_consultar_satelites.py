import sys
import json
import pytest
import Consultar_satelites

def test_consultar_main_sin_argumentos(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["consultar_satelites.py"])
    with pytest.raises(SystemExit) as excinfo:
        Consultar_satelites.main()
    assert excinfo.value.code == 1

def test_consultar_main_resumen(monkeypatch, tmp_path):
    archivo_temp = tmp_path / "satelites.json"
    datos = [{"OBJECT_NAME": "ISS", "NORAD_CAT_ID": 25544, "MEAN_MOTION": 15.0, "ECCENTRICITY": 0.0, "INCLINATION": 51.0, "EPOCH": "2026-10-14T08:06:39"}]
    archivo_temp.write_text(json.dumps(datos), encoding='utf-8')

    monkeypatch.setattr(sys, "argv", ["consultar_satelites.py", str(archivo_temp), "resumen"])
    

    monkeypatch.setattr(Consultar_satelites, "crear_posicion_dummy_o_similar", lambda r: None, raising=False)
    from Satelite import Satelite
    monkeypatch.setattr(Consultar_satelites, "crear_catalogo", lambda regs: [Satelite("ISS", 25544, 0.0, 0.0, 400.0)])

    try:
        Consultar_satelites.main()
    except SystemExit:
        pass  # Si el script hace sys.exit o termina normalmente