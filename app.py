
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Curva de Supervivencia de Eventos de Riesgo", layout="centered")

st.title("🛡️ Curva de Supervivencia: Eventos de Riesgo Extremo")
st.write("Introduce fechas de eventos (estrés o violencia) para visualizar cómo evoluciona el riesgo a lo largo del tiempo.")

# Entrada de fechas
st.subheader("📅 Fechas de eventos")
event_input = st.text_area("Introduce una fecha por línea (ejemplo: 2012-07)", height=200)

if event_input:
    try:
        # Convertir texto a lista de fechas
        fechas = [datetime.strptime(line.strip(), "%Y-%m") for line in event_input.splitlines() if line.strip()]
        fechas.sort()
        etiquetas = [fecha.strftime("%Y (%b)") for fecha in fechas]

        # Calcular intervalos en meses
        meses = [(fechas[i] - fechas[0]).days // 30 for i in range(len(fechas))]
        survival_probability = 1 - (np.arange(1, len(meses) + 1) / len(meses))

        # Graficar
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.step(meses, survival_probability, where='post', linewidth=2, color='orange', label='Curva de Supervivencia')
        ax.scatter(meses, survival_probability, color='black', zorder=5)

        for i, label in enumerate(etiquetas):
            ax.text(meses[i], survival_probability[i] + 0.05, label, ha='center', fontsize=9)

        ax.set_title("Curva de Supervivencia: Intervalos entre Eventos de Riesgo Extremo")
        ax.set_xlabel("Meses desde el primer evento")
        ax.set_ylabel("Probabilidad de no ocurrencia (Supervivencia)")
        ax.set_ylim(0, 1.05)
        ax.grid(True)
        st.pyplot(fig)

        # Explicación automática
        st.subheader("📘 Interpretación automática")
        st.write(f"Se han identificado **{len(fechas)} eventos**. La curva muestra cómo la probabilidad de no ocurrencia disminuye a medida que los eventos se vuelven más frecuentes.")
        if len(fechas) > 1:
            promedio = round(np.mean(np.diff(meses)), 1)
            st.write(f"El **intervalo promedio entre eventos** es de aproximadamente **{promedio} meses**.")
        st.write("Esta visualización permite observar patrones de recrudecimiento del riesgo o periodos de calma relativa.")

    except Exception as e:
        st.error("⚠️ Error procesando las fechas. Asegúrate de usar el formato YYYY-MM, por ejemplo: 2012-07.")
