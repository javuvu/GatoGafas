# Pequeño proyecto casero para simular una parte de un programa de televisión sencillo y muy friendly.

import tkinter as tk


inicio_elegido = None

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

ALTURA_CASILLA = 100
ANCHO = 400

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

        # ---------- TEXTO ----------
        mostrar_texto = True


        # Ocultar cantidades no elegidas
        if texto in {"4000", "2000", "1000", "500"}:
            if texto != inicio_elegido:
                mostrar_texto = False

        # Ocultar texto en casillas intermedias
        if texto in CASILLAS_SIN_TEXTO:
            mostrar_texto = False

        if mostrar_texto:
            canvas.create_text(
                ANCHO // 2,
                y1 + ALTURA_CASILLA // 2 + 5,
                #text=texto,
                font=("Arial", 30, "bold")
            )



        # ---------- TEXTO ----------
        texto_a_mostrar = None

        # CASA siempre visible
        if texto == "CASA":
            texto_a_mostrar = "CASA"

        # Mostrar el importe elegido SOLO donde está el jugador
        elif i == pos_jugador and inicio_elegido is not None:
            texto_a_mostrar = inicio_elegido

        # Mostrar "Cazador" solo arriba
        elif texto == "Cazador":
            texto_a_mostrar = "Cazador"

        if texto_a_mostrar:
            canvas.create_text(
                ANCHO // 2,
                y1 + ALTURA_CASILLA // 2 + 5,
                text=texto_a_mostrar,
                font=("Arial", 30, "bold")
            )



def elegir_inicio(valor):
    global pos_jugador, inicio_elegido
    inicio_elegido = valor
    pos_jugador = CASILLAS.index(valor)

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
    global pos_jugador, pos_cazador, inicio_elegido
    pos_jugador = None
    pos_cazador = 0
    inicio_elegido = None

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
root.geometry("1400x950")
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

tk.Button(botones, text="Cazador avanza", command=cazador_avanza).pack(pady=2)
tk.Button(botones, text="Jugador avanza", command=jugador_avanza).pack(pady=10)
tk.Button(botones, text="Reset", command=resetear).pack(pady=10)

# Columna derecha
canvas = tk.Canvas(
    frame,
    width=ANCHO,
    height=ALTURA_CASILLA * len(CASILLAS)
)
canvas.pack(side="right")

dibujar_tablero()


root.mainloop()
