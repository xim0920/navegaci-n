import tkinter as tk
from tkinter import messagebox

# -------------------------------------------------------
# CONFIGURACIÓN DE COLORES
# -------------------------------------------------------
COLOR_FONDO = "#F5EEDC"   # beige
COLOR_AZUL = "#0A1A2F"    # azul marino
COLOR_GRIS = "#7A7A7A"    # gris
COLOR_NEGRO = "#000000"   # negro

# -------------------------------------------------------
# CONFIGURACIÓN DE LOGIN (EDITABLE)
# -------------------------------------------------------
USUARIO_DUENO = "dueno"
CONTRASENA_DUENO = "FoodVide2025"


# -------------------------------------------------------
# FUNCIÓN: VENTANA "OLVIDASTE TU CONTRASEÑA"
# -------------------------------------------------------
def ventana_olvido():
    rec = tk.Toplevel()
    rec.title("Recuperar contraseña")
    rec.geometry("350x250")
    rec.configure(bg=COLOR_FONDO)

    tk.Label(rec, text="Recuperar contraseña", font=("Arial", 16,"bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

    tk.Label(rec, text="Ingresa tu correo:", font=("Arial", 12),
             bg=COLOR_FONDO, fg=COLOR_NEGRO).pack()

    correo = tk.Entry(rec, width=30)
    correo.pack(pady=10)

    def enviar():
        messagebox.showinfo("Listo", "Se envió un correo para recuperar tu contraseña.")
        rec.destroy()

    tk.Button(rec, text="Enviar", bg=COLOR_AZUL, fg="white",
              font=("Arial", 12, "bold"), width=12, command=enviar).pack(pady=15)


# -------------------------------------------------------
# FUNCIÓN: PERFIL
# -------------------------------------------------------
def ventana_perfil():
    perfil = tk.Toplevel()
    perfil.title("Mi Perfil - FOODVIDE")
    perfil.geometry("350x300")
    perfil.configure(bg=COLOR_FONDO)

    tk.Label(perfil, text="Mi Perfil", font=("Arial", 20, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

    tk.Label(perfil,
             text="Nombre: Administrador\nCargo: Dueño\nCorreo: owner@foodvide.com",
             font=("Arial", 12), bg=COLOR_FONDO, fg=COLOR_NEGRO).pack(pady=10)

    tk.Button(perfil, text="Cerrar", bg=COLOR_AZUL, fg="white",
              width=12, command=perfil.destroy).pack(pady=20)


# -------------------------------------------------------
# FUNCIÓN: CONTACTO
# -------------------------------------------------------
def ventana_contacto():
    cont = tk.Toplevel()
    cont.title("Contacto FOODVIDE")
    cont.geometry("380x420")
    cont.configure(bg=COLOR_FONDO)

    tk.Label(cont, text="Formulario de Contacto", font=("Arial", 18, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

    tk.Label(cont, text="Tu nombre:", bg=COLOR_FONDO, fg=COLOR_NEGRO).pack()
    nom = tk.Entry(cont, width=35)
    nom.pack(pady=5)

    tk.Label(cont, text="Tu correo:", bg=COLOR_FONDO, fg=COLOR_NEGRO).pack()
    corr = tk.Entry(cont, width=35)
    corr.pack(pady=5)

    tk.Label(cont, text="Mensaje:", bg=COLOR_FONDO, fg=COLOR_NEGRO).pack()
    msg = tk.Text(cont, width=40, height=8)
    msg.pack(pady=5)

    def enviar():
        messagebox.showinfo("Enviado", "Tu mensaje fue enviado correctamente.")
        cont.destroy()

    tk.Button(cont, text="Enviar", bg=COLOR_AZUL, fg="white", width=12,
              font=("Arial", 12), command=enviar).pack(pady=15)


# -------------------------------------------------------
# FUNCIÓN: ESTADÍSTICAS
# -------------------------------------------------------
def ventana_estadisticas():
    est = tk.Toplevel()
    est.title("Estadísticas FOODVIDE")
    est.geometry("380x420")
    est.configure(bg=COLOR_FONDO)

    tk.Label(est, text="Estadísticas del Día", font=("Arial", 20, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=20)

    datos = """
💰 Ventas de hoy: $1,850.75
📦 Inventario restante: 65%
👥 Empleados activos: 5
⭐ Calificación promedio: 4.8/5
🍽️ Platos vendidos hoy: 132
"""

    tk.Label(est, text=datos, font=("Arial", 13),
             bg=COLOR_FONDO, fg=COLOR_NEGRO, justify="left").pack(pady=10)

    tk.Button(est, text="Cerrar", bg=COLOR_AZUL, fg="white",
              width=12, command=est.destroy).pack(pady=20)


# -------------------------------------------------------
# FUNCIÓN: PANEL DEL DUEÑO
# -------------------------------------------------------
def ventana_panel():
    panel = tk.Toplevel()
    panel.title("Panel del Dueño - FOODVIDE")
    panel.geometry("420x450")
    panel.configure(bg=COLOR_FONDO)

    tk.Label(panel, text="FOODVIDE - Panel del Dueño",
             font=("Arial", 20, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=25)

    tk.Button(panel, text="📊 Ver estadísticas", width=20, height=2,
              bg=COLOR_AZUL, fg="white", command=ventana_estadisticas).pack(pady=10)

    tk.Button(panel, text="👤 Mi perfil", width=20, height=2,
              bg=COLOR_AZUL, fg="white", command=ventana_perfil).pack(pady=10)

    tk.Button(panel, text="📨 Contacto", width=20, height=2,
              bg=COLOR_AZUL, fg="white", command=ventana_contacto).pack(pady=10)

    tk.Button(panel, text="Cerrar sesión", width=12, height=1,
              bg=COLOR_NEGRO, fg="white", command=panel.destroy).pack(pady=25)


# -------------------------------------------------------
# FUNCIÓN: LOGIN
# -------------------------------------------------------
def abrir_login():
    login = tk.Toplevel()
    login.title("Login FOODVIDE")
    login.geometry("380x350")
    login.configure(bg=COLOR_FONDO)

    tk.Label(login, text="Iniciar Sesión", font=("Arial", 20, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=20)

    tk.Label(login, text="Usuario:", bg=COLOR_FONDO, fg=COLOR_NEGRO).pack()
    usuario = tk.Entry(login, width=30)
    usuario.pack(pady=5)

    tk.Label(login, text="Contraseña:", bg=COLOR_FONDO, fg=COLOR_NEGRO).pack()
    contra = tk.Entry(login, width=30, show="*")
    contra.pack(pady=5)

    def entrar():
        if usuario.get() == USUARIO_DUENO and contra.get() == CONTRASENA_DUENO:
            messagebox.showinfo("Bienvenido", "Acceso concedido")
            ventana_panel()
            login.destroy()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(login, text="Entrar", bg=COLOR_AZUL, fg="white",
              font=("Arial", 12), width=12, command=entrar).pack(pady=20)

    tk.Button(login, text="¿Olvidaste tu contraseña?",
              bg=COLOR_FONDO, fg=COLOR_AZUL, relief="flat",
              command=ventana_olvido).pack()


# -------------------------------------------------------
# PÁGINA DE INICIO
# -------------------------------------------------------
def abrir_inicio():
    inicio = tk.Tk()
    inicio.title("FOODVIDE - Inicio")
    inicio.geometry("420x380")
    inicio.configure(bg=COLOR_FONDO)

    tk.Label(inicio, text="FOODVIDE", font=("Arial", 30, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=25)

    tk.Label(inicio,
             text="Sistema de Administración del Restaurante",
             font=("Arial", 12),
             bg=COLOR_FONDO, fg=COLOR_GRIS).pack()

    tk.Button(inicio, text="Entrar al sistema",
              font=("Arial", 14, "bold"),
              bg=COLOR_AZUL, fg="white", width=18, height=2,
              command=abrir_login).pack(pady=40)

    tk.Button(inicio, text="Contacto",
              font=("Arial", 11),
              bg=COLOR_GRIS, fg="white", width=12,
              command=ventana_contacto).pack()

    inicio.mainloop()


# -------------------------------------------------------
# EJECUTAR PROGRAMA
# -------------------------------------------------------
abrir_inicio()