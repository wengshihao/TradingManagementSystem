from PyQt5.Qt import *
from T_summaryWgt import Ui_Form
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5 import QtGui,QtCore,QtWidgets,QtSql

class TsummaryWgt(QWidget, Ui_Form):

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.model = QtSql.QSqlTableModel()
        self.tableView.setModel(self.model)
        self.model2=QtSql.QSqlTableModel()
        self.tableView_2.setModel(self.model2)
        self.model3 = QtSql.QSqlTableModel()
        self.tableView_3.setModel(self.model3)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window =TsummaryWgt()
    window.show()
    sys.exit(app.exec_())
