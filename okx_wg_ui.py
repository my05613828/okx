import sys
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import uic
import okx_wg_trade
import position_information
class my_thread(QThread):
    start_signal = pyqtSignal(dict)
    datas = None
    def __init__(self):
        super(my_thread, self).__init__()

    def start_slot(self, data: dict):
        self.datas = data

    def run(self):
        print(self.datas)
        # 策略调用
        okx_wg_trade.wg_trade(self.datas)

class my_window(QWidget):
    ui = None
    data_information = None
    my_threading = None

    def __init__(self):
        super(my_window, self).__init__()
        self.__init_ui__()
    def __init_ui__(self,path :str = "./okx_wg.ui",title: str = "江苏鑫起点信息技术服务有限公司"):
        self.ui = uic.loadUi(path)
        self.ui.setWindowTitle(title)
        self.ui.setWindowIcon(QIcon('logo.ico'))
        # 线程
        self.ui.pushButton_3.clicked.connect(self.start_end)
        # 手工面板
        self.ui.pushButton_4.clicked.connect(self.open_buy_peice_slot)
        self.ui.pushButton_2.clicked.connect(self.open_sell_peice_slot)
        self.ui.pushButton.clicked.connect(self.close_long_peice_slot)
        self.ui.pushButton_8.clicked.connect(self.close_short_peice_slot)
        # 市价平单
        self.ui.pushButton_6.clicked.connect(self.close_long_peices_slot)
        self.ui.pushButton_9.clicked.connect(self.close_short_peices_slot)
        self.ui.pushButton_5.clicked.connect(self.close_all_peices_slot)

        self.my_threading = my_thread()
        self.my_threading.start_signal.connect(self.my_threading.start_slot)
        self.data_information = self.get_data_information()
        self.append_ui_log("初始化")

    def get_data(self):
        api = self.get_ui_api()
        api_key = self.get_ui_api_key()
        password = self.get_ui_password()
        flag = self.get_ui_demo()
        open_long = self.get_ui_long()
        open_short = self.get_ui_short()
        symbol = self.get_ui_symbol()
        peice = self.get_ui_peice()

        peice_lit = self.get_ui_peices_lit()
        percent_add = self.get_ui_percent_add()
        percent_out = self.get_ui_percent_out()
        tp_profits = self.get_ui_tp_profits()
        sl_profits = self.get_ui_sl_profits()
        data = {"api": api,
                     "api_key": api_key,
                     "password": password,
                     "flag": flag,
                     "open_long": open_long,
                     "open_short": open_short,
                     "symbol": symbol,
                     "peice": peice,
                     "peice_lit": peice_lit,
                     "percent_add": percent_add,
                     "percent_out": percent_out,
                     "tp_profits": tp_profits,
                     "sl_profits": sl_profits
                     }
        return data

    def get_data_information(self):
        api = self.get_ui_api()
        api_key = self.get_ui_api_key()
        password = self.get_ui_password()
        flag = self.get_ui_demo()
        symbol = self.get_ui_symbol()

        data_information = {
            "api": api,
            "api_key": api_key,
            "password": password,
            "flag": flag,
            "symbol": symbol
        }
        return data_information

    # 控制线程的启动运行
    def start_end(self):
        if self.get_ui_start() == "启动":
            self.set_ui_start("运行")
            self.append_ui_log("策略运行")

            #获取控件data数据
            data = self.get_data()
            self.data_information = self.get_data_information()
            self.my_threading.start_signal.emit(data)
            self.my_threading.start()
            #启动定时器 显示数据
            self.mytimer = QTimer()
            self.mytimer.timeout.connect(self.onTimer)
            self.mytimer.start(500)
        else:
            self.set_ui_start("启动")

            self.my_threading.terminate()  # 结束此进程
            self.my_threading.wait()  # 等待结束完成
            if self.my_threading.isFinished():  # 如果当前线程已经完成工作，则删除
                self.append_ui_log("策略终止")
    #用于显示tablewidget 数据
    def onTimer(self):
        try:
            long_list, short_list,sum_list = position_information.information(self.data_information)
            i , f = 0, 0
            for e in long_list:
                self.ui.tableWidget.setItem(0,i , QTableWidgetItem(str(e)))  # 在第一行第一列设置文本
                i += 1
            for e in short_list:
                self.ui.tableWidget.setItem(1,f, QTableWidgetItem(str(e)))  # 在第二行第一列设置文本
                f += 1
            self.ui.tableWidget.setItem(2, 1, QTableWidgetItem(sum_list[0]))
            self.ui.tableWidget.setItem(2, 5, QTableWidgetItem(sum_list[1]))
        except:
            print("信息获取中...")
            time.sleep(0.3)


    # 获取API KEY
    def get_ui_api(self):
        return self.ui.lineEdit_3.text()
    def get_ui_api_key(self):
        return self.ui.lineEdit.text()
    def get_ui_password(self):
        return self.ui.lineEdit_2.text()
    #模拟实盘选中
    def get_ui_demo(self):
        return self.ui.radioButton_2.isChecked()
    def get_ui_real(self):
        return self.ui.radioButton.isChecked()


    #获取策略参数
    #做多 做空被选中
    def get_ui_long(self):
        return self.ui.checkBox.isChecked()
    def get_ui_short(self):
        return self.ui.checkBox_2.isChecked()
    def get_ui_symbol(self):
        return self.ui.lineEdit_12.text()
    def get_ui_peice(self):
        return int(self.ui.lineEdit_5.text())
    def get_ui_peices_lit(self):
        return int(self.ui.lineEdit_6.text())
    def get_ui_percent_add(self):
        return float(self.ui.lineEdit_7.text())
    def get_ui_percent_out(self):
        return float(self.ui.lineEdit_9.text())
    def get_ui_tp_profits(self):
        return float(self.ui.lineEdit_4.text())
    def get_ui_sl_profits(self):
        return float(self.ui.lineEdit_8.text())

    def get_ui_open_peice(self):
        return int(self.ui.lineEdit_10.text())
    def get_ui_close_peice(self):
        return int(self.ui.lineEdit_11.text())

    #获取启动按钮状态
    def get_ui_start(self):
        return self.ui.pushButton_3.text()
    def set_ui_start(self,msg:str):
        return self.ui.pushButton_3.setText(msg)
    def append_ui_log(self,msg =" ",fun_name = sys._getframe().f_code.co_name):
        self.ui.textEdit.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" "+fun_name +" execute " +msg)

    # 手工面板
    def open_buy_peice_slot(self):
        position_information.open_buy_peice(self.data_information,self.get_ui_open_peice())
        self.append_ui_log("开多")
    def open_sell_peice_slot(self):
        position_information.open_sell_peice(self.data_information, self.get_ui_open_peice())
        self.append_ui_log("开空")

    def close_long_peice_slot(self):
        position_information.close_long_peice(self.data_information, self.get_ui_close_peice())
        self.append_ui_log("平多")
    def close_short_peice_slot(self):
        position_information.close_short_peice(self.data_information, self.get_ui_close_peice())
        self.append_ui_log("平空")

    def close_long_peices_slot(self):
        position_information.close_long_peices(self.data_information)
        self.append_ui_log("市价平多")
    def close_short_peices_slot(self):
        position_information.close_short_peices(self.data_information)
        self.append_ui_log("市价平空")
    def close_all_peices_slot(self):
        position_information.close_all_peices(self.data_information)
        self.append_ui_log("市价全平")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = my_window()
    w.ui.show()
    app.exec()