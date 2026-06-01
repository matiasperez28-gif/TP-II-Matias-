import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Asegurar la estructura local exigida por la UTN
os.makedirs("datos", exist_ok=True)
os.makedirs("resultados", exist_ok=True)

# 2. Carga y validación del archivo obligatorio
ruta_dataset = "datos/dataset.csv"
if not os.path.exists(ruta_dataset):
    raise FileNotFoundError(f"❌ Error: No se encontró el archivo en '{ruta_dataset}'.")

df_ventas = pd.read_csv(ruta_dataset)
print("✅ Archivo 'datos/dataset.csv' cargado con éxito.\n")

# 3. Cálculo de Indicadores (Escenario B)
# Ventas totales usando la columna nativa del archivo
ventas_totales = df_ventas["monto_total"].sum()

# Producto más vendido según la cantidad total de unidades
producto_estrella = df_ventas.groupby("producto")["cantidad_vendida"].sum().idxmax()

# Extraer el año-mes (YYYY-MM) para agrupar temporalmente
df_ventas["mes"] = df_ventas["fecha_venta"].str[0:7]
ventas_mensuales = df_ventas.groupby("mes")["monto_total"].sum()

# 4. Mostrar Resultados por Consola
print("📊 --- REPORTE DE INDICADORES (Escenario B) ---")
print(f"• Ventas Totales: ${ventas_totales:,.2f}")
print(f"• Producto más vendido: {producto_estrella}")
print("• Ventas agrupadas por Mes:")
print(ventas_mensuales.to_string())
print("------------------------------------------------\n")

# 5. Generar y guardar gráfico estadístico
plt.figure(figsize=(7, 4))
plt.bar(ventas_mensuales.index, ventas_mensuales.values, color="darkblue", alpha=0.75)
plt.title("Evolución de Ventas Mensuales", fontsize=12, fontweight="bold")
plt.xlabel("Período (Mes)", fontsize=10)
plt.ylabel("Monto Total ($)", fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Guardar con el nombre exacto requerido en la estructura del TP
ruta_grafico = "resultados/gráfico_resultados.png"
plt.savefig(ruta_grafico, dpi=300, bbox_inches="tight")
print(f"📈 Gráfico exportado con éxito en '{ruta_grafico}'")
