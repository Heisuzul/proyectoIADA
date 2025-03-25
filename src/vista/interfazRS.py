import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.logica.utils import leer_archivo_entrada, modCI
from src.logica.modciFB import modciFB


def cargar_archivo():
    try:
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            global red_social
            red_social = leer_archivo_entrada(ruta)
            if red_social:
                text_red_social.config(state="normal")
                text_red_social.delete("1.0", tk.END)
                text_red_social.insert(tk.END, str(red_social))
                text_red_social.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar el archivo: {e}")


def ejecutar_algoritmo():
    if red_social is None:
        messagebox.showwarning("Advertencia", "Carga primero un archivo de red social")
        return
    
    algoritmo = var_algoritmo.get()
    resultado = None

    if algoritmo == "modciFB":
        resultado = modciFB(red_social)    
    # elif algoritmo == "modciPD":
        # resultado = modciPD(red_social)
    # elif algoritmo == "modciV":
        # resultado = modciV(red_social)

    if resultado:
        mejor_estrategia, mejor_esfuerzo, mejor_conflicto = resultado  
        
        # Aplicar modCI para obtener la nueva red social
        nueva_red_social = modCI(red_social, mejor_estrategia)  

        # Mostrar resultados
        text_resultado.config(state="normal")
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, f"Mejor estrategia: {mejor_estrategia}\n")
        text_resultado.insert(tk.END, f"Mejor esfuerzo: {mejor_esfuerzo}\n")
        text_resultado.insert(tk.END, f"Mejor conflicto: {mejor_conflicto}\n")
        text_resultado.insert(tk.END, f"Nueva red social: {nueva_red_social}")
        text_resultado.config(state="disabled")


# Configurar ventana principal
root = tk.Tk()
root.title("Red Social - Análisis de Conflicto")

# Botón para cargar archivo
btn_cargar = tk.Button(root, text="Cargar Archivo", command=cargar_archivo)
btn_cargar.pack()

# Área de texto para mostrar la red social
text_red_social = tk.Text(root, height=5, width=50, state="disabled")
text_red_social.pack()

# Selección de algoritmo
var_algoritmo = tk.StringVar(value="modciFB")
frame_algoritmo = tk.Frame(root)
tk.Label(frame_algoritmo, text="Algoritmo:").pack(side=tk.LEFT)
tk.Radiobutton(frame_algoritmo, text="Fuerza Bruta", variable=var_algoritmo, value="modciFB").pack(side=tk.LEFT)
tk.Radiobutton(frame_algoritmo, text="Prog. Dinámica", variable=var_algoritmo, value="modciPD").pack(side=tk.LEFT)
tk.Radiobutton(frame_algoritmo, text="Voraz", variable=var_algoritmo, value="modciV").pack(side=tk.LEFT)
frame_algoritmo.pack()

# Botón para ejecutar el algoritmo
btn_ejecutar = tk.Button(root, text="Ejecutar", command=ejecutar_algoritmo)
btn_ejecutar.pack()

# Área de texto para mostrar resultados
text_resultado = tk.Text(root, height=6, width=50, state="disabled")
text_resultado.pack()

# Iniciar la aplicación
root.mainloop()
