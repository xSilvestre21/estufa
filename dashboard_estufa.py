import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

dt = 1.0

T_amb = 25
T = 25
T_aquecedor = 25

SP = 35
h = 1.0

u = 0
sistema_ligado = True

tempo = []
temperatura = []
temp_aquecedor_hist = []

k = 0


def aumentar_sp():
    global SP
    SP += 1
    label_sp.config(text=f"{SP} °C")


def diminuir_sp():
    global SP
    SP -= 1
    label_sp.config(text=f"{SP} °C")


def ligar_desligar():

    global sistema_ligado

    sistema_ligado = not sistema_ligado

    if sistema_ligado:

        btn_power.config(
            text="DESLIGAR SISTEMA",
            bg="red"
        )

    else:

        btn_power.config(
            text="LIGAR SISTEMA",
            bg="green"
        )


def atualizar():

    global T, T_amb, u, k, T_aquecedor

    # Perturbação ambiente

    if 50 < k < 80:
        T_amb = 20
    else:
        T_amb = 25

    if sistema_ligado:

        if T <= (SP-h):
            u = 1

        elif T >= (SP+h):
            u = 0

    else:
        u = 0

    if u == 1:

        T_aquecedor += 0.12*(50 - T_aquecedor)

    else:
        T_aquecedor += 0.08*(T - T_aquecedor)

    ganho_aquecedor = (
        0.07*(T_aquecedor - T)
    )

    perda_ambiente = (
        0.025*(T_amb - T)
    )

    T = T + ganho_aquecedor + perda_ambiente

    tempo.append(k)
    temperatura.append(T)
    temp_aquecedor_hist.append(T_aquecedor)

    if not sistema_ligado:

        status = "DESLIGADO"

    elif u == 1:

        status = "AQUECENDO"

    else:

        status = "TEMPERATURA CONTROLADA"

    label_temp.config(
        text=f"{T:.2f} °C"
    )

    label_aquecedor.config(
        text=f"{T_aquecedor:.2f} °C"
    )

    label_status.config(
        text=status
    )

    ax.clear()

    ax.plot(
        tempo,
        temperatura,
        label="Temperatura Estufa"
    )

    ax.plot(
        tempo,
        temp_aquecedor_hist,
        label="Temperatura Aquecedor"
    )

    ax.axhline(
        SP,
        linestyle='--',
        label='SetPoint'
    )

    ax.axhline(
        SP+h,
        linestyle=':',
        label='36°C'
    )

    ax.axhline(
        SP-h,
        linestyle=':',
        label='34°C'
    )

    ax.set_ylim(20, 55)

    ax.grid()
    ax.legend()

    canvas.draw()

    k += 1

    root.after(500, atualizar)


root = tk.Tk()
root.title("Painel da Estufa 🌱🔥")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(
    frame,
    text="Temperatura Estufa",
    font=("Arial", 14)
).pack()

label_temp = tk.Label(
    frame,
    text="-- °C",
    font=("Arial", 24)
)

label_temp.pack()

tk.Label(
    frame,
    text="Temperatura Aquecedor",
    font=("Arial", 14)
).pack()

label_aquecedor = tk.Label(
    frame,
    text="-- °C",
    font=("Arial", 24)
)

label_aquecedor.pack()

tk.Label(
    frame,
    text="Status",
    font=("Arial", 14)
).pack()

label_status = tk.Label(
    frame,
    text="--",
    font=("Arial", 18)
)

label_status.pack()

tk.Label(
    frame,
    text="SetPoint",
    font=("Arial", 14)
).pack()

label_sp = tk.Label(
    frame,
    text=f"{SP} °C",
    font=("Arial", 20)
)

label_sp.pack()

frame_sp = tk.Frame(frame)
frame_sp.pack()

tk.Button(
    frame_sp,
    text="-",
    width=5,
    command=diminuir_sp
).pack(side="left")

tk.Button(
    frame_sp,
    text="+",
    width=5,
    command=aumentar_sp
).pack(side="left")

btn_power = tk.Button(
    frame,
    text="DESLIGAR SISTEMA",
    bg="red",
    fg="white",
    font=("Arial", 12),
    command=ligar_desligar
)

btn_power.pack(pady=10)

fig, ax = plt.subplots(figsize=(7, 4))

canvas = FigureCanvasTkAgg(
    fig,
    master=root
)

canvas.get_tk_widget().pack()

atualizar()

root.mainloop()
