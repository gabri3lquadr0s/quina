from itertools import zip_longest
from quina import Quina
from tkinter import filedialog as fd
import dearpygui.dearpygui as dpg
import pandas as pd

quina = Quina()

def send_draws(draw_from_file=""):
    try:
        draw = []
        if draw_from_file == "":
            draw = [[i for i in dpg.get_values([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15]) if i != 0]]
        else:
            draw = draw_from_file
        send = quina.read_bets(draw)
        for j in draw:
            if j not in send['err']:
                with dpg.table_row(parent="row"):
                    dpg.add_text(str(j))

        dpg.set_value(prize, f"Valor do Prêmio: {send['current_total_prize']}")
    except Exception as e:
        with dpg.table_row(parent="row3"):
            dpg.add_text(f"Erro em send_draws: {e}")

def parse_from_excel():
    filename = fd.askopenfilename()
    try:
        df = pd.read_excel(filename)
        new_bets = []
        for index, row in df.iterrows():
            parsed_row = [int(i) for i in list(row) if str(i) != "nan"]
            new_bets.append(parsed_row)

        send_draws(new_bets)

    except Exception as e:
        with dpg.table_row(parent="row3"):
            dpg.add_text(f"Erro em send_draws: {e}")

def execute():
    try:
        finish = quina.execute_drawn()
        dpg.set_value(numbers, f"Números sorteados: {finish['drawn_values']}")
        del finish['drawn_values']
        try:
            dpg.delete_item("row2", children_only=True)
        except:
            pass
        for i in finish.keys():
            dpg.add_table_column(label=i, tag=i, parent="row2")

        for j,k,l,m,n,b in zip_longest(*list(finish.values())):
            with dpg.table_row(parent="row2"):
                dpg.add_text(f"{j}")
                dpg.add_text(f"{k}")
                dpg.add_text(f"{l}")
                dpg.add_text(f"{m}")
                dpg.add_text(f"{n}")
                dpg.add_text(f"{b}")

    except Exception as e:
        with dpg.table_row(parent="row3"):
            dpg.add_text(f"Erro em send_draws: {e}")

dpg.create_context()
dpg.create_viewport(title='Simulador da Quina', width=1000, height=800)

with dpg.window(label="LOTÉRICA"):
    dpg.add_text("Bem vindo a Quina! Por favor insiram suas apostas.\n\n-Se o input for 0 ele não será considerado\n-Primeiros 5 números são obrigatórios\n-Valores devem ser de 1 a 80\n\n\n")
    #
    with dpg.group():
        i1 = dpg.add_input_int(label="Primeiro Número (obrigatório)", default_value=1, width=100, min_value=1, max_value=80, tag="i1")
        i2 = dpg.add_input_int(label="Segundo Número (obrigatório)", default_value=2, width=100, min_value=1, max_value=80, tag="i2")
        i3 = dpg.add_input_int(label="Terceiro Número (obrigatório)", default_value=3, width=100, min_value=1, max_value=80, tag="i3")
        i4 = dpg.add_input_int(label="Quarto Número (obrigatório)", default_value=4, width=100, min_value=1, max_value=80, tag="i4")
        i5 = dpg.add_input_int(label="Quinto Número (obrigatório)", default_value=5, width=100, min_value=1, max_value=80, tag="i5")
        i6 = dpg.add_input_int(label="Sexto Número", default_value=0, width=100, min_value=0, max_value=80, tag="i6")
        i7 = dpg.add_input_int(label="Sétimo Número", default_value=0, width=100, min_value=0, max_value=80, tag="i7")
        i8 = dpg.add_input_int(label="Oitavo Número", default_value=0, width=100, min_value=0, max_value=80, tag="i8")
        i9 = dpg.add_input_int(label="Nono Número", default_value=0, width=100, min_value=0, max_value=80, tag="i9")
        i10 = dpg.add_input_int(label="Décimo Número", default_value=0, width=100, min_value=0, max_value=80, tag="i10")
        i11 = dpg.add_input_int(label="Décimo Primeiro Número", default_value=0, width=100, min_value=0, max_value=80, tag="i11")
        i12 = dpg.add_input_int(label="Décimo Segundo Número", default_value=0, width=100, min_value=0, max_value=80, tag="i12")
        i13 = dpg.add_input_int(label="Décimo Terceiro Número", default_value=0, width=100, min_value=0, max_value=80, tag="i13")
        i14 = dpg.add_input_int(label="Décimo Quarto Número", default_value=0, width=100, min_value=0, max_value=80, tag="i14")
        i15 = dpg.add_input_int(label="Décimo Quinto Número", default_value=0, width=100, min_value=0, max_value=80, tag="i15")

    dpg.add_text("Ou insira apostas através de um arquivo Excel")
    dpg.add_button(label="Selecione um arquivo excel", callback=parse_from_excel)
    dpg.add_button(label="Apostar", tag="insert_draw", callback=send_draws)

with dpg.window(label="APOSTAS"):
    with dpg.table(header_row=False, tag="row"):
        dpg.add_table_column()

with dpg.window(label="SORTEIO", tag="sorteio"):
    prize = dpg.add_text("Valor do prêmio: 10000", tag="prize")
    dpg.add_button(label="Executar sorteio", tag="execute_draw", callback=execute)
    numbers = dpg.add_text("Números sorteados: ", tag="numbers")
    with dpg.table(tag="row2"):
        pass

with dpg.window(label="ERROS", tag="erros"):
    with dpg.table(tag="row3"):
        dpg.add_table_column()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

