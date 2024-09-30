from dataclasses import asdict

import dearpygui.dearpygui as dpg
from dearpygui.dearpygui import maximize_viewport

#import pandas as pd
from quina import Quina

quina = Quina()

def send_draws():
    try:
        draw = [[i for i in dpg.get_values([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15]) if i != 0]]
        send = quina.read_bets(draw)
        print(send)
        for j in draw:
            if j not in send['err']:
                with dpg.table_row(parent="row"):
                    dpg.add_text(str(j))

        dpg.set_value(prize, f"Valor do Prêmio: {send['current_total_prize']}")
    except Exception as e:
        print(e)

def execute():
    #try:
        finish = quina.execute_drawn()
        dpg.set_value(numbers, f"Números sorteados: {finish['drawn_values']}")
        del finish['drawn_values']
        try:
            dpg.delete_item("row2", children_only=True)
        except:
            pass
        for i in finish.keys():
            dpg.add_table_column(label=i, tag=i, parent="row2")
            for ii in finish[i]:
                with dpg.table_row(parent="row2"):
                    dpg.add_text(str(ii))

    # except Exception as e:
    #     print(e)

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
    dpg.add_button(label="Selecione um arquivo", callback=lambda: dpg.show_item("file_select"))
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

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

