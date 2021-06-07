from PyQt5.Qt import *
from TmainWgt import Ui_Form


class TmainWgt(QWidget, Ui_Form):

    Tshow_SPandCP_signal=pyqtSignal()
    TgiveTrade_signal=pyqtSignal()
    Tshow_summary_signal=pyqtSignal()
    Tlogout_signal=pyqtSignal()
    Tshow_summaryOfP_signal=pyqtSignal()
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


    def seeSPandCP(self):
        print("T请求查看供求")
        self.Tshow_SPandCP_signal.emit()

    def giveTrade(self):
        print("T请求给出交易建议")
        self.TgiveTrade_signal.emit()

    def Tsummary(self):
        print("T请求查看交易总结")
        self.Tshow_summary_signal.emit()

    def Tlogout(self):
        print("T注销")
        self.Tlogout_signal.emit()

    def TsummaryP(self):
        print("T请求查看统计P")
        self.Tshow_summaryOfP_signal.emit()




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = TmainWgt()
    window.show()
    sys.exit(app.exec_())
