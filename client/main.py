import sys
import os
import pathlib
import datetime
import shutil
import hashlib
import psycopg2
from interface import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from Custom_Widgets.Widgets import *
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_4.clicked.connect(self.select_files)
        self.ui.pushButton_3.clicked.connect(self.send)
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Файл', 'Хэш'])
        self.con()
        self.upload()
    def con(self):
        self.con = psycopg2.connect(user="postgres",
                                     password="mash78",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="dlp")
        self.cur = self.con.cursor()
    def send(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Уведомление")
        self.msg.setText("Заявка на подключение отправлена")
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.exec_()
    def upload(self):
        self.cur.execute("SELECT name FROM secret_files")
        rows = self.cur.fetchall()
        i = 0
        self.ui.tableWidget.setRowCount(0)
        for elem in rows:
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            j = 0
            for t in elem:  # заполняем внутри строки
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        self.ui.tableWidget.resizeColumnsToContents()
    def select_files(self):
        filenames, _ = QFileDialog.getOpenFileNames(
            None,
            "Выбор защищаемых файлов")
        if filenames:
            for filename in filenames:
                shutil.copy(filename, "result")
                file_hash = hashlib.md5(open(filename, 'rb').read()).hexdigest()
                path = pathlib.Path(filename)
                timestamp = path.stat().st_mtime
                m_time = datetime.datetime.fromtimestamp(timestamp)
                current_timestamp = path.stat().st_ctime
                c_time = datetime.datetime.fromtimestamp(current_timestamp)
                print(filename,file_hash, c_time, m_time)
                self.cur.execute("INSERT into secret_files (name, path, date_use, date_edit,id_pc_secret_files) values ('" + filename + "', '" + file_hash + "', '" + str(c_time) + "', '" + str(m_time) + "','5')")
                print('2')
                self.con.commit()
        else:
            return
        self.upload()
        self.con.close() #повторное добавление только через выход и вход из за ограничения на подключения


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


    ##         pyuic5 interface.ui -o interface.py

    ##         pyrcc5 resources.qrc -o resources_rc.py
