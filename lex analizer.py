import tkinter as tk
from tkinter import scrolledtext
import re


def analizador_lexico(cadena):
    # Definición de patrones para palabras clave y símbolos
    patrones = [
        (r'for', 'reservada for'),
        (r'if', 'reservada if'),
        (r'do', 'reservada do'),
        (r'while', 'reservada while'),
        (r'else', 'reservada else'),
        (r'\(', 'paréntesis izquierdo'),
        (r'\)', 'paréntesis derecho'),
        (r'\s+', None),  # Ignorar espacios en blanco
        (r'\w+', 'identificador'),  # Identificadores
    ]

    tokens = []
    while cadena:
        encontrado = False
        for patron, tipo in patrones:
            match = re.match(patron, cadena)
            if match:
                encontrado = True
                valor = match.group(0)
                if tipo:
                    tokens.append((valor, tipo))
                break
        if not encontrado:
            tokens.append((cadena[0], 'error'))
            break
        cadena = cadena[match.end():]

    return tokens


def analizar():
    entrada = entrada_text.get("1.0", tk.END).strip()
    tokens = analizador_lexico(entrada)
    salida_text.delete("1.0", tk.END)
    for token, tipo in tokens:
        salida_text.insert(tk.END, f"{token}: {tipo}\n")


# Configuración de la interfaz de usuario
root = tk.Tk()
root.title("Analizador Léxico")

frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

label_entrada = tk.Label(frame_entrada, text="Introduce los tokens:")
label_entrada.grid(row=0, column=0)

entrada_text = scrolledtext.ScrolledText(frame_entrada, width=40, height=5)
entrada_text.grid(row=0, column=1)

boton_analizar = tk.Button(root, text="Analizar", command=analizar)
boton_analizar.pack(pady=5)

frame_salida = tk.Frame(root)
frame_salida.pack(pady=10)

label_salida = tk.Label(frame_salida, text="Salida:")
label_salida.pack()

salida_text = scrolledtext.ScrolledText(frame_salida, width=40, height=10)
salida_text.pack()

root.mainloop()
