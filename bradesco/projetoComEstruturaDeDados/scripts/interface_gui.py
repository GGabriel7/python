from tkinter import *

class Gui:
    """Classe da Interface Gráfica"""

    def __init__(self):
        # Configurações gerais
        self.xPad = 5
        self.yPad = 3
        self.widthEntry = 30

        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")

        # Variáveis
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Labels
        self.lblnome = Label(self.window, text="Nome")
        self.lblsobrenome = Label(self.window, text="Sobrenome")
        self.lblemail = Label(self.window, text="Email")
        self.lblcpf = Label(self.window, text="CPF")

        # Entradas
        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.widthEntry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.widthEntry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.widthEntry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.widthEntry)

        # Lista e Scrollbar
        self.listClientes = Listbox(self.window, width=100)
        self.scrollClientes = Scrollbar(self.window)

        # Botões
        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

        # Layout
        self.lblnome.grid(row=0, column=0)
        self.lblsobrenome.grid(row=1, column=0)
        self.lblemail.grid(row=2, column=0)
        self.lblcpf.grid(row=3, column=0)

        self.entNome.grid(row=0, column=1, padx=50, pady=50)
        self.entSobrenome.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)

        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=3, rowspan=10)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        # Configurações adicionais
        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        for child in self.window.winfo_children():
            widgetClass = child.__class__.__name__
            if widgetClass == "Button":
                child.grid_configure(sticky='WE', padx=self.xPad, pady=self.yPad)
            elif widgetClass == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widgetClass == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.xPad, pady=self.yPad, sticky='N')

    def run(self):
        self.window.mainloop()