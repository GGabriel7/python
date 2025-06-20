from tkinter import *

class Gui:
    """Classe da Interface Gráfica do PySQL."""

    def __init__(self):
        # Configurações
        self.x_pad = 5
        self.y_pad = 3
        self.entry_width = 30

        # Inicializa a janela principal
        self.window = Tk()
        self.window.title("PySQL versão 1.0")

        # Variáveis dos campos de entrada
        self.txt_nome = StringVar()
        self.txt_sobrenome = StringVar()
        self.txt_email = StringVar()
        self.txt_cpf = StringVar()

        # Criação e organização dos elementos
        self._criar_widgets()
        self._configurar_grid()

    def _criar_widgets(self):
        # Labels
        self.lbl_nome = Label(self.window, text="Nome")
        self.lbl_sobrenome = Label(self.window, text="Sobrenome")
        self.lbl_email = Label(self.window, text="Email")
        self.lbl_cpf = Label(self.window, text="CPF")

        # Campos de entrada
        self.ent_nome = Entry(self.window, textvariable=self.txt_nome, width=self.entry_width)
        self.ent_sobrenome = Entry(self.window, textvariable=self.txt_sobrenome, width=self.entry_width)
        self.ent_email = Entry(self.window, textvariable=self.txt_email, width=self.entry_width)
        self.ent_cpf = Entry(self.window, textvariable=self.txt_cpf, width=self.entry_width)

        # Lista e Scroll
        self.list_clientes = Listbox(self.window, width=100)
        self.scroll_clientes = Scrollbar(self.window)

        # Botões
        self.btn_view = Button(self.window, text="Ver Todos")
        self.btn_buscar = Button(self.window, text="Buscar")
        self.btn_inserir = Button(self.window, text="Inserir")
        self.btn_update = Button(self.window, text="Atualizar Selecionado")
        self.btn_deletar = Button(self.window, text="Deletar Selecionado")
        self.btn_fechar = Button(self.window, text="Fechar")

    def _configurar_grid(self):
        # Labels
        self.lbl_nome.grid(row=0, column=0)
        self.lbl_sobrenome.grid(row=1, column=0)
        self.lbl_email.grid(row=2, column=0)
        self.lbl_cpf.grid(row=3, column=0)

        # Entradas
        self.ent_nome.grid(row=0, column=1, padx=self.x_pad, pady=self.y_pad)
        self.ent_sobrenome.grid(row=1, column=1, padx=self.x_pad, pady=self.y_pad)
        self.ent_email.grid(row=2, column=1, padx=self.x_pad, pady=self.y_pad)
        self.ent_cpf.grid(row=3, column=1, padx=self.x_pad, pady=self.y_pad)

        # Listbox e Scroll
        self.list_clientes.grid(row=0, column=2, rowspan=10, sticky="NS")
        self.scroll_clientes.grid(row=0, column=3, rowspan=10, sticky="NS")
        self.list_clientes.configure(yscrollcommand=self.scroll_clientes.set)
        self.scroll_clientes.configure(command=self.list_clientes.yview)

        # Botões
        self.btn_view.grid(row=4, column=0, columnspan=2, sticky="WE", padx=self.x_pad, pady=self.y_pad)
        self.btn_buscar.grid(row=5, column=0, columnspan=2, sticky="WE", padx=self.x_pad, pady=self.y_pad)
        self.btn_inserir.grid(row=6, column=0, columnspan=2, sticky="WE", padx=self.x_pad, pady=self.y_pad)
        self.btn_update.grid(row=7, column=0, columnspan=2, sticky="WE", padx=self.x_pad, pady=self.y_pad)
        self.btn_deletar.grid(row=8, column=0, columnspan=2, sticky="WE", padx=self.x_pad, pady=self.y_pad)
        self.btn_fechar.grid(row=9, column=0, columnspan=2, sticky="WE", padx=self.x_pad, pady=self.y_pad)

    def run(self):
        self.window.mainloop()