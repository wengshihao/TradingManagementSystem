from PyQt5.Qt import *
from CmainWgt import Ui_Form


class CmainWgt(QWidget, Ui_Form):

    C_show_P_signal=pyqtSignal()
    C_logout_signal=pyqtSignal()
    C_show_CP_signal=pyqtSignal()
    C_show_SCP_signal=pyqtSignal()
    C_show_summary_signal=pyqtSignal()
    C_show_summaryOfP_signal=pyqtSignal()
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def CopenP(self):
        print("C请求打开P")
        self.C_show_P_signal.emit()

    def CopenCP(self):
        print("C请求打开CP")
        self.C_show_CP_signal.emit()

    def CopenSCP(self):
        print("C请求打开SCP")
        self.C_show_SCP_signal.emit()

    def CopenSummary(self):
        print("C请求打开总结")
        self.C_show_summary_signal.emit()

    def Clogout(self):
        print("C请求注销")
        self.C_logout_signal.emit()

    def CsummaryP(self):
        print("C请求打开总结P")
        self.C_show_summaryOfP_signal.emit()



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = CmainWgt()
    window.show()
    sys.exit(app.exec_())
