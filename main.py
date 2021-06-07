from PyQt5.Qt import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5 import QtGui,QtCore,QtWidgets,QtSql
from login_pane import LoginPane
from register_pane import RegisterPane
from SmainWgt_pane import SmainWgt
from SseeP_Wgt_pane import SseePWgt
from SsupplyWgt_pane import SsuplyWgt
from SchangeSupplyWgt_pane import SchangeSuplyWgt
from changeWgt_pane import ChangeWgt
from ScfmTradeShowSCP_pane import ScfmTradeShowSCPWgt
from cfmTradeWgt_pane import CfmTradeWgt
from S_summaryWgt_pane import SsummaryWgt
from CmainWgt_pane import CmainWgt
from CopenPWgt_pane import CopenPWgt
from CbugWgt_pane import CbugWgt
from CchangeButWgt_pane import CchangebutWgt
from CopenSCP_pane import CopenSCP
from C_summaryWgt_pane import CsummaryWgt
from TmainWgt_pane import TmainWgt
from TopenSPandCPWgt_pane import TopenSPandCPWgt
from TgiveTadeWgt_pane import TgiveTadeWgt
from T_summaryWgt_pane import TsummaryWgt
from summaryOfPWgt_pane import SummaryOfPWgt
import datetime,time
########################################################
def show_register_pane():
    Register_Pane.show()
def return_to_login_pane():
    Register_Pane.close()
def register_to_db_login_pane():
    # 插入账号密码
    query = QSqlQuery()
    if Register_Pane.supplierRiobtn.isChecked():
        insert_sql = 'INSERT INTO sys_S_login_cfg VALUES(?,?)'
    elif Register_Pane.customerRiobtn.isChecked():
        insert_sql = 'INSERT INTO sys_C_login_cfg VALUES(?,?)'
    else:
        insert_sql = 'INSERT INTO sys_T_login_cfg VALUES(?,?)'
    query.prepare(insert_sql)
    query.addBindValue(Register_Pane.accountLedit.text())
    query.addBindValue(Register_Pane.passwordLedit.text())
    if not query.exec_():
        print("插入账号密码失败！")
    else:
        print('插入账号密码成功')
    Register_Pane.close()
def checkAndLogin(acc, pas):
    query = QSqlQuery()
    global currentType
    if Login_Pane.supplierLogRiobtn.isChecked():
        search_query = 'SELECT * FROM sys_S_login_cfg'
        currentType = 0
    elif Login_Pane.customerLogRiobtn.isChecked():
        search_query = 'SELECT * FROM sys_C_login_cfg'
        currentType = 1
    else:
        search_query = 'SELECT * FROM sys_T_login_cfg'
        currentType = 2
    query.exec_(search_query)
    isEffectiveAcPa = False
    while (query.next()):
        if query.value(0) == acc and query.value(1) == pas:
            isEffectiveAcPa = True
            break
    if isEffectiveAcPa == False:
        print("登录失败")
        QMessageBox.information(None, "登录失败", "账号或密码错误", QMessageBox.Yes)
    else:
        print("登录主界面成功")
        global  currentAccount
        currentAccount=acc
        if currentType==0:
            SmainWgt_Pane.show()
        elif currentType==1:
            CmainWgt_Pane.show()
        else:
            TmainWgt_Pane.show()
        Login_Pane.close()
def show_summary_p():
    query = QSqlQuery("select scp.pno,p.PNAME,max(scp.SCPPRS),min(scp.SCPPRS),avg(scp.SCPPRS)  from scp,p where scp.pno=p.pno group by scp.pno,p.PNAME")
    SummaryOfPWgt_Pane.model.setQuery(query)
    SummaryOfPWgt_Pane.tableView.setColumnWidth(0, 150)
    SummaryOfPWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    SummaryOfPWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '零件编号')
    SummaryOfPWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '零件名')
    SummaryOfPWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '最高价')
    SummaryOfPWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '最低价')
    SummaryOfPWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '平均价')
    ######################
    query = QSqlQuery(
        "select s.sname,scp.pno,p.pname,scp.SCPPRS from scp,s,p where s.sno=scp.sno and scp.CCFM='同意交易' and scp.SCFM='同意交易' and p.pno=scp.pno")
    SummaryOfPWgt_Pane.model2.setQuery(query)
    SummaryOfPWgt_Pane.tableView_2.setColumnWidth(0, 300)
    SummaryOfPWgt_Pane.tableView_2.setColumnWidth(1, 150)
    SummaryOfPWgt_Pane.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
    SummaryOfPWgt_Pane.model2.setHeaderData(0, QtCore.Qt.Horizontal, '供应商名')
    SummaryOfPWgt_Pane.model2.setHeaderData(1, QtCore.Qt.Horizontal, '零件编号')
    SummaryOfPWgt_Pane.model2.setHeaderData(2, QtCore.Qt.Horizontal, '零件名')
    SummaryOfPWgt_Pane.model2.setHeaderData(3, QtCore.Qt.Horizontal, '成交价')

    SummaryOfPWgt_Pane .show()
########################################################################################
def S_show_P():
    query = QSqlQuery("select * from P")
    SseePWgt_Pane.model.setQuery(query)
    SseePWgt_Pane.tableView.resizeColumnsToContents()
    SseePWgt_Pane.tableView.resizeRowsToContents()
    SseePWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    SseePWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '编号')
    SseePWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '名字')
    SseePWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '重量(kg)')
    SseePWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '颜色')
    SseePWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '简介')
    SseePWgt_Pane.show()
def S_supplydoubleClickedHandle():
    nowrow=SseePWgt_Pane.tableView.currentIndex().row()
    ind=SseePWgt_Pane.model.index(nowrow,0)
    clickedPNO=SseePWgt_Pane.model.data(ind)
    S_show_supply_pane(clickedPNO)
def S_show_supply_pane(PNO):
    global currentAccount
    SsupplyWgt_Pane.SsupplyWgt_SnoLedit.setText(currentAccount)
    SsupplyWgt_Pane.SsupplyWgt_PnoLedit.setText(PNO)
    SsupplyWgt_Pane.show()
def S_Logout():
    SmainWgt_Pane.close()
    Login_Pane.show()
def S_cfmSupply(suplyNum,suplyPrice):
    print('数量和价格',suplyNum,suplyPrice)
    query = QSqlQuery()
    # 获取当前时间
    now_time = datetime.datetime.now()
    str_time = now_time.strftime("%Y-%m-%d %X")
    insert_sql = 'INSERT INTO SP VALUES(?,?,?,?,?)'
    query.prepare(insert_sql)
    query.addBindValue(SsupplyWgt_Pane.SsupplyWgt_SnoLedit.text())
    query.addBindValue(SsupplyWgt_Pane.SsupplyWgt_PnoLedit.text())
    query.addBindValue(SsupplyWgt_Pane.SsupplyWgt_NumLedit.text())
    query.addBindValue(SsupplyWgt_Pane.SsupplyWgt_PriceLedit.text())
    query.addBindValue(str_time)
    if not query.exec_():
        print("插入供应失败！")
        QMessageBox.information(None, "失败", "供应失败！该零件已存在供应或格式错误", QMessageBox.Yes)
    else:
        print('插入供应成功')
        QMessageBox.information(None, "成功", "供应成功", QMessageBox.Yes)
        SsupplyWgt_Pane.close()
def S_show_SP():
    global currentAccount
    query = QSqlQuery("select P.PNO,PName,SPNUM,SPPRS,sptime from P,SP where sp.sno='"+currentAccount+"' and p.pno=sp.pno")
    SchangeSuplyWgt_Pane.model.setQuery(query)
    SchangeSuplyWgt_Pane.tableView.resizeColumnsToContents()
    SchangeSuplyWgt_Pane.tableView.resizeRowsToContents()
    SchangeSuplyWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    SchangeSuplyWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '编号')
    SchangeSuplyWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '名字')
    SchangeSuplyWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '数量')
    SchangeSuplyWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '价格')
    SchangeSuplyWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '供应时间')
    SchangeSuplyWgt_Pane.show()
def S_changethisitem(changeTarget):
    global currentType
    global currentInd
    global currentAccount
    global currentPno
    if currentType==0:
        query = QSqlQuery()
        if currentInd==2:
            change_sql="update sp set spnum="+changeTarget+"where sno='"+currentAccount+"' and pno='"+currentPno+"'"
        elif currentInd==3:
            change_sql = "update sp set spprs=" + changeTarget + "where sno='" + currentAccount + "' and pno='" + currentPno + "'"
        query.prepare(change_sql)
        if query.exec_():
            print("修改成功")
        else:
            print("修改失败")
        ChangeWgt_Pane.close()
        SchangeSuplyWgt_Pane.close()
    elif currentType==1:
        query = QSqlQuery()
        if currentInd == 2:
            change_sql = "update cp set cpnum=" + changeTarget + "where cno='" + currentAccount + "' and pno='" + currentPno + "'"
        elif currentInd == 3:
            change_sql = "update cp set cpprs=" + changeTarget + "where cno='" + currentAccount + "' and pno='" + currentPno + "'"
        query.prepare(change_sql)
        if query.exec_():
            print("修改成功")
        else:
            print("修改失败")
        ChangeWgt_Pane.close()
        CchangebutWgt_Pane.close()
def S_change_doubleClickedHandle():
    global currentType
    global currentPno
    global currentInd
    if currentType==0:
        nowrow = SchangeSuplyWgt_Pane.tableView.currentIndex().row()
        nowcol = SchangeSuplyWgt_Pane.tableView.currentIndex().column()
        ind = SchangeSuplyWgt_Pane.model.index(nowrow, nowcol)
        clickeddata = SchangeSuplyWgt_Pane.model.data(ind)
        ChangeWgt_Pane.lineEdit.setText(str(clickeddata))
        ind2=SchangeSuplyWgt_Pane.model.index(nowrow,0)
        currentPno=SchangeSuplyWgt_Pane.model.data(ind2)
        currentInd=nowcol
        if nowcol==2 or nowcol==3:
            ChangeWgt_Pane.show()
    elif currentType==1:
        nowrow = CchangebutWgt_Pane.tableView.currentIndex().row()
        nowcol = CchangebutWgt_Pane.tableView.currentIndex().column()
        ind = CchangebutWgt_Pane.model.index(nowrow, nowcol)
        clickeddata = CchangebutWgt_Pane.model.data(ind)
        ChangeWgt_Pane.lineEdit.setText(str(clickeddata))
        ind2 = CchangebutWgt_Pane.model.index(nowrow, 0)
        currentPno = CchangebutWgt_Pane.model.data(ind2)
        currentInd = nowcol
        if nowcol==2 or nowcol==3:
            ChangeWgt_Pane.show()
def S_show_SCP():
    global currentAccount
    query = QSqlQuery("SELECT SCP.SCPNO,SCP.PNO,P.PNAME,SCP.CNO,C.CNAME,SCP.SCPNUM,SCP.SCPPRS,SCP.SCFM,SCP.CCFM,SCP.begscptime,scptime FROM SCP,P,C "
                      "WHERE SCP.PNO=P.PNO AND SCP.CNO=C.CNO AND SCP.SNO='"+currentAccount+"'")
    ScfmTradeShowSCPWgt_Pane.model.setQuery(query)
    ScfmTradeShowSCPWgt_Pane.tableView.setColumnWidth(0,150)
    ScfmTradeShowSCPWgt_Pane.tableView.setColumnWidth(6, 150)
    ScfmTradeShowSCPWgt_Pane.tableView.setColumnWidth(7, 150)
    ScfmTradeShowSCPWgt_Pane.tableView.setColumnWidth(8, 150)
    ScfmTradeShowSCPWgt_Pane.tableView.setColumnWidth(9, 350)
    ScfmTradeShowSCPWgt_Pane.tableView.setColumnWidth(10, 350)
    #ScfmTradeShowSCPWgt_Pane.tableView.resizeRowsToContents()
    ScfmTradeShowSCPWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '零件号')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '零件名')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '顾客号')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '顾客名')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(5, QtCore.Qt.Horizontal, '数量')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(6, QtCore.Qt.Horizontal, '成交单价')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(7, QtCore.Qt.Horizontal, '供应商确认')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(8, QtCore.Qt.Horizontal, '顾客确认')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(9, QtCore.Qt.Horizontal, '订单创建时间')
    ScfmTradeShowSCPWgt_Pane.model.setHeaderData(10, QtCore.Qt.Horizontal, '订单完成时间')
    ScfmTradeShowSCPWgt_Pane.show()
def S_show_cfmTradeWgt():
    CfmTradeWgt_Pane.textEdit.setText("无特殊原因。")
    CfmTradeWgt_Pane.show()
def agreeTradeChangeSCP():
    global currentType
    global currentAccount
    query = QSqlQuery()
    now_time = datetime.datetime.now()
    str_time = now_time.strftime("%Y-%m-%d %X")
    if currentType==0:
        nowrow = ScfmTradeShowSCPWgt_Pane.tableView.currentIndex().row()
        ind = ScfmTradeShowSCPWgt_Pane.model.index(nowrow, 0)
        clickSCPNO = ScfmTradeShowSCPWgt_Pane.model.data(ind)
        change_quert = "update  scp set scfm='同意交易' where scpno='"+clickSCPNO+"'"
    elif currentType==1:
        nowrow = CopenSCP_Pane.tableView.currentIndex().row()
        ind = CopenSCP_Pane.model.index(nowrow, 0)
        clickSCPNO = CopenSCP_Pane.model.data(ind)
        change_quert = "update  scp set ccfm='同意交易' where scpno='" +clickSCPNO + "'"
    query.prepare(change_quert)
    if query.exec_():
        print("同意交易成功")
    else:
        print("同意交易失败")
    if currentType==0:
        query2=QSqlQuery()
        print(clickSCPNO)
        QUE="select ccfm from scp where scpno='" +clickSCPNO + "'"
        query2.exec_(QUE)
        query2.next()
        print(query2.value(0))
        if query2.value(0)=="同意交易":
            query3=QSqlQuery()
            qq="update scp set scptime='" + str_time + "' where scpno='" + clickSCPNO + "'"
            query3.exec_(qq)
    elif currentType==1:
        query2=QSqlQuery()
        print(clickSCPNO)
        QUE="select scfm from scp where scpno='" +clickSCPNO + "'"
        query2.exec_(QUE)
        query2.next()
        print(query2.value(0))
        if query2.value(0)=="同意交易":
            query3=QSqlQuery()
            qq="update scp set scptime='" + str_time + "' where scpno='" + clickSCPNO + "'"
            query3.exec_(qq)
    CfmTradeWgt_Pane.close()
def refuseTradeChangeSCP(reason):
    global currentType
    global currentAccount
    now_time = datetime.datetime.now()
    str_time = now_time.strftime("%Y-%m-%d %X")
    query = QSqlQuery()
    if currentType == 0:
        nowrow = ScfmTradeShowSCPWgt_Pane.tableView.currentIndex().row()
        ind = ScfmTradeShowSCPWgt_Pane.model.index(nowrow, 0)
        clickSCPNO = ScfmTradeShowSCPWgt_Pane.model.data(ind)
        change_quert = "update  scp set scfm='拒绝' where scpno='" + clickSCPNO + "'"
    elif currentType == 1:
        nowrow = CopenSCP_Pane.tableView.currentIndex().row()
        ind = CopenSCP_Pane.model.index(nowrow, 0)
        clickSCPNO = CopenSCP_Pane.model.data(ind)
        change_quert = "update  scp set ccfm='拒绝' where scpno='" + clickSCPNO + "'"
    query.prepare(change_quert)
    if query.exec_():
        print("拒绝交易成功")
    else:
        print("拒绝交易失败")
    query2=QSqlQuery()
    if currentType==1:
        inset_sql="insert into refuseReason values('"+clickSCPNO+"',NULL,'"+reason+"')"
    elif currentType == 0:
        inset_sql = "insert into refuseReason values('" + clickSCPNO + "','" + reason + "',NULL)"
    query2.prepare(inset_sql)
    if query2.exec_():
        print("插入原因成功")
    else:
        print("插入原因失败")
    query3 = QSqlQuery()
    qq = "update scp set scptime='" + str_time + "' where scpno='" + clickSCPNO + "'"
    query3.exec_(qq)
    CfmTradeWgt_Pane.close()
def S_show_Summary():
    global currentAccount
    query = QSqlQuery()
    select_sql="select SUM(SCP.SCPPRS*SCP.SCPNUM) from SCP WHERE SNO='"+currentAccount+"' AND SCP.SCFM='同意交易' AND SCP.CCFM='同意交易'"
    if query.exec_(select_sql):
        print("计算总交易额成功")
    else:
        print("计算总交易额失败")
    query.next()
    sumTrade=query.value(0)
    sumTrade=round(sumTrade,1)
    SsummaryWgt_Pane.label_2.setText(str(sumTrade)+"元")
    ####################
    query2 = QSqlQuery("select scpno,scp.cno,c.cname,scp.pno,pname,scpnum*SCP.SCPPRS from scp,p,c where scp.pno=p.pno and scp.sno='"+currentAccount+"' and SCP.SCFM='同意交易' AND SCP.CCFM='同意交易' and c.cno=scp.cno")
    SsummaryWgt_Pane.model.setQuery(query2)
    SsummaryWgt_Pane.tableView.resizeColumnsToContents()
    SsummaryWgt_Pane.tableView.resizeRowsToContents()
    SsummaryWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    SsummaryWgt_Pane.tableView.setColumnWidth(1, 80)
    SsummaryWgt_Pane.tableView.setColumnWidth(3, 80)
    SsummaryWgt_Pane.tableView.setColumnWidth(4, 80)
    SsummaryWgt_Pane.tableView.setColumnWidth(5, 80)
    SsummaryWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    SsummaryWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '顾客号')
    SsummaryWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '顾客名')
    SsummaryWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '零件号')
    SsummaryWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '零件名')
    SsummaryWgt_Pane.model.setHeaderData(5, QtCore.Qt.Horizontal, '收入')
    #######################
    query3 = QSqlQuery("select scp.scpno,refuseReason.SREASON from scp, refuseReason where scp.SCPNO = refuseReason.SCPNO and scp.sno = '"+currentAccount+"' and scp.SCFM='拒绝'")
    SsummaryWgt_Pane.model2.setQuery(query3)
    SsummaryWgt_Pane.tableView_2.resizeColumnsToContents()
    SsummaryWgt_Pane.tableView_2.resizeRowsToContents()
    SsummaryWgt_Pane.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
    SsummaryWgt_Pane.model2.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    SsummaryWgt_Pane.model2.setHeaderData(1, QtCore.Qt.Horizontal, '拒绝原因')
    ########################
    query4 = QSqlQuery(
        "select scp.scpno,refuseReason.CREASON from scp, refuseReason where scp.SCPNO = refuseReason.SCPNO and scp.sno = '" + currentAccount + "' and scp.CCFM='拒绝'")
    SsummaryWgt_Pane.model3.setQuery(query4)
    SsummaryWgt_Pane.tableView_3.resizeColumnsToContents()
    SsummaryWgt_Pane.tableView_3.resizeRowsToContents()
    SsummaryWgt_Pane.tableView_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
    SsummaryWgt_Pane.model3.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    SsummaryWgt_Pane.model3.setHeaderData(1, QtCore.Qt.Horizontal, '拒绝原因')
    SsummaryWgt_Pane.show()
################################################################################################C
def C_logout():
    CmainWgt_Pane.close()
    Login_Pane.show()
def C_show_P():
    query = QSqlQuery("select * from P")
    CopenPWgt_Pane.model.setQuery(query)
    CopenPWgt_Pane.tableView.resizeColumnsToContents()
    CopenPWgt_Pane.tableView.resizeRowsToContents()
    CopenPWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    CopenPWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '编号')
    CopenPWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '名字')
    CopenPWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '重量(kg)')
    CopenPWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '颜色')
    CopenPWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '简介')
    CopenPWgt_Pane.show()
def C_show_buy():
    nowrow = CopenPWgt_Pane.tableView.currentIndex().row()
    ind = CopenPWgt_Pane.model.index(nowrow, 0)
    clickedPNO = CopenPWgt_Pane.model.data(ind)
    print(clickedPNO)
    global currentAccount
    CbugWgt_Pane.SsupplyWgt_SnoLedit_2.setText(currentAccount)
    CbugWgt_Pane.SsupplyWgt_PnoLedit_2.setText(clickedPNO)
    CbugWgt_Pane.show()
def C_cfm_buy(buynum,buyPrice):
    print('数量和价格', buynum,buyPrice)
    query = QSqlQuery()
    # 获取当前时间
    now_time = datetime.datetime.now()
    str_time = now_time.strftime("%Y-%m-%d %X")
    insert_sql = 'INSERT INTO CP VALUES(?,?,?,?,?)'
    query.prepare(insert_sql)
    query.addBindValue(CbugWgt_Pane.SsupplyWgt_SnoLedit_2.text())
    query.addBindValue(CbugWgt_Pane.SsupplyWgt_PnoLedit_2.text())
    query.addBindValue(buynum)
    query.addBindValue(buyPrice)
    query.addBindValue(str_time)
    if not query.exec_():
        print("插入求购失败！")
        QMessageBox.information(None, "失败", "求购失败！该零件已存在求购或格式错误", QMessageBox.Yes)
    else:
        print('插入求购成功')
        QMessageBox.information(None, "成功", "求购成功", QMessageBox.Yes)
        CbugWgt_Pane.close()
def C_show_CP():
    global currentAccount
    query = QSqlQuery("select P.PNO,PName,CPNUM,CPPRS,CPTIME from P,CP where cp.cno='"+currentAccount+"' and p.pno=cp.pno")
    CchangebutWgt_Pane.model.setQuery(query)
    CchangebutWgt_Pane.tableView.resizeColumnsToContents()
    CchangebutWgt_Pane.tableView.resizeRowsToContents()
    CchangebutWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    CchangebutWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '编号')
    CchangebutWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '名字')
    CchangebutWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '数量')
    CchangebutWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '价格')
    CchangebutWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '求购时间')
    CchangebutWgt_Pane.show()
def C_show_SCP():
    global currentAccount
    query = QSqlQuery(
        "SELECT SCP.SCPNO,SCP.PNO,P.PNAME,SCP.SNO,S.SNAME,SCP.SCPNUM,SCP.SCPPRS,SCP.SCFM,SCP.CCFM,SCP.begscptime,scptime FROM SCP,P,S "
        "WHERE SCP.PNO=P.PNO AND SCP.SNO=S.SNO AND SCP.CNO='" + currentAccount + "'")
    CopenSCP_Pane.model.setQuery(query)
    CopenSCP_Pane.tableView.setColumnWidth(4, 280)
    CopenSCP_Pane.tableView.setColumnWidth(7, 120)
    CopenSCP_Pane.tableView.setColumnWidth(8, 120)
    CopenSCP_Pane.tableView.setColumnWidth(9, 320)
    CopenSCP_Pane.tableView.setColumnWidth(10, 320)
    # ScfmTradeShowSCPWgt_Pane.tableView.resizeRowsToContents()
    CopenSCP_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    CopenSCP_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    CopenSCP_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '零件号')
    CopenSCP_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '零件名')
    CopenSCP_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '商家号')
    CopenSCP_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '商家名')
    CopenSCP_Pane.model.setHeaderData(5, QtCore.Qt.Horizontal, '数量')
    CopenSCP_Pane.model.setHeaderData(6, QtCore.Qt.Horizontal, '成交单价')
    CopenSCP_Pane.model.setHeaderData(7, QtCore.Qt.Horizontal, '供应商确认')
    CopenSCP_Pane.model.setHeaderData(8, QtCore.Qt.Horizontal, '顾客确认')
    CopenSCP_Pane.model.setHeaderData(9, QtCore.Qt.Horizontal, '订单创建时间')
    CopenSCP_Pane.model.setHeaderData(10, QtCore.Qt.Horizontal, '订单完成时间')
    CopenSCP_Pane.show()
def C_show_Summary():
    global currentAccount
    query = QSqlQuery()
    select_sql = "select SUM(SCP.SCPPRS*SCP.SCPNUM) from SCP WHERE CNO='" + currentAccount + "' AND SCP.SCFM='同意交易' AND SCP.CCFM='同意交易'"
    if query.exec_(select_sql):
        print("计算总交易额成功")
    else:
        print("计算总交易额失败")
    query.next()
    sumTrade = query.value(0)
    CsummaryWgt_Pane.label_2.setText(str(sumTrade) + "元")
    ####################
    query2 = QSqlQuery(
        "select scpno,scp.sno,s.sname,scp.pno,pname,scpnum*SCP.SCPPRS from scp,p,s where scp.pno=p.pno and scp.cno='" + currentAccount + "' and SCP.SCFM='同意交易' AND SCP.CCFM='同意交易' and s.sno=scp.sno")
    CsummaryWgt_Pane.model.setQuery(query2)
    CsummaryWgt_Pane.tableView.resizeColumnsToContents()
    CsummaryWgt_Pane.tableView.resizeRowsToContents()
    CsummaryWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    CsummaryWgt_Pane.tableView.setColumnWidth(1, 80)
    CsummaryWgt_Pane.tableView.setColumnWidth(3, 80)
    CsummaryWgt_Pane.tableView.setColumnWidth(4, 80)
    CsummaryWgt_Pane.tableView.setColumnWidth(5, 80)
    CsummaryWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    CsummaryWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '商家号')
    CsummaryWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '商家名')
    CsummaryWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '零件号')
    CsummaryWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '零件名')
    CsummaryWgt_Pane.model.setHeaderData(5, QtCore.Qt.Horizontal, '收入')
    #######################
    query3 = QSqlQuery(
        "select scp.scpno,refuseReason.CREASON from scp, refuseReason where scp.SCPNO = refuseReason.SCPNO and scp.cno = '" + currentAccount + "' and scp.CCFM='拒绝'")
    CsummaryWgt_Pane.model2.setQuery(query3)
    CsummaryWgt_Pane.tableView_2.resizeColumnsToContents()
    CsummaryWgt_Pane.tableView_2.resizeRowsToContents()
    CsummaryWgt_Pane.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
    CsummaryWgt_Pane.model2.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    CsummaryWgt_Pane.model2.setHeaderData(1, QtCore.Qt.Horizontal, '拒绝原因')
    ########################
    query4 = QSqlQuery(
        "select scp.scpno,refuseReason.SREASON from scp, refuseReason where scp.SCPNO = refuseReason.SCPNO and scp.Cno = '" + currentAccount + "' and scp.SCFM='拒绝'")
    CsummaryWgt_Pane.model3.setQuery(query4)
    CsummaryWgt_Pane.tableView_3.resizeColumnsToContents()
    CsummaryWgt_Pane.tableView_3.resizeRowsToContents()
    CsummaryWgt_Pane.tableView_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
    CsummaryWgt_Pane.model3.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    CsummaryWgt_Pane.model3.setHeaderData(1, QtCore.Qt.Horizontal, '拒绝原因')
    CsummaryWgt_Pane.show()
################################################################3
def T_show_SPandCP():
    query = QSqlQuery("select sp.sno,sname,sp.pno,pname,spnum,spprs from sp,p,s where sp.pno=p.pno and s.sno=sp.sno")
    TopenSPandCPWgt_Pane.model.setQuery(query)
    TopenSPandCPWgt_Pane.tableView.resizeColumnsToContents()
    TopenSPandCPWgt_Pane.tableView.resizeRowsToContents()
    TopenSPandCPWgt_Pane.tableView.setColumnWidth(0, 100)
    TopenSPandCPWgt_Pane.tableView.setColumnWidth(2, 100)
    TopenSPandCPWgt_Pane.tableView.setColumnWidth(3, 100)
    TopenSPandCPWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    TopenSPandCPWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '商家号')
    TopenSPandCPWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '商家名')
    TopenSPandCPWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '零件号')
    TopenSPandCPWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '零件名')
    TopenSPandCPWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '数量')
    TopenSPandCPWgt_Pane.model.setHeaderData(5, QtCore.Qt.Horizontal, '单价')
    ##########################################################################################3
    query2 = QSqlQuery("select cp.cno,cname,cp.pno,pname,cpnum,cpprs from cp,p,c where cp.pno=p.pno and c.cno=cp.cno")
    TopenSPandCPWgt_Pane.model2.setQuery(query2)
    TopenSPandCPWgt_Pane.tableView_2.resizeColumnsToContents()
    TopenSPandCPWgt_Pane.tableView_2.resizeRowsToContents()
    TopenSPandCPWgt_Pane.tableView_2.setColumnWidth(0, 100)
    TopenSPandCPWgt_Pane.tableView_2.setColumnWidth(2, 100)
    TopenSPandCPWgt_Pane.tableView_2.setColumnWidth(3, 100)
    TopenSPandCPWgt_Pane.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
    TopenSPandCPWgt_Pane.model2.setHeaderData(0, QtCore.Qt.Horizontal, '顾客号')
    TopenSPandCPWgt_Pane.model2.setHeaderData(1, QtCore.Qt.Horizontal, '顾客名')
    TopenSPandCPWgt_Pane.model2.setHeaderData(2, QtCore.Qt.Horizontal, '零件号')
    TopenSPandCPWgt_Pane.model2.setHeaderData(3, QtCore.Qt.Horizontal, '零件名')
    TopenSPandCPWgt_Pane.model2.setHeaderData(4, QtCore.Qt.Horizontal, '数量')
    TopenSPandCPWgt_Pane.model2.setHeaderData(5, QtCore.Qt.Horizontal, '单价')

    TopenSPandCPWgt_Pane.show()
def T_show_giveTrade():
    global currentAccount
    TgiveTadeWgt_Pane.T_tnoLedit.setText(currentAccount)
    TgiveTadeWgt_Pane.show()
def T_cfmTradeAndinsertSCP():
    query = QSqlQuery()
    now_time = datetime.datetime.now()
    str_time = now_time.strftime("%Y-%m-%d %X")
    insert_sql = 'INSERT INTO SCP VALUES(?,?,?,?,?,?,?,?,?,?,?)'
    query.prepare(insert_sql)
    query.addBindValue(TgiveTadeWgt_Pane.T_scpnoLedit.text())
    query.addBindValue(TgiveTadeWgt_Pane.T_snoLedit.text())
    query.addBindValue(TgiveTadeWgt_Pane.T_cnoLedit.text())
    query.addBindValue(TgiveTadeWgt_Pane.T_pnoLedit.text())
    query.addBindValue(int(TgiveTadeWgt_Pane.T_numLedit.text()))
    query.addBindValue(float(TgiveTadeWgt_Pane.T_priceLedit.text()))
    query.addBindValue("未确认")
    query.addBindValue("未确认")
    query.addBindValue(TgiveTadeWgt_Pane.T_tnoLedit.text())
    query.addBindValue("未完成")
    query.addBindValue(str_time)
    if query.exec_():
        print("插入SCP成功")
        QMessageBox.information(None, "成功", "提出交易建议成功", QMessageBox.Yes)
    else:
        print("插入SCP失败")
        QMessageBox.information(None, "失败", "提出交易建议失败，请检查格式", QMessageBox.Yes)
    TgiveTadeWgt_Pane.close()
def T_show_summary():
    global currentAccount
    query = QSqlQuery()
    select_sql = "select SUM(SCP.SCPPRS*SCP.SCPNUM) from SCP WHERE TNO='" + currentAccount + "' AND SCP.SCFM='同意交易' AND SCP.CCFM='同意交易'"
    if query.exec_(select_sql):
        print("计算总交易额成功")
    else:
        print("计算总交易额失败")
    query.next()
    sumTrade = query.value(0)
    TsummaryWgt_Pane.cfmmoneyQlabel.setText(str(sumTrade) + "元")
    ####################
    query2 = QSqlQuery(
        "select scpno,scp.sno,s.sname,scp.pno,pname,scpnum*SCP.SCPPRS from scp,p,s where scp.pno=p.pno and scp.Tno='" + currentAccount + "' and SCP.SCFM='同意交易' AND SCP.CCFM='同意交易' and s.sno=scp.sno")
    TsummaryWgt_Pane.model.setQuery(query2)
    TsummaryWgt_Pane.tableView.resizeColumnsToContents()
    TsummaryWgt_Pane.tableView.resizeRowsToContents()
    TsummaryWgt_Pane.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    TsummaryWgt_Pane.tableView.setColumnWidth(1, 80)
    TsummaryWgt_Pane.tableView.setColumnWidth(3, 80)
    TsummaryWgt_Pane.tableView.setColumnWidth(4, 80)
    TsummaryWgt_Pane.tableView.setColumnWidth(5, 80)
    TsummaryWgt_Pane.model.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    TsummaryWgt_Pane.model.setHeaderData(1, QtCore.Qt.Horizontal, '商家号')
    TsummaryWgt_Pane.model.setHeaderData(2, QtCore.Qt.Horizontal, '商家名')
    TsummaryWgt_Pane.model.setHeaderData(3, QtCore.Qt.Horizontal, '零件号')
    TsummaryWgt_Pane.model.setHeaderData(4, QtCore.Qt.Horizontal, '零件名')
    TsummaryWgt_Pane.model.setHeaderData(5, QtCore.Qt.Horizontal, '成交额')
    #######################
    query3 = QSqlQuery(
        "select scp.scpno,refuseReason.CREASON from scp, refuseReason where scp.SCPNO = refuseReason.SCPNO and scp.Tno = '" + currentAccount + "' and scp.CCFM='拒绝'")
    TsummaryWgt_Pane.model2.setQuery(query3)
    TsummaryWgt_Pane.tableView_2.resizeColumnsToContents()
    TsummaryWgt_Pane.tableView_2.resizeRowsToContents()
    TsummaryWgt_Pane.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
    TsummaryWgt_Pane.model2.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    TsummaryWgt_Pane.model2.setHeaderData(1, QtCore.Qt.Horizontal, '拒绝原因')
    ########################
    query4 = QSqlQuery(
        "select scp.scpno,refuseReason.SREASON from scp, refuseReason where scp.SCPNO = refuseReason.SCPNO and scp.Tno = '" + currentAccount + "' and scp.SCFM='拒绝'")
    TsummaryWgt_Pane.model3.setQuery(query4)
    TsummaryWgt_Pane.tableView_3.resizeColumnsToContents()
    TsummaryWgt_Pane.tableView_3.resizeRowsToContents()
    TsummaryWgt_Pane.tableView_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
    TsummaryWgt_Pane.model3.setHeaderData(0, QtCore.Qt.Horizontal, '订单号')
    TsummaryWgt_Pane.model3.setHeaderData(1, QtCore.Qt.Horizontal, '拒绝原因')
    TsummaryWgt_Pane.show()
def Tlogout():
    TmainWgt_Pane.close()
    Login_Pane.show()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ########################################
    Login_Pane = LoginPane()
    SmainWgt_Pane = SmainWgt()
    Register_Pane = RegisterPane()
    SseePWgt_Pane=SseePWgt()
    SsupplyWgt_Pane=SsuplyWgt()
    SchangeSuplyWgt_Pane=SchangeSuplyWgt()
    ChangeWgt_Pane=ChangeWgt()
    ScfmTradeShowSCPWgt_Pane=ScfmTradeShowSCPWgt()
    CfmTradeWgt_Pane=CfmTradeWgt()
    SsummaryWgt_Pane=SsummaryWgt()
    CmainWgt_Pane=CmainWgt()
    CopenPWgt_Pane=CopenPWgt()
    CbugWgt_Pane=CbugWgt()
    CchangebutWgt_Pane=CchangebutWgt()
    CopenSCP_Pane=CopenSCP()
    CsummaryWgt_Pane=CsummaryWgt()
    TmainWgt_Pane=TmainWgt()
    TopenSPandCPWgt_Pane = TopenSPandCPWgt()
    TgiveTadeWgt_Pane=TgiveTadeWgt()
    TsummaryWgt_Pane=TsummaryWgt()
    SummaryOfPWgt_Pane=SummaryOfPWgt()
    #########################################

    Login_Pane.show()
    currentInd=0
    currentPno=''
    currentType = 0  # 目前用户类型 0为S 1为C 2为T
    currentAccount = ''  # 目前的用户用户名


    ##连接数据库##########################################################
    db = QSqlDatabase.addDatabase("QODBC")
    db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=PTMS;Uid=sa;Pwd=sasasasa")
    if not db.open():
        print("连接数据库失败！")
    else:
        print("连接数据库成功")
    #################################################################333

    ######################################################
    Login_Pane.show_register_pane_signal.connect(show_register_pane)
    Register_Pane.returnSignal.connect(return_to_login_pane)
    Register_Pane.registerSignal.connect(register_to_db_login_pane)
    Login_Pane.loginToMainpane_signal.connect(checkAndLogin)
    SmainWgt_Pane.SmainWgt_Logout_signal.connect(S_Logout)
    SsupplyWgt_Pane.ScfmSupply_signal.connect(S_cfmSupply)
    SmainWgt_Pane.SmainWgt_showSP_signal.connect(S_show_SP)
    SmainWgt_Pane.SmainWgt_showSCP_signal.connect(S_show_SCP)
    ChangeWgt_Pane.changeIt_signal.connect(S_changethisitem)
    SseePWgt_Pane.tableView.doubleClicked.connect(S_supplydoubleClickedHandle)
    CfmTradeWgt_Pane.agreeThisTrade_signal.connect(agreeTradeChangeSCP)
    CfmTradeWgt_Pane.refuseThisTrade_signal.connect(refuseTradeChangeSCP)
    ScfmTradeShowSCPWgt_Pane.tableView.doubleClicked.connect(S_show_cfmTradeWgt)
    CopenSCP_Pane.tableView.doubleClicked.connect(S_show_cfmTradeWgt)
    SmainWgt_Pane.SmainWgt_showSummary_signal.connect(S_show_Summary)
    CmainWgt_Pane.C_show_P_signal.connect(C_show_P)
    CmainWgt_Pane.C_logout_signal.connect(C_logout)
    CopenPWgt_Pane.tableView.doubleClicked.connect(C_show_buy)
    CbugWgt_Pane.C_cfm_buy_signal.connect(C_cfm_buy)
    CmainWgt_Pane.C_show_CP_signal.connect(C_show_CP)
    SchangeSuplyWgt_Pane.tableView.doubleClicked.connect(S_change_doubleClickedHandle)
    CchangebutWgt_Pane.tableView.doubleClicked.connect(S_change_doubleClickedHandle)
    CmainWgt_Pane.C_show_SCP_signal.connect(C_show_SCP)
    CmainWgt_Pane.C_show_summary_signal.connect(C_show_Summary)
    TmainWgt_Pane.Tshow_SPandCP_signal.connect(T_show_SPandCP)
    TmainWgt_Pane.TgiveTrade_signal.connect(T_show_giveTrade)
    TgiveTadeWgt_Pane.T_cfmTrade_signal.connect(T_cfmTradeAndinsertSCP)
    TmainWgt_Pane.Tshow_summary_signal.connect(T_show_summary)
    TmainWgt_Pane.Tlogout_signal.connect(Tlogout)
    SmainWgt_Pane.SmainWgt_showSummaryofP_signal.connect(show_summary_p)
    CmainWgt_Pane.C_show_summaryOfP_signal.connect(show_summary_p)
    TmainWgt_Pane.Tshow_summaryOfP_signal.connect(show_summary_p)
    #####################################################


    SmainWgt_Pane.SmainWgt_showP_signal.connect(S_show_P)
    sys.exit(app.exec_())
