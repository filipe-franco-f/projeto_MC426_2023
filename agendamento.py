import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from datetime import datetime
import banco_agendamento
import agendamento_reunioes.validador_reuniao
from agendamento_reunioes.agendamento_exceptions import CampoVazioException, DataInvalidaException, reuniaoNaoEncontrada

class CampoVazioException(Exception):
    pass

class ValorInvalidoException(Exception):
    pass

# Função para agendar uma reunião
def agendar_reuniao(id_user, calendario, hora_entry, assunto_entry):
    data = calendario.get()
    hora = hora_entry.get()
    assunto = assunto_entry.get()

    try:
        data_hora = agendamento_reunioes.validador_reuniao.validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)
    except CampoVazioException:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    except DataInvalidaException:
        messagebox.showerror("Erro", "Formato de data/hora inválido.")
        return
    except:
        return

    # Adiciona a reunião agendada à lista
    try:
        cadastro = banco_agendamento.cadastra_reuniao(id_user, data_hora.strftime('%d/%m/%Y %H:%M'), assunto)
    except:
        messagebox.showerror("Erro", "Erro ao agendar reuniao")
        return


    # Limpa os campos após o agendamento
    calendario.delete(0, tk.END)
    hora_entry.delete(0, tk.END)
    assunto_entry.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Reunião agendada com sucesso.")

def desmarcar_reuniao(id_user, calendario, hora_entry, assunto_entry):
    data = calendario.get()
    hora = hora_entry.get()
    assunto = assunto_entry.get()

    try:
        data_hora = agendamento_reunioes.validador_reuniao.validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)
    except CampoVazioException:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    except DataInvalidaException:
        messagebox.showerror("Erro", "Formato de data/hora inválido.")
        return
    except:
        return

    try:
        cadastro = banco_agendamento.deletar_reuniao(id_user, data_hora.strftime('%d/%m/%Y %H:%M'), assunto)
    except reuniaoNaoEncontrada:
        messagebox.showerror("Erro", "Reunião não encontrada")
        return
    except:
        return

    # Limpa os campos após o agendamento
    calendario.delete(0, tk.END)
    hora_entry.delete(0, tk.END)
    assunto_entry.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Reunião deletada com sucesso.")

# Função para exibir as reuniões agendadas
def exibir_reunioes(id_user):
    reunioes_agendadas = banco_agendamento.checar_reunioes(id_user)
    if not reunioes_agendadas:
        messagebox.showinfo("Reuniões Agendadas", "Não há reuniões agendadas.")
    else:
        lista_reunioes = "\n".join(
            [f"""Data: {data}\n 
            Assunto: {assunto}\n
            ===============""" for data, assunto in reunioes_agendadas])
        messagebox.showinfo("Reuniões Agendadas", lista_reunioes)

def agendar_com_interface(id_user):
    # Configuração da janela principal
    root = tk.Tk()
    root.title("Administrador de reuniões")

    notebook = ttk.Notebook(root)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    notebook.add(tab1, text="Agendar reuniao")
    notebook.add(tab2, text="Desmarcar reuniao")

    # Rótulos e entradas
    calendario_label_t1 = tk.Label(tab1, text="Data (dd/mm/yyyy):")
    calendario_label_t1.pack()
    calendario_t1 = ttk.Entry(tab1)
    calendario_t1.pack()

    hora_label_t1 = tk.Label(tab1, text="Hora (hh:mm):")
    hora_label_t1.pack()
    hora_entry_t1 = ttk.Entry(tab1)
    hora_entry_t1.pack()

    assunto_label_t1 = tk.Label(tab1, text="Assunto:")
    assunto_label_t1.pack()
    assunto_entry_t1 = ttk.Entry(tab1)
    assunto_entry_t1.pack()

    # Botão para agendar reunião
    agendar_button = ttk.Button(tab1, text="Agendar Reunião", command=lambda: agendar_reuniao(id_user, calendario_t1, hora_entry_t1, assunto_entry_t1))
    agendar_button.pack()

    # Rótulos e entradas
    calendario_label_t2 = tk.Label(tab2, text="Data (dd/mm/yyyy):")
    calendario_label_t2.pack()
    calendario_t2 = ttk.Entry(tab2)
    calendario_t2.pack()

    hora_label_t2 = tk.Label(tab2, text="Hora (hh:mm):")
    hora_label_t2.pack()
    hora_entry_t2 = ttk.Entry(tab2)
    hora_entry_t2.pack()

    assunto_label_t2 = tk.Label(tab2, text="Assunto:")
    assunto_label_t2.pack()
    assunto_entry_t2 = ttk.Entry(tab2)
    assunto_entry_t2.pack()

    # Botão para agendar reunião
    agendar_button = ttk.Button(tab2, text="Desmarcar Reunião", command=lambda: desmarcar_reuniao(id_user, calendario_t2, hora_entry_t2, assunto_entry_t2))
    agendar_button.pack()

    # Cria um menu
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    # Adiciona um menu chamado "Reuniões"
    reunioes_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Reuniões", menu=reunioes_menu)

    # Adiciona uma opção no menu para exibir as reuniões agendadas
    reunioes_menu.add_command(label="Exibir Reuniões Agendadas", command=lambda: exibir_reunioes(id_user))

    # Iniciar a interface gráfica
    notebook.pack()
    root.mainloop()

f = 1
if f:
    banco_agendamento.deletarusuario("u0")
    banco_agendamento.inserir_no_banco(0, "u0")
    

agendar_com_interface(0)