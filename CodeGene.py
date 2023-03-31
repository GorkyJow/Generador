import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip


def generar_contrasena():
    longitud = int(longitud_entry.get())
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for i in range(longitud))
    if any(c.isupper() for c in password):
        etiqueta_contrasena.config(text=password)
    else:
        generar_contrasena()

def copiar_contrasena():
    pyperclip.copy(etiqueta_contrasena.cget("text"))
    messagebox.showinfo("Copiar Contraseña", "Contraseña copiada al portapapeles")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de contraseñas")
ventana.geometry("400x300")
ventana.iconbitmap("icono.ico")

# Frame para la entrada de la longitud de la contraseña
frame_longitud = ttk.Frame(ventana)
frame_longitud.pack(pady=20)

etiqueta_longitud = ttk.Label(frame_longitud, text="Longitud de la contraseña:")
etiqueta_longitud.pack(side=tk.LEFT, padx=10)

longitud_entry = ttk.Entry(frame_longitud, width=3)
longitud_entry.insert(tk.END, "12")
longitud_entry.pack(side=tk.LEFT)

# Frame para la generación de contraseñas y copiado de las mismas
frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=20)

boton_generar = ttk.Button(frame_botones, text="Generar Contraseña", command=generar_contrasena)
boton_generar.pack(side=tk.LEFT, padx=10)

boton_copiar = ttk.Button(frame_botones, text="Copiar Contraseña", command=copiar_contrasena)
boton_copiar.pack(side=tk.LEFT, padx=10)

# Etiqueta para mostrar la contraseña generada
etiqueta_contrasena = ttk.Label(ventana, font=("Arial", 16), anchor="center")
etiqueta_contrasena.pack(pady=10)

# Configuración del estilo visual
style = ttk.Style()
style.configure("TLabel", background="#ffffff", foreground="#000000", font=("Arial", 12), padding=10)
style.configure("TButton", background="#4d4d4d", foreground="#ffffff", font=("Arial", 12), padding=10, width=20)

# Bucle principal de la aplicación
ventana.mainloop()
