import os
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo PySide + SQLite")
        self.resize(600, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.load_data()

    def load_data(self):
        dbPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exemplo.db')
        conn = sqlite3.connect(dbPath )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()

        self.table.setRowCount(len(rows))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ID', 'Nome', 'Email'])

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        conn.close()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()