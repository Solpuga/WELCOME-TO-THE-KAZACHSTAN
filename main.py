import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3
from PyQt6 import uic

class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite3")
        self.create_table()

    def nothing(self):
        self.nothing()

    def create_table(self):
        res = self.connection.cursor().execute('SELECT * from coffee').fetchall()
        self.tea.setColumnCount(7)
        self.tea.setRowCount(0)
        for i, row in enumerate(res):
            self.tea.setRowCount(
                self.tea.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tea.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
