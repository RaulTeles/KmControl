from PySide6 import QtWidgets, QtCore


class MyKmcontrol(QtWidgets.QMainWindow):
    def __init__(self,parent: QtWidgets.QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.MyWidget = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout()
        self.MyWidget.setLayout(self.layout)
        self.setCentralWidget(self.MyWidget)


    #função para fixar a tela caso seja necessário    
    def adjustLayoutFixed(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    #função para boas práticas com finalidade de adicinar widgets no layout
    def addWidgetOnLayout(self, widget: QtWidgets.QWidget, row: int, col: int, row_span: int = 1, col_span: int = 1):
        self.layout.addWidget(widget)
        self.adjustLayoutFixed()