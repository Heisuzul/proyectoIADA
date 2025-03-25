import tkinter as tk
from tkinter import filedialog, messagebox, ttk
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
                text_red_social.insert(tk.END, "Red social cargada:\n")
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
root.geometry("600x500")  # Ajustar el tamaño de la ventana
root.configure(bg="#f4f4f4")  # Fondo estilo FlatLeaf

# Aplicar estilo FlatLeaf a todos los componentes
style = ttk.Style()
style.theme_use("clam")

# Estilo para botones
style.configure("TButton", 
                font=("Poppins", 12), 
                padding=10, 
                relief="flat", 
                background="#584caf", 
                foreground="white", 
                borderwidth=4, 
                focuscolor="none")
style.map("TButton", 
          background=[("active", "#8478da")])

# Estilo para etiquetas
style.configure("TLabel", 
                font=("Montserrat", 12), 
                background="#f4f4f4", 
                foreground="#333")

# Estilo para Radiobuttons
style.configure("TRadiobutton", 
                font=("Montserrat", 10), 
                background="#f4f4f4", 
                foreground="#333",
                indicatorcolor="#4CAF50")
style.map("TRadiobutton", 
          background=[("active", "#ddd")])

# Estilo para el área de texto
style.configure("TText", 
                font=("Poppins", 10), 
                background="white", 
                foreground="#333", 
                padding=5)

# Contenedor principal con padding
frame_principal = tk.Frame(root, padx=20, pady=20, bg="#f4f4f4")
frame_principal.pack(fill=tk.BOTH, expand=True)

# Botón para cargar archivo
btn_cargar = ttk.Button(frame_principal, text="Cargar Archivo", command=cargar_archivo)
btn_cargar.pack(pady=5)

# Área de texto para mostrar la red social
text_red_social = tk.Text(frame_principal, height=7, width=60, font=("Montserrat", 10), bg="white", fg="#333")
text_red_social.pack(pady=10)

# Selección de algoritmo con más separación
var_algoritmo = tk.StringVar(value="modciFB")
frame_algoritmo = tk.Frame(frame_principal, pady=10, bg="#f4f4f4")
ttk.Label(frame_algoritmo, text="Algoritmo:").pack(side=tk.LEFT, padx=5)
ttk.Radiobutton(frame_algoritmo, text="Fuerza Bruta", variable=var_algoritmo, value="modciFB").pack(side=tk.LEFT, padx=10)
ttk.Radiobutton(frame_algoritmo, text="Prog. Dinámica", variable=var_algoritmo, value="modciPD").pack(side=tk.LEFT, padx=10)
ttk.Radiobutton(frame_algoritmo, text="Voraz", variable=var_algoritmo, value="modciV").pack(side=tk.LEFT, padx=10)
frame_algoritmo.pack()

# Botón para ejecutar el algoritmo
btn_ejecutar = ttk.Button(frame_principal, text="Ejecutar", command=ejecutar_algoritmo)
btn_ejecutar.pack(pady=10)

# Área de texto para mostrar resultados
text_resultado = tk.Text(frame_principal, height=8, width=60, font=("Montserrat", 10), bg="white", fg="#333")
text_resultado.pack(pady=10)

# Iniciar la aplicación
root.mainloop()