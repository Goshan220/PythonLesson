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

        self.midUpButton.clicked.connect(self.showAll)
        self.midDownButton.clicked.connect(self.showAll2)

    def showAll(self):
        self.qu.put(self.F.Verbrauch_aller_Geld())

    def showAll2(self):
        self.qu.put(self.F.Eintragung_aller_Geld())

    def thread(self):
        th = threading.Thread(target=self.worker)
        th.setDaemon(True)
        th.start()

    def worker(self):
        while True:
            item = self.qu.get()
            self.output.setText(str(item))
            self.qu.task_done()


def run():
        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = GUI(window)
        window.show()
        sys.exit(app.exec_())

run()
