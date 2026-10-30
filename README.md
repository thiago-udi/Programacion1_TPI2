# TPI 2: Satélites Activos (`tpi2-satelites`)

**Estudiante:** Udi Thiago  

## Descripción del Proyecto
Programa de línea de comandos (CLI) desarrollado en Python que lee datos orbitales de satélites activos obtenidos de CelesTrak (`satelites.json`), calcula sus coordenadas geográficas actuales (latitud, longitud y altitud) mediante la librería `skyfield`, los modela a través de Programación Orientada a Objetos (POO) y permite realizar consultas estadísticas resumidas por tipo de órbita y filtrado espacial por zona geográfica.

---

## Estructura del Repositorio
```text
tpi2-satelites/
├── datos/
│   └── satelites.json         # Archivo de datos provisto
├── .gitignore                 # Archivos excluidos del control de versiones
├── requirements.txt           # Dependencias del proyecto
├── funciones_base.py          # Módulo provisto para cálculo orbital
├── satelite.py                # Definición de la clase Satelite y validaciones
├── catalogo.py                # Funciones de carga, filtrado y resúmenes
├── consultar_satelites.py     # Programa principal (CLI)
├── test_satelite.py           # Pruebas unitarias para satelite.py
├── test_catalogo.py           # Pruebas unitarias para catalogo.py
└── README.md                  # Documentación del proyecto