from PyQt5.Qt import *
from TgiveTadeWgt import Ui_Form


class TgiveTadeWgt(QWidget, Ui_Form):

    T_cfmTrade_signal=pyqtSignal()
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def TcfmGiveTrade(self):
        print("T确认提出订单")
        self.T_cfmTrade_signal.emit()



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = TgiveTadeWgt()
    window.show()
    sys.exit(app.exec_())
