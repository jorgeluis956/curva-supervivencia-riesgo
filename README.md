
# Curva de Supervivencia de Riesgo Extremo

Esta aplicación permite a usuarios ingresar fechas de eventos violentos o estresores y visualizar una curva de supervivencia para evaluar el patrón de recurrencia de riesgos extremos.

## Cómo desplegar en Render

1. Sube este repositorio a GitHub.
2. Ve a [https://render.com](https://render.com) y selecciona "New Web Service".
3. Conecta tu cuenta de GitHub y elige el repositorio.
4. En "Build Command" escribe: `pip install -r requirements.txt`
5. En "Start Command" escribe: `streamlit run app.py`
6. Espera a que Render construya tu app y obtén una URL pública.

## Formato de entrada

Ingresa fechas como:

```
2012-07
2018-04
2022-07
2022-08
2022-11
2025-03
2025-04
```

Cada línea debe tener el formato `YYYY-MM`.
