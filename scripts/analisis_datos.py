import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear carpetas
os.makedirs("datos", exist_ok=True)
os.makedirs("resultados", exist_ok=True)

# 2. Datos de prueba listos (con números incluidos)
datos_simulados = {
    "fecha": ["2025-01-15", "2025-01-20", "2025-02-10", "2025-02-18", "2025-03-05", "2025-03-22"],
    "producto": ["Teclado", "Mouse", "Teclado", "Monitor", "Mouse", "Monitor"],
    "cantidad": [2, 5, 1, 1, 3, 2],
    "precio": [100, 20, 100, 250, 20, 250]
}

# 3. Crear el archivo ventas.csv
df = pd.DataFrame(datos_simulados)
df.to_csv("datos/ventas.csv", index=False)
print("✅ Archivo 'datos/ventas.csv' creado con éxito.\n")

# 4. Calcular Indicadores
df_ventas = pd.read_csv("datos/ventas.csv")
df_ventas["total"] = df_ventas["cantidad"] * df_ventas["precio"]

ventas_totales = df_ventas["total"].sum()
producto_estrella = df_ventas.groupby("producto")["cantidad"].sum().idxmax()
df_ventas["mes"] = df_ventas["fecha"].str[0:7]
ventas_mensuales = df_ventas.groupby("mes")["total"].sum()

# 5. Mostrar Resultados
print("📊 --- RESULTADOS ---")
print(f"Ventas Totales: ${ventas_totales}")
print(f"Producto más vendido: {producto_estrella}")
print("Ventas por Mes:\n", ventas_mensuales)
print("----------------------\n")

# 6. Crear y guardar gráfico
plt.figure(figsize=(6, 4))
plt.plot(ventas_mensuales.index, ventas_mensuales.values, marker="o", color="blue")
plt.title("Evolución de Ventas Mensuales")
plt.grid(True)
plt.savefig("resultados/grafico_ventas.png")
print("📈 Gráfico guardado en 'resultados/grafico_ventas.png'")
