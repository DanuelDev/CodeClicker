# Criar jogo cookie clicker
# Criar interface e dados

import tkinter as tk
from tkinter import messagebox

# variáveis globais
codes = 0
codes_per_click = 1

rtfm = 0
cost_rtfm = 10.0

cps = 0
cost_cps = 100.0
cps_update = 1000 # inicia 1 segundo de delay

server = 0
cost_server = 1000

# criar janela
window = tk.Tk()
window.title('Code Clicker')
window.iconbitmap('_internal/assets/icon.ico')
window.config(background='#292b38')
window.resizable(False, False)
#window.grid_rowconfigure(1, minsize=100)

# tamanho janela
window_width = 1000
window_height = 800

# obter informações do monitor e centralizar janela
window_x = window.winfo_screenwidth()
window_y = window.winfo_screenheight()
x = (window_x - window_width) // 2
y = (window_y - window_height) // 2

# calcular posição
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# update codes per second(cps)
def update():
    global codes, cps, cps_update, codes_per_click
    codes += (cps*codes_per_click)
    update_label()
    window.after(cps_update, update)

# adicionar cookie
def generate_code():
    global codes, codes_per_click
    codes += codes_per_click
    update_label()

# gerenciar vovós
def buy_RTFM():
    global codes, codes_per_click, rtfm, cost_rtfm
    if codes >= cost_rtfm:
        if rtfm == 0:
            messagebox.showinfo(title='New Update!', message='Read The F*cking Manual!\nCode 2x more efficient')
            button_robot.grid(row=2, column=2, pady=25)
            label_qnt_CPS.grid(row=2, column=3, pady=25)
        codes_per_click *= 2
        rtfm += 1
        codes -= cost_rtfm
        cost_rtfm = (cost_rtfm * (rtfm + 1)) / 2
        label_qnt_RTFM.config(
            text=
                f'RTFM: {rtfm}\n'
                f'cost: {cost_rtfm:,}'
        )
        update_label()

# comprar robos
def buy_CPS():
    global cps, codes, cost_cps
    if codes >= cost_cps:
        if cps == 0:
            messagebox.showinfo(title='Bot Jr.', message='Vibe coding is crap\n+1 code per second')
            button_server.grid(row=3, column=2, pady=25)
            label_qnt_server.grid(row=3, column=3, pady=25)
        cps += 1
        codes -= cost_cps
        cost_cps = (cost_cps * (cps + 2)) / 2
        label_qnt_CPS.config(
            text=
                f'AI Coder: {cps}\n'
                f'cost: {cost_cps:,}',
        )
        update_label()

# comprar servidor
def buy_server():
    global cps_update, cost_server, codes, server
    if codes >= cost_server and server < 19:
        if server == 0:
            messagebox.showinfo(title='Overclock', message='Just install Linux ;)')
        codes -= cost_server
        server += 1
        cps_update -= 50
        cost_server *= 2
        label_qnt_server.config(
            text=
                f'Server: {server}\n'
                f'cost: {cost_server:,}',
        )
        update_label()
    elif server == 19:
        label_qnt_server.config(
                text=
                    f'Server: Max'
            )

# função atualizar label principal
def update_label():
    global codes, cps, codes_per_click
    label_qnt_code.config(
        text=
            f'{codes:,}\n'
            f'CPS: {(cps*codes_per_click):,}'
    )

# Criar label qnt cookies
label_qnt_code = tk.Label(
    window,
    text=
        f'{codes}\n'
        f'CPS: {(cps*codes_per_click)}',
    font=('Arial', 25),
    foreground='white',
    background='#292b38'
)
label_qnt_code.grid(row=1, column=1, pady=25)

#criar botão codar
image_main_button = tk.PhotoImage(file='_internal/assets/main_button.png')
resized_image_main_button = image_main_button.subsample(3, 3)
main_button = tk.Button(
    window,
    image=resized_image_main_button,
    background="#292b38",
    highlightthickness=0,
    bd=0,
    command=generate_code,
    activebackground='#292b38'
)
main_button.grid(row = 4, column = 1, padx=100)

# criar botão RTFM
image_RTFM = tk.PhotoImage(file='_internal/assets/RTFM.png')
resized_image_RTFM = image_RTFM.subsample(7, 7)
button_RTFM = tk.Button(
    window,
    image=resized_image_RTFM,
    background='#292b38',
    highlightthickness=0,
    bd=0,
    command=buy_RTFM,
    activebackground='#292b38'
)
button_RTFM.grid(row=1, column=2, pady=25)

# Criar label qnt RTFM
label_qnt_RTFM = tk.Label(
    window,
    text=
        f'RTFM: {rtfm}\n'
        f'cost: {cost_rtfm}',
    font=('Arial', 15),
    foreground='white',
    background='#292b38'
)
label_qnt_RTFM.grid(row=1, column=3, pady=25)

# criar botão robô
image_robot = tk.PhotoImage(file='_internal/assets/robot.png')
resized_image_robot = image_robot.subsample(4, 4)
button_robot = tk.Button(
    window,
    image=resized_image_robot,
    background='#292b38',
    highlightthickness=0,
    bd=0,
    command=buy_CPS,
    activebackground='#292b38'
)

# criar label qnt CPS robôs
label_qnt_CPS = tk.Label(
    window,
    text=
        f'AI Coder: {cps}\n'
        f'cost: {cost_cps}',
    font=('Arial', 15),
    foreground='white',
    background='#292b38'
)

# criar botão servidor
image_server = tk.PhotoImage(file='_internal/assets/server.png')
resized_image_server = image_server.subsample(7, 7)
button_server = tk.Button(
    window,
    image=resized_image_server,
    background='#292b38',
    highlightthickness=0,
    bd=0,
    command=buy_server,
    activebackground='#292b38'
)

# criar label botão servidor
label_qnt_server = tk.Label(
    window,
    text=
        f'Server: {server}\n'
        f'cost: {cost_server}',
    font=('Arial', 15),
    foreground='white',
    background='#292b38'
)

# Inicializa
update()
window.mainloop()