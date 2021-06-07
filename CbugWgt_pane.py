from PyQt5.Qt import *
from CbugWgt import Ui_Form


class CbugWgt(QWidget, Ui_Form):

    C_cfm_buy_signal=pyqtSignal(int,float)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def cfmBuy(self):
        print("确认求购")
        self.C_cfm_buy_signal.emit(int(self.SsupplyWgt_NumLedit_2.text()),float(self.SsupplyWgt_PriceLedit_2.text()))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window =CbugWgt()
    window.show()
    sys.exit(app.exec_())
