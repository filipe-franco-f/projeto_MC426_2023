import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from datetime import datetime
import banco_financas

dividas = []

class CampoVazioException(Exception):
    pass

class ValorInvalidoException(Exception):
    pass

def validar_informacoes_divida(pessoa: str, valor:str, assunto:str):
    if not pessoa or not valor or not assunto:
        raise CampoVazioException

    # Converte a data e valor para um objeto datetime
    if len(valor) < 4 or valor[-3] != ".":
        raise ValorInvalidoException
    try:
        reais = int(valor[:-3])
        centavos = int(valor[-2:])
    except:
        raise ValorInvalidoException

    return 

# Função para agendar uma reunião
def cadastrar_divida(id_user, pessoa_entry, valor_entry, assunto_entry):
    pessoa = pessoa_entry.get()
    valor = valor_entry.get()
    assunto = assunto_entry.get()

    try:
        validar_informacoes_divida(pessoa=pessoa, valor=valor, assunto=assunto)
    except CampoVazioException:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    except ValorInvalidoException:
        messagebox.showerror("Erro", "Formato de valor da dívida inválido.")
        return
    except:
        return

    # Adiciona a reunião agendada à lista
    try:
        cadastro = banco_financas.cadastra_divida(id_user, pessoa, valor, assunto)
    except:
        messagebox.showerror("Erro", "Pessoa não encontrada")
        return

    # Limpa os campos após o agendamento
    pessoa_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)
    assunto_entry.delete(0, tk.END)
    messagebox.showinfo("Sucesso", "Dívida cadastrada com sucesso.")


def quita_divida(id_user, pessoa_entry, valor_entry, assunto_entry):
    pessoa = pessoa_entry.get()
    valor = valor_entry.get()
    assunto = assunto_entry.get()

    try:
        validar_informacoes_divida(pessoa=pessoa, valor=valor, assunto=assunto)
    except CampoVazioException:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    except ValorInvalidoException:
        messagebox.showerror("Erro", "Formato de valor da dívida inválido.")
        return
    except:
        return

    # Adiciona a reunião agendada à lista
    try:
        cadastro = banco_financas.quitar_divida(id_user, pessoa, valor, assunto)
    except banco_financas.PessoaNaoEncontrada:
        messagebox.showerror("Erro", "Pessoa não encontrada")
        return
    except banco_financas.DividaNaoEncontrada:
        messagebox.showerror("Erro", "Dívida não encontrada")
        return
    except:
        return

    # Limpa os campos após o agendamento
    pessoa_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)
    assunto_entry.delete(0, tk.END)
    messagebox.showinfo("Sucesso", "Dívida quitada com sucesso.")

# Função para exibir as dividas
def exibir_dividas(id_user):
    dividas = banco_financas.checar_dividas(id_user)
    if not dividas:
        messagebox.showinfo("Dívidas", "Não há dívidas cadastradas.")
    else:
        lista_dividas = "\n".join(
            [f"""Pessoa: {pessoa}\n 
            Valor: {valor}\n
            Assunto: {assunto}\n
            ===============""" for pessoa, valor, assunto in dividas])
        messagebox.showinfo("Dívidas", lista_dividas)
    
def quitar_dividas(id_user):
    root = tk.Tk()
    root.title("Administrador de finanças")

def administrar_financas(id_user):
    # Configuração da janela principal
    root = tk.Tk()
    root.title("Administrador de finanças")

    notebook = ttk.Notebook(root)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    notebook.add(tab1, text="Cadastra divida")
    notebook.add(tab2, text="Quita divida")

    # Rótulos e entradas
    pessoa_label_t1 = tk.Label(tab1, text="Pessoa:")
    pessoa_label_t1.pack()
    pessoa_entry_t1 = ttk.Entry(tab1)
    pessoa_entry_t1.pack()

    valor_label_t1 = tk.Label(tab1, text="Valor da dívida: x.xx")
    valor_label_t1.pack()
    valor_entry_t1 = ttk.Entry(tab1)
    valor_entry_t1.pack()

    assunto_label_t1 = tk.Label(tab1, text="Assunto:")
    assunto_label_t1.pack()
    assunto_entry_t1 = ttk.Entry(tab1)
    assunto_entry_t1.pack()

    cadastrar_divida_button = ttk.Button(tab1, text="Cadastrar dívida", command=lambda: cadastrar_divida(id_user, pessoa_entry_t1, valor_entry_t1, assunto_entry_t1))
    cadastrar_divida_button.pack()

    # Rótulos e entradas
    pessoa_label_t2 = tk.Label(tab2, text="Pessoa:")
    pessoa_label_t2.pack()
    pessoa_entry_t2 = ttk.Entry(tab2)
    pessoa_entry_t2.pack()

    valor_label_t2 = tk.Label(tab2, text="Valor da dívida: x.xx")
    valor_label_t2.pack()
    valor_entry_t2 = ttk.Entry(tab2)
    valor_entry_t2.pack()

    assunto_label_t2 = tk.Label(tab2, text="Assunto:")
    assunto_label_t2.pack()
    assunto_entry_t2 = ttk.Entry(tab2)
    assunto_entry_t2.pack()

    quita_divida_button = ttk.Button(tab2, text="Quita dívida", command=lambda: quita_divida(id_user, pessoa_entry_t2, valor_entry_t2, assunto_entry_t2))
    quita_divida_button.pack()

    # Cria um menu
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    # Adiciona um menu chamado "Dividas"
    dividas_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Dívidas", menu=dividas_menu)

    # Adiciona uma opção no menu para exibir as dividas
    dividas_menu.add_command(label="Exibir dividas", command=lambda: exibir_dividas(id_user))

    # Iniciar a interface gráfica
    notebook.pack()
    root.mainloop()

administrar_financas(1)