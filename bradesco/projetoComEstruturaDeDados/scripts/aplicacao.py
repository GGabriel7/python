from interface_gui import Gui
import Backend as core
from tkinter import END

app = None  # Variável global para a interface GUI
selected = None  # Variável para armazenar o cliente selecionado


def viewCommand():
    """Exibe todos os registros no ListBox"""
    app.listClientes.delete(0, END)
    rows = core.view()
    for r in rows:
        app.listClientes.insert(END, r)


def searchCommand():
    """Busca registros com base nos critérios"""
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)


def insertCommand():
    """Insere um novo registro e atualiza a exibição"""
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    viewCommand()


def updateCommand():
    """Atualiza o registro selecionado"""
    if selected:
        core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
        viewCommand()
    else:
        print("Nenhum registro selecionado para atualizar.")


def delCommand():
    """Deleta o registro selecionado"""
    if selected:
        core.delete(selected[0])
        viewCommand()
    else:
        print("Nenhum registro selecionado para deletar.")


def getSelectedRow(event):
    """Obtém a linha selecionada no ListBox"""
    global selected
    try:
        index = app.listClientes.curselection()[0]
        selected = app.listClientes.get(index)

        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])
        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])
        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])
    except IndexError:
        selected = None


if __name__ == "__main__":
    # Inicializa a GUI
    app = Gui()

    # Vincula os eventos
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    # Configura os botões
    app.btnViewAll.configure(command=viewCommand)
    app.btnBuscar.configure(command=searchCommand)
    app.btnInserir.configure(command=insertCommand)
    app.btnUpdate.configure(command=updateCommand)
    app.btnDel.configure(command=delCommand)
    app.btnClose.configure(command=app.window.destroy)

    # Executa o loop principal
    app.run()