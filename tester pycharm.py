from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from tkinter import *
from tkinter import messagebox

box = Tk()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setAutoFillBackground(True)
        self.p=self.palette()
        self.p.setColor(self.backgroundRole(), Qt.yellow)
        self.setPalette(self.p)
        header=QLabel("Kalkulator pajak")
        priceLabel=QLabel("Masukan nominal: ")
        print("Error")
        self.priceEntry=QLineEdit()
        taxlabel=QLabel("Masukan Tarif Pajak %: ")
        self.tax=QSpinBox()
        self.button=QPushButton("Ok")
        self.answer=QLineEdit()
        grid=QGridLayout()
        grid=QGridLayout()
        grid.addWidget(header,0,0)
        grid.addWidget(priceLabel, 2, 0)
        grid.addWidget(self.priceEntry, 2, 1)
        grid.addWidget(taxlabel,3,0)
        grid.addWidget(self.tax,3,1)
        grid.addWidget(self.button,4,0)
        grid.addWidget(self.answer, 4, 1)
        self.button.clicked.connect(self.taxcal)
        self.resize(200,150)
        self.show()
        self.setLayout(grid)
        self.setWindowTitle("Calculator")

    def taxcal(self):
        try:
            price = float(self.priceEntry.text())
            tax = float(self.tax.text())
        except ValueError:
            messagebox.showwarning("Error", "Insert Number Please!")
        else:
            final=(price*(tax/100)+price)
            self.answer.setText(str(final))

app=QApplication([])
main_window=MainWindow()
main_window.show()
sys.exit(app.exec())