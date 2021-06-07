from PyQt5.Qt import *
from changeWgt import Ui_Form


class ChangeWgt(QWidget, Ui_Form):

    changeIt_signal=pyqtSignal(str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def changeIt(self):
        print("执行修改")
        self.changeIt_signal.emit(self.lineEdit.text())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = ChangeWgt()
    window.show()
    sys.exit(app.exec_())
