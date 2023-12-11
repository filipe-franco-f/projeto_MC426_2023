import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from datetime import datetime
from validador_reuniao import validar_informacoes_reuniao
from agendamento_exceptions import (
    CampoVazioException,
    DataInvalidaException
)

# Lista para armazenar as reuniões agendadas
reunioes_agendadas = []

# Função para agendar uma reunião
def agendar_reuniao():
    data = calendario.get()
    hora = hora_entry.get()
    assunto = assunto_entry.get()

    try:
        data_hora = validar_informacoes_reuniao(data=data, hora=hora, assunto=assunto)
    except CampoVazioException:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    except DataInvalidaException:
        messagebox.showerror("Erro", "Formato de data/hora inválido.")
        return
    except:
        return

    # Adiciona a reunião agendada à lista
    reunioes_agendadas.append((data_hora, assunto))

    # Limpa os campos após o agendamento
    calendario.delete(0, tk.END)
    hora_entry.delete(0, tk.END)
    assunto_entry.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Reunião agendada com sucesso.")


# Função para exibir as reuniões agendadas
def exibir_reunioes():
    if not reunioes_agendadas:
        messagebox.showinfo("Reuniões Agendadas", "Não há reuniões agendadas.")
    else:
        lista_reunioes = "\n".join(
            [f"{data.strftime('%d/%m/%Y %H:%M')} - {assunto}" for data, assunto in reunioes_agendadas])
        messagebox.showinfo("Reuniões Agendadas", lista_reunioes)

def agendar_com_interface(id_user):
    # Configuração da janela principal
    root = tk.Tk()
    root.title("Agendamento de Reuniões")

    # Rótulos e entradas
    calendario_label = tk.Label(root, text="Data (dd/mm/yyyy):")
    calendario_label.pack()
    calendario = ttk.Entry(root)
    calendario.pack()

    hora_label = tk.Label(root, text="Hora (hh:mm):")
    hora_label.pack()
    hora_entry = ttk.Entry(root)
    hora_entry.pack()

    assunto_label = tk.Label(root, text="Assunto:")
    assunto_label.pack()
    assunto_entry = ttk.Entry(root)
    assunto_entry.pack()

    # Botão para agendar reunião
    agendar_button = ttk.Button(root, text="Agendar Reunião", command=agendar_reuniao)
    agendar_button.pack()

    # Cria um menu
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    # Adiciona um menu chamado "Reuniões"
    reunioes_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Reuniões", menu=reunioes_menu)

    # Adiciona uma opção no menu para exibir as reuniões agendadas
    reunioes_menu.add_command(label="Exibir Reuniões Agendadas", command=exibir_reunioes)

    # Iniciar a interface gráfica
    root.mainloop()
