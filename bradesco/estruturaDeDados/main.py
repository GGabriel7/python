from GUI import Gui
from backend import TransactionObject
from tkinter import END

# Variável global da interface e seleção
app = None
selected = None

# Instância do banco de dados
db = TransactionObject()
db.init_db()

def view_command():
    rows = db.view()
    app.list_clientes.delete(0, END)
    for row in rows:
        app.list_clientes.insert(END, row)

def search_command():
    app.list_clientes.delete(0, END)
    rows = db.search(
        app.txt_nome.get(),
        app.txt_sobrenome.get(),
        app.txt_email.get(),
        app.txt_cpf.get()
    )
    for row in rows:
        app.list_clientes.insert(END, row)

def insert_command():
    db.insert(
        app.txt_nome.get(),
        app.txt_sobrenome.get(),
        app.txt_email.get(),
        app.txt_cpf.get()
    )
    view_command()

def update_command():
    if selected:
        db.update(
            selected[0],
            app.txt_nome.get(),
            app.txt_sobrenome.get(),
            app.txt_email.get(),
            app.txt_cpf.get()
        )
        view_command()

def delete_command():
    if selected:
        db.delete(selected[0])
        view_command()

def get_selected_row(event):
    global selected
    try:
        index = app.list_clientes.curselection()[0]
        selected = app.list_clientes.get(index)

        # Usando StringVar.set() (caso esteja usando StringVar)
        app.txt_nome.set(selected[1])
        app.txt_sobrenome.set(selected[2])
        app.txt_email.set(selected[3])
        app.txt_cpf.set(selected[4])
    except IndexError:
        selected = None

def main():
    global app
    app = Gui()

    # Eventos e comandos
    app.list_clientes.bind('<<ListboxSelect>>', get_selected_row)
    app.btn_view.configure(command=view_command)
    app.btn_buscar.configure(command=search_command)
    app.btn_inserir.configure(command=insert_command)
    app.btn_update.configure(command=update_command)
    app.btn_deletar.configure(command=delete_command)
    app.btn_fechar.configure(command=app.window.destroy)

    app.run()

if __name__ == "__main__":
    main()