import os
import sys
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.logica.utils import leer_archivo_entrada
from src.logica.modciFB import modciFB
from src.logica.modciPD import modciPD
from src.logica.modciV import modciV

# Ruta a los archivos de prueba
ruta_pruebas = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/BateriaPruebas"))
archivos_prueba = sorted([f for f in os.listdir(ruta_pruebas) if f.endswith(".txt")])

# Rutas para los reportes
ruta_reporte_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../tests/outputs/reporte_resultados.csv"))
ruta_reporte_md = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../tests/outputs/reporte_resultados.md"))

# titulos
encabezado = ["Archivo", "Algoritmo", "Conflicto Interno", "Esfuerzo Total", "Estrategia"]
tabla_md = []
tabla_md.append("| " + " | ".join(encabezado) + " |")
tabla_md.append("|" + "|".join(["-" * len(e) for e in encabezado]) + "|")

# CSV 
with open(ruta_reporte_csv, mode='w', newline='', encoding='utf-8-sig') as file_csv:
    writer = csv.writer(file_csv)
    writer.writerow(encabezado)

    for archivo in archivos_prueba:
        ruta_archivo = os.path.join(ruta_pruebas, archivo)
        print(f"\n[INFO] Procesando archivo: {archivo}")

        try:
            red_social = leer_archivo_entrada(ruta_archivo)
        except Exception as e:
            print(f"[ERROR] Al leer {archivo}: {e}")
            continue

        for nombre_algoritmo, funcion in [
            #("Fuerza Bruta", modciFB),     # Algoritmo pesado
            ("Programacion Dinamica", modciPD),
            ("Voraz", modciV)
        ]:
            try:
                print(f"    [INFO] Ejecutando {nombre_algoritmo}...")
                estrategia, esfuerzo, conflicto = funcion(red_social)

                # limpiar datos
                conflicto = round(conflicto, 2)
                esfuerzo = int(esfuerzo)
                estrategia_str = str(list(estrategia))

                # Guardar en CSV
                writer.writerow([archivo, nombre_algoritmo, conflicto, esfuerzo, estrategia_str])

                # Guardar en Markdown
                fila_md = f"| {archivo} | {nombre_algoritmo} | {conflicto} | {esfuerzo} | {estrategia_str} |"
                tabla_md.append(fila_md)

                print(f"    [OK] {nombre_algoritmo} -> CI: {conflicto}, E: {esfuerzo}")
            except Exception as e:
                writer.writerow([archivo, nombre_algoritmo, "ERROR", "ERROR", str(e)])
                tabla_md.append(f"| {archivo} | {nombre_algoritmo} | ERROR | ERROR | {str(e)} |")
                print(f"    [ERROR] {nombre_algoritmo} fallo con {archivo}: {e}")

with open(ruta_reporte_md, 'w', encoding='utf-8') as md_file:
    md_file.write("# Reporte de Resultados - Formato Markdown\n\n")
    md_file.write("\n".join(tabla_md))

print(f"\n Archivos generados:\n- CSV: {ruta_reporte_csv}\n- Markdown: {ruta_reporte_md}")
