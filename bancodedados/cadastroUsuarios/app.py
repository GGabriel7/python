import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableWidget, 
    QTableWidgetItem, QLineEdit, QHBoxLayout, QLabel, QMessageBox, QDialog, QHeaderView, QSizePolicy, 
)
from PySide6.QtCore import Qt
from criarDB import *

# Janela de Adicionar Usuário
class AddUserDialog(QDialog):
    def __init__(self, parent=None, editing_user=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar Usuário")
        self.editing_user = editing_user
        self.setFixedSize(300, 150)

        layout = QVBoxLayout(self)
        
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Nome Completo")
        self.age_input = QLineEdit(self)
        self.age_input.setPlaceholderText("Idade")
        self.add_button = QPushButton("Adicionar")
        self.add_button.clicked.connect(self.add_user)
        save_button = QPushButton("Salvar", self)
        save_button.clicked.connect(self.salvar_usuario)

        layout.addWidget(self.name_input)
        layout.addWidget(self.age_input)
        layout.addWidget(self.add_button)
        layout.addWidget(save_button)

        self.setLayout(layout)

        if self.editing_user:
            # Se for edição, carrega os dados do usuário nos campos de entrada
            self.name_input.setText(self.editing_user["nome"])
            self.age_input.setText(str(self.editing_user["idade"]))

    def add_user(self):
        nome = self.name_input.text().strip()
        idade = self.age_input.text().strip()

        # Validar nome completo
        if len(nome.split()) < 2 or not all(palavra.isalpha() for palavra in nome.split()):
            QMessageBox.warning(self, "Erro", "Por favor, insira o nome completo (pelo menos dois nomes).")
            return

        # Validar idade
        if not idade.isdigit() or not (0 < int(idade) <= 120):
            QMessageBox.warning(self, "Erro", "Por favor, insira uma idade válida (entre 1 e 120).")
            return
        
        adicionarUsuario(nome, int(idade))
        QMessageBox.information(self, "Sucesso", "Usuário adicionado com sucesso!")
        self.close()

    
    def salvar_usuario(self):
        nome = self.name_input.text()
        idade = self.age_input.text()

        if len(nome.split()) < 2 or not all(palavra.isalpha() for palavra in nome.split()):
            QMessageBox.warning(self, "Erro", "Por favor, insira o nome completo (pelo menos dois nomes).")
            return

        # Validar idade
        if not idade.isdigit() or not (0 < int(idade) <= 120):
            QMessageBox.warning(self, "Erro", "Por favor, insira uma idade válida (entre 1 e 120).")
            return
        
        if self.editing_user:
            # Se for edição, atualiza o usuário
            atualizarUsuario(self.editing_user["id"], nome, int(idade))
            QMessageBox.information(self, "Sucesso", "Usuário atualizado com sucesso!")
        else:
            # Se for novo usuário, adiciona
            adicionarUsuario(nome, int(idade))
            QMessageBox.information(self, "Sucesso", "Usuário adicionado com sucesso!")

        self.close()


# Janela Principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Usuários")
        self.resize(600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # Botões superiores
        top_layout = QHBoxLayout()
        self.add_button = QPushButton("Adicionar")
        self.add_button.clicked.connect(self.show_add_dialog)
        self.refresh_button = QPushButton("Atualizar Lista")
        self.refresh_button.clicked.connect(self.load_table)
        self.delete_button = QPushButton("Excluir")
        self.delete_button.clicked.connect(self.delete_user)
        self.edit_button = QPushButton("Editar Usuário")
        self.edit_button.clicked.connect(self.editar_usuario)

        top_layout.addWidget(self.add_button)
        top_layout.addWidget(self.refresh_button)
        top_layout.addWidget(self.delete_button)
        top_layout.addWidget(self.edit_button)

        # Tabela
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Nome", "Idade"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)  # Estica a última coluna
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Colunas ajustáveis
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) #Ocupar todo o espaço disponivel

        # Botão Inferir
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()

        self.json_button = QPushButton("Gerar Arquivo")
        self.json_button.clicked.connect(self.criar_json)

        bottom_layout.addWidget(self.json_button)

        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.table)
        main_layout.addLayout(bottom_layout)

        self.load_table()

    
    def load_table(self):
        self.table.setRowCount(0)
        usuarios = listarUsuarios()

        for row_idx, row_data in enumerate(usuarios):
            self.table.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
    

    def show_add_dialog(self):
        dialog = AddUserDialog()
        dialog.exec()
        self.load_table()

    
    def delete_user(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Erro", "Selecione um usuário para excluir!")
            return

        user_id = self.table.item(selected_row, 0).text()
        apagarUsuario(user_id)
        QMessageBox.information(self, "Sucesso", "Usuário excluído!")
        self.load_table()


    def editar_usuario(self):
        current_row = self.table.currentRow()

        if current_row == -1:
            QMessageBox.warning(self, "Aviso", "Selecione um usuário para editar.")
            return
        
        user_id = self.table.item(current_row, 0).text()
        nome = self.table.item(current_row, 1).text()
        idade = self.table.item(current_row, 2).text()

        self.dialog = AddUserDialog(self, {"id": user_id, "nome": nome, "idade": idade})
        self.dialog.exec()
        self.load_table()

    
    def criar_json(self):
        try:
            criarJSON()
            QMessageBox.information(self, "Sucesso", "Arquivo JSON gerado com sucesso!")
        
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao criar o arquivo JSON:\n{str(e)}")


createTable()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())