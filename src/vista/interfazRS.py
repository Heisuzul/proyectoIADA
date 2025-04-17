import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.logica.utils import leer_archivo_entrada, aplicar_estrategia
from src.logica.modciFB import modciFB
from src.logica.modciV import modciV
from src.logica.modciPD import modciPD

# Variable global para guardar la red cargada
red_social = None


def guardar_resultado_txt(estrategia, esfuerzo, conflicto, algoritmo):
    try:
        nombres_archivos = {
            "modciFB": "salida_FB.txt",
            "modciV": "salida_V.txt",
            "modciPD": "salida_PD.txt"
        }

        nombre_archivo = nombres_archivos.get(algoritmo, "salida.txt")
        ruta_salida = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data", nombre_archivo))

        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

        with open(ruta_salida, "w") as archivo:
            archivo.write(f"{conflicto}\n")
            archivo.write(f"{esfuerzo}\n")
            for e in estrategia:
                archivo.write(f"{e}\n")

        print(f"[INFO] Resultado guardado automáticamente en {ruta_salida}")
    except Exception as e:
        print(f"[ERROR] Al guardar el archivo de salida: {e}")




def cargar_archivo():
    try:
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            global red_social
            red_social = leer_archivo_entrada(ruta)
            if red_social:
                text_red_social.config(state="normal")
                text_red_social.delete("1.0", tk.END)
                text_red_social.insert(tk.END, "Red social cargada:\n")
                text_red_social.insert(tk.END, str(red_social))
                text_red_social.config(state="disabled")
                lbl_ruta.config(text=f"Archivo cargado: {os.path.basename(ruta)}")
    except Exception as e:
        print(f"[ERROR] Al cargar el archivo: {e}")  # útil en consola
        messagebox.showerror("Error", f"Error al cargar el archivo:\n{e}")

def ejecutar_algoritmo():
    if red_social is None:
        messagebox.showwarning("Advertencia", "Carga primero un archivo de red social")
        return
    
    algoritmo = var_algoritmo.get()
    resultado = None

    try:
        if algoritmo == "modciFB":
            resultado = modciFB(red_social)
        elif algoritmo == "modciV":
            resultado = modciV(red_social)
        elif algoritmo == "modciPD":
            resultado = modciPD(red_social)
        
        if resultado:
            mejor_estrategia, mejor_esfuerzo, mejor_conflicto = resultado
            # Aplicar estrategia para obtener la nueva red social
            nueva_red_social = aplicar_estrategia(red_social, mejor_estrategia)
            #**Actualizar número de grupos después de calcular la nueva red**
            nueva_red_social = (len(nueva_red_social[1]), nueva_red_social[1], nueva_red_social[2])
            # Mostrar resultados
            text_resultado.config(state="normal")
            text_resultado.delete("1.0", tk.END)
            text_resultado.insert(tk.END, f"Mejor estrategia: {mejor_estrategia}\n")
            text_resultado.insert(tk.END, f"Esfuerzo requerido: {mejor_esfuerzo}\n")
            text_resultado.insert(tk.END, f"Conflicto Interno: {mejor_conflicto}\n")
            text_resultado.insert(tk.END, f"Nueva red social: {nueva_red_social}")
            text_resultado.config(state="disabled")
            
            
            guardar_resultado_txt(mejor_estrategia, mejor_esfuerzo, mejor_conflicto, algoritmo)

    except Exception as e:
        print(f"[ERROR] Al ejecutar el algoritmo: {e}")
        messagebox.showerror("Error", f"Error al ejecutar el algoritmo:\n{e}")


# Configurar ventana principal

root = tk.Tk()
root.title("Red Social - Análisis de Conflicto Interno")
root.geometry("600x550")
root.configure(bg="#f4f4f4")
# Aplicar estilo FlatLeaf a todos los componentes
style = ttk.Style()
style.theme_use("clam")

# Estilo para botones
style.configure("TButton", font=("Poppins", 12), padding=10,
                relief="flat", background="#584caf", foreground="white")
style.map("TButton", background=[("active", "#8478da")])
# Estilo para etiquetas
style.configure("TLabel", font=("Montserrat", 12), background="#f4f4f4", foreground="#333")
# Estilo para Radiobuttons
style.configure("TRadiobutton", font=("Montserrat", 10), background="#f4f4f4", foreground="#333")
# Estilo para el área de texto
style.configure("TText", font=("Poppins", 10), background="white", foreground="#333", padding=5)

# Contenedor principal con padding

frame_principal = tk.Frame(root, padx=20, pady=20, bg="#f4f4f4")
frame_principal.pack(fill=tk.BOTH, expand=True)
# Boton para cargar archivo
btn_cargar = ttk.Button(frame_principal, text="Cargar Archivo", command=cargar_archivo)
btn_cargar.pack(pady=5)

lbl_ruta = ttk.Label(frame_principal, text="Esperando archivo...", font=("Montserrat", 10))
lbl_ruta.pack(pady=5)
# Área de texto para mostrar la red social
text_red_social = tk.Text(frame_principal, height=7, width=60, font=("Montserrat", 10), bg="white", fg="#333")
text_red_social.pack(pady=10)
# Selección de Algoritmo con más separación
var_algoritmo = tk.StringVar(value="modciFB")
frame_algoritmo = tk.Frame(frame_principal, pady=10, bg="#f4f4f4")
ttk.Label(frame_algoritmo, text="Algoritmo:").pack(side=tk.LEFT, padx=5)
ttk.Radiobutton(frame_algoritmo, text="Fuerza Bruta", variable=var_algoritmo, value="modciFB").pack(side=tk.LEFT, padx=10)
ttk.Radiobutton(frame_algoritmo, text="Prog. Dinámica", variable=var_algoritmo, value="modciPD").pack(side=tk.LEFT, padx=10)
ttk.Radiobutton(frame_algoritmo, text="Voraz", variable=var_algoritmo, value="modciV").pack(side=tk.LEFT, padx=10)
frame_algoritmo.pack()
# Boton para ejecutar el algoritmo
btn_ejecutar = ttk.Button(frame_principal, text="Ejecutar", command=ejecutar_algoritmo)
btn_ejecutar.pack(pady=10)
# Area de texto para mostrar resultados
text_resultado = tk.Text(frame_principal, height=8, width=60, font=("Montserrat", 10), bg="white", fg="#333")
text_resultado.pack(pady=10)

# Iniciar la aplicación
root.mainloop()