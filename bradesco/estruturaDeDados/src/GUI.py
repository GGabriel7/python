from tkinter import *

class Gui():
    """"Classe da Interface Gráfica."""
    
    xPad = 5
    yPad = 3
    widthEntry = 30
    
    window = Tk()
    window.wm_title("PySQL versão 1.0")
    
    txtNome = StringVar()
    txtSobreNome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()
    
    lblnome = Label(window, text="Nome")
    lblsobreNome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="CPF")
    
    entNome = Entry(window, textvariable=txtNome, width=widthEntry)
    entSobreNome = Entry(window, textvariable=txtSobreNome, width=widthEntry)
    entEmail = Entry(window, textvariable=txtEmail, width=widthEntry)
    entCPF = Entry(window, textvariable=txtCPF, width=widthEntry)
    
    listClientes = Listbox(window, width=100)
    
    scrollClientes = Scrollbar(window)
    
    btnView = Button(window, text="Ver Todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")
    
    lblnome.grid(row=0, column=0)
    lblsobreNome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblcpf.grid(row=3, column=0)
    
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobreNome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    
    listClientes.grid(row=0, column=2, rowspan=10)
    
    scrollClientes.grid(row=0, column=6, rowspan=10)
    
    btnView.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)
    
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)
    
    for child in window.winfo_children():
        widgetClass = child.__class__.__name__
        if widgetClass == "Button":
            child.grid_configure(sticky="WE", padx=xPad, pady=yPad)
        elif widgetClass == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky="NS")
        elif widgetClass == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky="NS")
        else:
            child.grid_configure(padx=xPad, pady=yPad, sticky="N")
            
    def run(self):
        Gui.window.mainloop()