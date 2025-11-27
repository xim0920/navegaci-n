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
# PIE DE PÁGINA
# -------------------------------------------------------
def pie_de_pagina(contenedor):
    tk.Label(contenedor,
             text="FOODVIDE © 2025 - Todos los derechos reservados",
             font=("Arial", 10),
             bg=COLOR_FONDO,
             fg=COLOR_GRIS).pack(side="bottom", pady=10)

# -------------------------------------------------------
# MENÚ LATERAL
# -------------------------------------------------------
def crear_menu_lateral(ventana, contenido_callback):
    panel = tk.Frame(ventana, bg=COLOR_PANEL, width=180)
    panel.pack(side="left", fill="y")

    tk.Label(panel, text="🍔 MENÚ",
             font=("Arial", 18, "bold"),
             bg=COLOR_PANEL, fg="white").pack(pady=20)

    def add_btn(txt, cmd):
        tk.Button(panel, text=txt, width=18,
                  bg=COLOR_AZUL, fg="white",
                  relief="flat", font=("Arial", 12),
                  command=cmd).pack(pady=10)

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
             font=("Arial", 28, "bold"),
             fg=COLOR_AZUL, bg=COLOR_FONDO).pack(pady=15)

    # Misión
    tk.Label(contenedor, text="Misión",
             font=("Arial", 18, "bold"),
             bg=COLOR_FONDO, fg=COLOR_NEGRO).pack()

    tk.Label(contenedor,
             text="Ofrecer alimentos de alta calidad con un servicio excepcional.",
             font=("Arial", 12),
             bg=COLOR_FONDO).pack(pady=5)

    # Visión
    tk.Label(contenedor, text="Visión",
             font=("Arial", 18, "bold"),
             bg=COLOR_FONDO, fg=COLOR_NEGRO).pack(pady=10)

    tk.Label(contenedor,
             text="Ser líder en la industria gastronómica a nivel nacional.",
             font=("Arial", 12),
             bg=COLOR_FONDO).pack()

    # Imagen FOODVIDE
    ruta_img = "C:/Users/1104960894/Desktop/foodvide.png"

    try:
        img = tk.PhotoImage(file=ruta_img)
        lbl = tk.Label(contenedor, image=img, bg=COLOR_FONDO)
        lbl.image = img
        lbl.pack(pady=15)
    except:
        tk.Label(contenedor, text="Imagen no encontrada",
                 font=("Arial", 12),
                 fg="red", bg=COLOR_FONDO).pack(pady=15)

    tk.Label(contenedor, text="Ubicación: Angelópolis, Puebla",
             font=("Arial", 14, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

    pie_de_pagina(contenedor)

# -------------------------------------------------------
# ESTADÍSTICAS
# -------------------------------------------------------
def pagina_estadisticas(contenedor):
    for w in contenedor.winfo_children():
        w.destroy()

    tk.Label(contenedor, text="📊 Estadísticas Generales",
             font=("Arial", 24, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=20)

    # -------------------------------------------
    # Ventas del día
    # -------------------------------------------
    def mostrar_dia():
        for w in contenedor.winfo_children():
            w.destroy()

        tk.Label(contenedor, text="💰 Ventas del Día",
                 font=("Arial", 22, "bold"),
                 bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=10)

        tk.Label(contenedor,
                 text="Hoy se vendieron: $1,850.75",
                 font=("Arial", 14),
                 bg=COLOR_FONDO).pack(pady=10)

        pie_de_pagina(contenedor)

    # -------------------------------------------
    # Ventas mensuales
    # -------------------------------------------
    def mostrar_mensual():
        for w in contenedor.winfo_children():
            w.destroy()

        tk.Label(contenedor, text="📆 Ventas Mensuales",
                 font=("Arial", 22, "bold"),
                 bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=10)

        tk.Label(contenedor,
                 text="Ingresos del mes: $52,340.00",
                 font=("Arial", 14),
                 bg=COLOR_FONDO).pack(pady=10)

        pie_de_pagina(contenedor)

    # -------------------------------------------
    # Gráfica manual SIN matplotlib
    # -------------------------------------------
    def mostrar_grafica():
        for w in contenedor.winfo_children():
            w.destroy()

        tk.Label(contenedor, text="📈 Gráfica de Ventas (Simulada)",
                 font=("Arial", 22, "bold"),
                 bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=10)

        canvas = tk.Canvas(contenedor, width=500, height=300, bg="white")
        canvas.pack(pady=20)

        ventas = [120, 150, 170, 200, 250, 300, 280]
        x = 50

        for i in range(len(ventas) - 1):
            canvas.create_line(
                x, 300 - ventas[i] * 0.5,
                x + 60, 300 - ventas[i + 1] * 0.5,
                fill="purple", width=3
            )
            x += 60

        x = 50
        for v in ventas:
            canvas.create_oval(
                x - 5, 300 - v * 0.5 - 5,
                x + 5, 300 - v * 0.5 + 5,
                fill="purple"
            )
            x += 60

        pie_de_pagina(contenedor)

    # -------------------------------------------
    # BOTONES DE ESTADÍSTICAS
    # -------------------------------------------
    tk.Button(contenedor, text="💰 Ventas del Día",
              bg=COLOR_AZUL, fg="white",
              font=("Arial", 14), width=20,
              command=mostrar_dia).pack(pady=10)

    tk.Button(contenedor, text="📆 Informe Mensual",
              bg=COLOR_AZUL, fg="white",
              font=("Arial", 14), width=20,
              command=mostrar_mensual).pack(pady=10)

    tk.Button(contenedor, text="📈 Gráficas",
              bg=COLOR_AZUL, fg="white",
              font=("Arial", 14), width=20,
              command=mostrar_grafica).pack(pady=10)

    pie_de_pagina(contenedor)

# -------------------------------------------------------
# PERFIL
# -------------------------------------------------------
def pagina_perfil(contenedor):
    for w in contenedor.winfo_children():
        w.destroy()

    tk.Label(contenedor, text="Mi Perfil",
             font=("Arial", 26, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

    tk.Label(contenedor, text="Nombre:", bg=COLOR_FONDO).pack()
    entry_nom = tk.Entry(contenedor, width=30)
    entry_nom.insert(0, "Administrador")
    entry_nom.pack(pady=5)

    tk.Label(contenedor, text="Cargo:", bg=COLOR_FONDO).pack()
    entry_cargo = tk.Entry(contenedor, width=30)
    entry_cargo.insert(0, "Dueño")
    entry_cargo.pack(pady=5)

    tk.Label(contenedor, text="Correo:", bg=COLOR_FONDO).pack()
    entry_correo = tk.Entry(contenedor, width=30)
    entry_correo.insert(0, "owner@foodvide.com")
    entry_correo.pack(pady=5)

    def guardar():
        messagebox.showinfo("Guardado",
                            "Datos actualizados correctamente.")

    tk.Button(contenedor, text="Guardar Cambios",
              bg=COLOR_AZUL, fg="white",
              font=("Arial", 12),
              command=guardar).pack(pady=20)

    pie_de_pagina(contenedor)

# -------------------------------------------------------
# CONTACTO
# -------------------------------------------------------
def pagina_contacto(contenedor):
    for w in contenedor.winfo_children():
        w.destroy()

    tk.Label(contenedor, text="Formulario de Contacto",
             font=("Arial", 24, "bold"),
             bg=COLOR_FONDO, fg=COLOR_AZUL).pack(pady=15)

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

    tk.Button(contenedor, text="Enviar",
              bg=COLOR_AZUL, fg="white",
              font=("Arial", 12), width=12,
              command=enviar).pack()

    pie_de_pagina(contenedor)

# -------------------------------------------------------
# PANEL PRINCIPAL
# -------------------------------------------------------
def ventana_panel():
    win = tk.Tk()
    win.title("FOODVIDE - Panel del Dueño")
    win.geometry("780x520")
    win.configure(bg=COLOR_FONDO)

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
             font=("Arial", 22, "bold"),
             fg=COLOR_AZUL,
             bg=COLOR_FONDO).pack(pady=20)

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

    tk.Button(log, text="Entrar",
              bg=COLOR_AZUL, fg="white",
              width=12, font=("Arial", 12),
              command=entrar).pack(pady=25)

    log.mainloop()

# -------------------------------------------------------
# EJECUTAR
# -------------------------------------------------------
login()
