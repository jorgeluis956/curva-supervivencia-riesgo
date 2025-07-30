
# 🛡️ Curva de Supervivencia de Eventos de Riesgo Extremo

## 🎯 ¿Qué es esta herramienta?
Esta aplicación permite visualizar cómo evoluciona el riesgo de sufrir eventos violentos o estresores a lo largo del tiempo. Genera una **curva de supervivencia** que muestra cómo disminuye la probabilidad de evitar un evento conforme ocurren nuevos incidentes.

Está pensada para periodistas, investigadores, defensores de derechos humanos y otras personas que necesitan comprender patrones de riesgo en contextos hostiles.

---

## 🛠️ ¿Cómo funciona?

### 1️⃣ Ingreso de datos
El usuario introduce fechas de eventos en formato `YYYY-MM` (una por línea), que representan situaciones de alto riesgo como amenazas, ataques, actos de intimidación, etc.

### 2️⃣ Curva de Supervivencia
La herramienta calcula los **intervalos en meses** entre eventos. Con estos datos genera una **curva de supervivencia tipo escalón (step chart)**, mostrando cómo disminuye la probabilidad acumulada de no haber tenido un evento a lo largo del tiempo.

### 3️⃣ Análisis Automático
- Calcula el **intervalo promedio entre eventos**.
- Informa si los eventos se están haciendo más frecuentes (aceleración del riesgo).
- Proporciona interpretación automática para facilitar la comprensión.

---

## 🔮 Estimación del Próximo Evento

### 📊 ¿En qué se basa el Gráfico de Probabilidad?
La estimación del siguiente evento se construye usando una **distribución Weibull**, una técnica clásica en análisis de supervivencia que permite estimar el tiempo esperado hasta un próximo evento.

### 🚧 ¿Cómo se construye?
1. Calcula los intervalos históricos en meses.
2. Estima un **parámetro de escala** a partir del promedio de estos intervalos.
3. Utiliza un **parámetro de forma ≈ 1.5** (común en análisis de riesgos).
4. Simula **10,000 intervalos futuros posibles** mediante la función `weibull_min` de `scipy.stats`.
5. Genera un **gráfico de densidad de probabilidad** que muestra las zonas más probables para la ocurrencia del próximo evento.

### 📤 ¿Qué muestra el gráfico?
- **Mediana estimada**: Tiempo más probable hasta el próximo evento.
- **Bandas de confianza**:
  - 50%: zona naranja
  - 80%: zona amarilla
- Claridad visual sobre si el riesgo es inminente o disperso.

---

## 📥 ¿Qué resultados entrega?

- **Curva de Supervivencia**: Muestra la evolución acumulativa del riesgo.
- **Interpretación automática**:
  - Intervalo promedio entre eventos.
  - Número de eventos registrados.
- **Estimación del próximo evento**:
  - Mediana estimada en meses.
  - Bandas de confianza del 50% y 80%.
  - Gráfico de densidad.
- **Descarga en PDF** de la curva de supervivencia.

---

## 📚 Fundamento metodológico

Esta herramienta está inspirada en las técnicas descritas por:

> Barranco-Chamorro, I., & Gulati, S. (2015). *Some estimation techniques in reliability and survival analysis based on record-breaking data.* In C. P. Kitsos et al. (Eds.), *Theory and practice of risk assessment* (Vol. 136, pp. 333–348). Springer. https://doi.org/10.1007/978-3-319-18029-8_25

Desarrollada por **Jorge Luis Sierra con ayuda de ChatGPT**.

---
