
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from io import BytesIO
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import weibull_min

st.set_page_config(page_title="Curva de Supervivencia de Eventos de Riesgo", layout="centered")

st.title("🛡️ Curva de Supervivencia: Eventos de Riesgo Extremo")
st.markdown(
    (
        "<p style='font-size: 10px;'>"
        "Esta herramienta fue desarrollada por Jorge Luis Sierra como parte del proyecto Salama. "
        "Está basada en la metodología de Barranco-Chamorro y Gulati (2015) para predecir la supervivencia ante eventos de alto riesgo."
        "<br><br>"
        "Referencia: Barranco-Chamorro, I., & Gulati, S. (2015). Some estimation techniques in reliability and survival analysis based on record-breaking data. "
        "In C. P. Kitsos et al. (Eds.), <i>Theory and practice of risk assessment</i> (Vol. 136, pp. 333–348). Springer. "
        "<a href='https://doi.org/10.1007/978-3-319-18029-8_25' target='_blank'>https://doi.org/10.1007/978-3-319-18029-8_25</a>"
        "</p>"
    ),
    unsafe_allow_html=True
)

if "reset" not in st.session_state:
    st.session_state["reset"] = False

if st.button("🔁 Reiniciar entrada de datos"):
    st.session_state["reset"] = True
    st.rerun()

st.subheader("📅 Fechas de eventos")
event_input = st.text_area("Introduce una fecha por línea (ejemplo: 2012-07)", height=200)

if event_input:
    try:
        fechas = [datetime.strptime(line.strip(), "%Y-%m") for line in event_input.splitlines() if line.strip()]
        fechas.sort()
        etiquetas = [fecha.strftime("%Y (%b)") for fecha in fechas]
        meses = [(fechas[i] - fechas[0]).days // 30 for i in range(len(fechas))]
        survival_probability = 1 - (np.arange(1, len(meses) + 1) / len(meses))

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

        st.subheader("📄 Descargar resultado en PDF")
        pdf_buffer = BytesIO()
        with PdfPages(pdf_buffer) as pdf:
            pdf.savefig(fig, bbox_inches='tight')
        pdf_buffer.seek(0)
        st.download_button("📥 Descargar curva en PDF", data=pdf_buffer, file_name="Curva_Supervivencia.pdf", mime="application/pdf")

        st.subheader("📘 Interpretación automática")
        st.write(f"Se han identificado **{len(fechas)} eventos**. La curva muestra cómo la probabilidad de no ocurrencia disminuye a medida que los eventos se vuelven más frecuentes.")
        if len(fechas) > 1:
            promedio = round(np.mean(np.diff(meses)), 1)
            st.write(f"El **intervalo promedio entre eventos** es de aproximadamente **{promedio} meses**.")
        st.write("Esta visualización permite observar patrones de recrudecimiento del riesgo o periodos de calma relativa.")

        if len(meses) > 1:
            intervals = np.diff(meses)
            scale_est = np.mean(intervals)
            shape_est = 1.5

            simulated_intervals = weibull_min.rvs(c=shape_est, scale=scale_est, size=10000)
            median_interval = round(np.median(simulated_intervals), 1)
            p10 = round(np.percentile(simulated_intervals, 10), 1)
            p90 = round(np.percentile(simulated_intervals, 90), 1)
            p25 = round(np.percentile(simulated_intervals, 25), 1)
            p75 = round(np.percentile(simulated_intervals, 75), 1)

            st.subheader("🔮 Estimación de ocurrencia futura")
            st.write(f"Según los datos ingresados y el modelo Weibull:")
            st.write(f"- **Mediana estimada:** {median_interval} meses desde el último evento.")
            st.write(f"- **50% de probabilidad:** entre {p25} y {p75} meses.")
            st.write(f"- **80% de probabilidad:** entre {p10} y {p90} meses.")
            st.write("_Este modelo es indicativo y refleja patrones históricos, no predice eventos específicos._")

            fig2, ax2 = plt.subplots(figsize=(10, 4))
            ax2.hist(simulated_intervals, bins=50, density=True, color='skyblue', edgecolor='gray', alpha=0.7)
            ax2.axvline(median_interval, color='red', linestyle='--', label=f"Mediana: {median_interval} meses")
            ax2.fill_betweenx(y=[0, ax2.get_ylim()[1]], x1=p25, x2=p75, color='orange', alpha=0.2, label='50% probabilidad')
            ax2.fill_betweenx(y=[0, ax2.get_ylim()[1]], x1=p10, x2=p90, color='yellow', alpha=0.1, label='80% probabilidad')

            ax2.set_title("Distribución simulada del intervalo al próximo evento")
            ax2.set_xlabel("Meses desde el último evento")
            ax2.set_ylabel("Densidad de probabilidad")
            ax2.legend()
            ax2.grid(True)
            st.pyplot(fig2)

    except Exception as e:
        st.error("⚠️ Error procesando las fechas. Asegúrate de usar el formato YYYY-MM, por ejemplo: 2012-07.")
