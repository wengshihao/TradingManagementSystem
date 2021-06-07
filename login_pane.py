from PyQt5.Qt import *
from login import Ui_Form


class LoginPane(QWidget, Ui_Form):
    loginToMainpane_signal = pyqtSignal(str, str)
    show_register_pane_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def loginToMainpane(self):
        print("按钮被点击：登录主界面")
        self.loginToMainpane_signal.emit(self.accountLogComBox.currentText(), self.passwordLogLedit.text())

    def show_register_pane(self):
        print("按钮被点击：进入注册界面")
        self.show_register_pane_signal.emit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())
