from PyQt5.Qt import *
from cfmTradeWgt import Ui_Form


class CfmTradeWgt(QWidget, Ui_Form):

    agreeThisTrade_signal=pyqtSignal()
    refuseThisTrade_signal=pyqtSignal(str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def cfmThisTrade(self):
        print("同意交易")
        self.agreeThisTrade_signal.emit()

    def refuseThisTrade(self):
        print("拒绝交易")
        print("原因：",self.textEdit.toPlainText())
        self.refuseThisTrade_signal.emit(self.textEdit.toPlainText())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = CfmTradeWgt()
    window.show()
    sys.exit(app.exec_())
