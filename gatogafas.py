# Pequeño proyecto casero para simular una parte de un programa de televisión sencillo y muy friendly.

import tkinter as tk

# ---------------- CONFIGURACIÓN ----------------
CASILLAS = [
    "Cazador",
    "4000",
    "2000",
    "1000",
    "500",
    "300",
    "200",
    "100",
    "CASA"
]

CASILLAS_SIN_TEXTO = {"300", "200", "100"}

ALTURA_CASILLA = 50
ANCHO = 200

# ---------------- ESTADO ----------------
pos_jugador = None
pos_cazador = 0

# ---------------- FUNCIONES ----------------
def dibujar_tablero():
    canvas.delete("all")

    for i, texto in enumerate(CASILLAS):
        y1 = i * ALTURA_CASILLA
        y2 = y1 + ALTURA_CASILLA

        color = "white"

        if texto == "CASA":
            color = "lightgreen"

        if i <= pos_cazador:
            color = "lightcoral"

        if pos_jugador == i:
            color = "lightgreen"

        canvas.create_rectangle(
            10, y1 + 10, ANCHO - 10, y2,
            fill=color
        )

        # Dibujar texto solo si es relevante
        if texto not in CASILLAS_SIN_TEXTO:
            canvas.create_text(
                ANCHO // 2,
                y1 + ALTURA_CASILLA // 2 + 5,
                text=texto,
                font=("Arial", 12, "bold")
            )

def elegir_inicio(valor):
    global pos_jugador
    pos_jugador = CASILLAS.index(valor)

    # Eliminar botones de inicio
    for boton in botones_inicio:
        boton.destroy()
    botones_inicio.clear()

    label_inicio.config(text="Jugador en juego")

    dibujar_tablero()

def jugador_avanza():
    global pos_jugador
    if pos_jugador is not None and pos_jugador < len(CASILLAS) - 1:
        pos_jugador += 1
        dibujar_tablero()

def cazador_avanza():
    global pos_cazador
    if pos_cazador < len(CASILLAS) - 1:
        pos_cazador += 1
        dibujar_tablero()

def resetear():
    global pos_jugador, pos_cazador
    pos_jugador = None
    pos_cazador = 0

    # Volver a mostrar botones de inicio
    label_inicio.config(text="Inicio jugador")
    crear_botones_inicio()

    dibujar_tablero()

def crear_botones_inicio():
    botones_inicio.clear()
    for v in ["4000", "2000", "1000", "500"]:
        b = tk.Button(
            botones,
            text=v,
            width=12,
            command=lambda x=v: elegir_inicio(x)
        )
        b.pack(pady=2)
        botones_inicio.append(b)

# ---------------- INTERFAZ ----------------
root = tk.Tk()
root.title("El Cazador")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Panel izquierdo
botones = tk.Frame(frame)
botones.pack(side="left", padx=10)

label_inicio = tk.Label(botones, text="Inicio jugador")
label_inicio.pack(pady=5)

botones_inicio = []
crear_botones_inicio()

tk.Button(botones, text="Jugador avanza", command=jugador_avanza).pack(pady=10)
tk.Button(botones, text="Cazador avanza", command=cazador_avanza).pack(pady=2)
tk.Button(botones, text="Reset", command=resetear).pack(pady=10)

# Columna derecha
canvas = tk.Canvas(
    frame,
    width=ANCHO,
    height=ALTURA_CASILLA * len(CASILLAS)
)
canvas.pack(side="right")

dibujar_tablero()


# root = tk.Tk()

# root.geometry("1200x800")
# root.title("Gato Gafas")


root.mainloop()
