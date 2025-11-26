import tkinter as tk
from tkinter import messagebox

# -------------------------------------------------------
# COLORES
# -------------------------------------------------------
COLOR_FONDO = "#F5EEDC"
COLOR_AZUL = "#0A1A2F"
COLOR_GRIS = "#7A7A7A"
COLOR_NEGRO = "#000000"
COLOR_PANEL = "#102542"

USUARIO_DUENO = "dueno"
CONTRASENA_DUENO = "1234"


# -------------------------------------------------------
# MENÚ LATERAL HAMBURGUESA
# -------------------------------------------------------
def crear_menu_lateral(ventana, contenido_callback):
    panel = tk.Frame(ventana, bg=COLOR_PANEL, width=180)
    panel.pack(side="left", fill="y")

    tk.Label(panel, text="🍔 MENÚ", font=("Arial", 18, "bold"),
             bg=COLOR_PANEL, fg="white").pack(pady=20)

    def add_btn(texto, comando):
        tk.Button(panel, text=texto, width=18, bg=COLOR_AZUL, fg="white",
                  relief="flat", font=("Arial", 12), command=comando).pack(pady=10)

    add_btn("🏠 Inicio", contenido_callback["inicio"])
    add_btn("📊 Estadísticas", contenido_callback["estadisticas"])
    add_btn("👤 Mi perfil", contenido_callback["perfil"])
    add_btn("📨 Contacto", contenido_callback["contacto"])
    add_btn("⬅ Cerrar sesión", contenido_callback["cerrar"])


# -------------------------------------------------------
# PÁGINA DE INICIO
# -------------------------------------------------------
def pagina_inicio(contenedor):
    for widget in contenedor.winfo_children():
        widget.destroy()

    tk.Label(contenedor, text="FOODVIDE",
             font=("Arial", 28, "bold"), fg=COLOR_AZUL, bg=COLOR_FONDO).pack(pady=15)

    tk.Label(contenedor, text="Misión", font=("Arial", 18, "bold"),
             bg=COLOR_FONDO, fg=COLOR_NEGRO).pack()
    tk.Label(contenedor, text="Ofrecer alimentos de alta calidad con un servicio excepcional.",
             font=("Arial", 12), bg=COLOR_FONDO).pack(pady=5)

    tk.Label(contenedor, text="Visión", font=("Arial", 18, "bold"),
             bg=COLOR_FONDO, fg=COLOR_NEGRO).pack(pady=10)
    tk.Label(contenedor, text="Ser líder en la industria gastronómica a nivel nacional.",
             font=("Arial", 12), bg=COLOR_FONDO).pack()

    tk.Label(contenedor, text="Ubicación: Angelópolis, Puebla",
             font=("Arial", 14, "bold"), bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

    tk.Label(contenedor, text="FOODVIDE © 2025",
             font=("Arial", 10), bg=COLOR_FONDO, fg=COLOR_GRIS).pack(side="bottom", pady=10)


# -------------------------------------------------------
# ESTADÍSTICAS
# -------------------------------------------------------
def pagina_estadisticas(contenedor):
    for w in contenedor.winfo_children():
        w.destroy()

    tk.Label(contenedor, text="Estadísticas del Día",
             font=("Arial", 24, "bold"), bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=20)

    datos = """
💰 Ventas de hoy: $1,850.75
📦 Inventario disponible: 65%
👥 Empleados activos: 5
⭐ Calificación promedio: 4.8/5
🍽️ Platos vendidos: 132
"""
    tk.Label(contenedor, text=datos, font=("Arial", 14),
             bg=COLOR_FONDO, fg=COLOR_NEGRO, justify="left").pack(pady=20)


# -------------------------------------------------------
# PERFIL
# -------------------------------------------------------
def pagina_perfil(contenedor):
    for w in contenedor.winfo_children():
        w.destroy()

    tk.Label(contenedor, text="Mi Perfil",
             font=("Arial", 26, "bold"), bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

    tk.Label(contenedor,
             text="Nombre: Administrador\nCargo: Dueño\nCorreo: owner@foodvide.com",
             font=("Arial", 14), bg=COLOR_FONDO, fg=COLOR_NEGRO).pack(pady=10)


# -------------------------------------------------------
# CONTACTO
# -------------------------------------------------------
def pagina_contacto(contenedor):
    for w in contenedor.winfo_children():
        w.destroy()

    tk.Label(contenedor, text="Formulario de Contacto",
             font=("Arial", 24, "bold"), bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

    tk.Label(contenedor, text="Nombre:", bg=COLOR_FONDO).pack()
    nom = tk.Entry(contenedor, width=40)
    nom.pack()

    tk.Label(contenedor, text="Correo:", bg=COLOR_FONDO).pack()
    corr = tk.Entry(contenedor, width=40)
    corr.pack()

    tk.Label(contenedor, text="Mensaje:", bg=COLOR_FONDO).pack()
    msg = tk.Text(contenedor, width=40, height=6)
    msg.pack(pady=10)

    def enviar():
        messagebox.showinfo("Enviado", "Tu mensaje fue enviado correctamente.")

    tk.Button(contenedor, text="Enviar", bg=COLOR_AZUL, fg="white",
              font=("Arial", 12), width=12, command=enviar).pack()


# -------------------------------------------------------
# PANEL PRINCIPAL (DUEÑO)
# -------------------------------------------------------
def ventana_panel():
    win = tk.Tk()
    win.title("FOODVIDE - Panel del Dueño")
    win.geometry("780x520")
    win.configure(bg=COLOR_FONDO)

    # Contenedor derecho
    contenido = tk.Frame(win, bg=COLOR_FONDO)
    contenido.pack(side="right", fill="both", expand=True)

    callbacks = {
        "inicio": lambda: pagina_inicio(contenido),
        "estadisticas": lambda: pagina_estadisticas(contenido),
        "perfil": lambda: pagina_perfil(contenido),
        "contacto": lambda: pagina_contacto(contenido),
        "cerrar": win.destroy
    }

    crear_menu_lateral(win, callbacks)
    pagina_inicio(contenido)

    win.mainloop()


# -------------------------------------------------------
# LOGIN
# -------------------------------------------------------
def login():
    log = tk.Tk()
    log.title("Login FOODVIDE")
    log.geometry("350x350")
    log.configure(bg=COLOR_FONDO)

    tk.Label(log, text="Iniciar Sesión",
             font=("Arial", 22, "bold"), fg=COLOR_AZUL, bg=COLOR_FONDO).pack(pady=20)

    tk.Label(log, text="Usuario:", bg=COLOR_FONDO).pack()
    user = tk.Entry(log, width=30)
    user.pack(pady=5)

    tk.Label(log, text="Contraseña:", bg=COLOR_FONDO).pack()
    pasw = tk.Entry(log, width=30, show="*")
    pasw.pack(pady=5)

    def entrar():
        if user.get() == USUARIO_DUENO and pasw.get() == CONTRASENA_DUENO:
            messagebox.showinfo("Bienvenido", "Acceso concedido")
            log.destroy()
            ventana_panel()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(log, text="Entrar", bg=COLOR_AZUL, fg="white",
              width=12, font=("Arial", 12), command=entrar).pack(pady=25)

    log.mainloop()


# -------------------------------------------------------
# EJECUTAR
# -------------------------------------------------------
login()