from tkinter import *
from PythonGuiGOD import Ui_MainWindow
from PyQt5.QtWidgets import *
from Main import Familienbuchhaltung
import threading
import queue

class GUI(Ui_MainWindow):
    def __init__(self, form):
        super().__init__()
        self.setupUi(form)
        self.F = Familienbuchhaltung()
        self.qu = queue.Queue(5)
        self.thread()

        self.midUpButton.clicked.connect(self.showAllCoasts)
        self.midDownButton.clicked.connect(self.showAllProceeds)
        self.rightUpButton.clicked.connect(self.PreAddPeople)
        self.rightmidButton.clicked.connect(self.PreAddEntry)
        self.okButton.clicked.connect(self.Add)
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

    def showAllCoasts(self):
        self.qu.put(self.F.Verbrauch_aller_Geld())

    def showAllProceeds(self):
        self.qu.put(self.F.Eintragung_aller_Geld())

    def PreAddPeople(self):
        self.dateTimeEdit.setDisabled(True)
        self.rightLine.setDisabled(False)
        self.okButton.setDisabled(False)

    def PreAddEntry(self):
        self.dateTimeEdit.setDisabled(False)
        self.rightLine.setDisabled(False)
        self.okButton.setDisabled(False)

    def Add(self):
        if (self.dateTimeEdit.isEnabled() == False):
            text = self.rightLine.text()
            self.qu.put(self.F.PersonHinzufügen(text))
            self.comboBox.addItem(text)
            print("done")
        else:
            data = self.dateTimeEdit.date()
            data = str(data)[19::]
            data = data[:-1:].split(",")
            for i in range(3):
                data[i] = data[i].lstrip()
            self.qu.put(self.F.ändernSiedasDatum(int(data[2]), int(data[1]), int(data[0])))
            text = self.rightLine.text()
            text = str(text).lstrip()
            self.qu.put(self.F.OperationMitDemGeld(int(text), int(self.comboBox.currentIndex())))


        self.rightLine.setText("")
        self.rightLine.setDisabled(True)
        self.okButton.setDisabled(True)

def run():
        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = GUI(window)
        window.show()
        sys.exit(app.exec_())

run()
