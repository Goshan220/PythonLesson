from tkinter import *
from PythonGuiGOD import Ui_MainWindow
from PyQt5.QtWidgets import *
from Main import FamilyAccounting
import threading
import queue


class GUI(Ui_MainWindow):
    def __init__(self, form, file):
        super().__init__()
        self.setupUi(form)
        self.F = FamilyAccounting(file)
        self.qu = queue.Queue(5)
        self.thread()

        self.midUpButton.clicked.connect(self.show_all_coasts)
        self.midDownButton.clicked.connect(self.show_all_proceeds)
        self.rightUpButton.clicked.connect(self.pre_add_people)
        self.rightmidButton.clicked.connect(self.pre_add_entry)
        self.okButton.clicked.connect(self.add)
        self.comboBox.addItems(self.F.person)
        self.dateTimeEdit.setDisabled(True)

    def thread(self):
        th = threading.Thread(target=self.worker)
        th.setDaemon(True)
        th.start()

    def worker(self):
        while True:
            item = self.qu.get()
            self.output.setText(str(item))
            self.qu.task_done()

    def show_all_coasts(self):
        self.qu.put(self.F.expense_all_person())

    def show_all_proceeds(self):
        self.qu.put(self.F.add_money_all_person())

    def pre_add_people(self):
        self.dateTimeEdit.setDisabled(True)
        self.rightLine.setDisabled(False)
        self.okButton.setDisabled(False)

    def pre_add_entry(self):
        self.dateTimeEdit.setDisabled(False)
        self.rightLine.setDisabled(False)
        self.okButton.setDisabled(False)

    def add(self):
        if not self.dateTimeEdit.isEnabled():
            text = self.rightLine.text()
            self.qu.put(self.F.app_person(text))
            self.comboBox.addItem(text)
            print("done")
        else:
            data = self.dateTimeEdit.date()
            data = str(data)[19::]
            data = data[:-1:].split(",")
            for i in range(3):
                data[i] = data[i].lstrip()
            self.qu.put(self.F.change_date(int(data[2]), int(data[1]), int(data[0])))
            text = self.rightLine.text()
            text = str(text).lstrip()
            self.qu.put(self.F.add_operation_money(int(text), int(self.comboBox.currentIndex())))

        self.rightLine.setText("")
        self.rightLine.setDisabled(True)
        self.okButton.setDisabled(True)


def run():
    try:
        file = open('Datenbank.txt', 'r')
        app = QApplication(sys.argv)
        window = QMainWindow()
        GUI(window, file)
        window.show()
        sys.exit(app.exec_())
    finally:
        file.close()

run()
