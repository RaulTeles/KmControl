import sys
from PySide6 import QtWidgets, QtCore
from mainWindow import MyKmcontrol



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyKmcontrol()

    welcome = QtWidgets.QLabel("Bem-vindo ao Sistema de Controle de Veículo!")
    namelabel = QtWidgets.QLabel("Por favor, insira o seu nome: ")
    nametext = QtWidgets.QLineEdit("")

    window.addWidgetOnLayout(welcome, 1, 1, 1, 2)  # Span across 2 columns
    window.addWidgetOnLayout(namelabel, 2, 1)
    window.addWidgetOnLayout(nametext, 2, 2)
    window.show()
    app.exec()
