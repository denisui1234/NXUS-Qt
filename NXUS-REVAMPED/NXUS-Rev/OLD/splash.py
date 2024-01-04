print("Working in: " + os.getcwd())
import time
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.Qt import QPixmap
import subprocess
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.setFixedSize(400, 200)
        self.label = QLabel(self)
        self.setWindowTitle("NXUS Is Starting...")

        self.pixmap = QPixmap("splash.png")
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.show


if __name__ == "__main__":
    import sys
    App = QApplication(sys.argv)
        # <---
    window = Window()
    sys.exit(App.exec())
time.sleep(4)
path = "NXUS-Rev"
os.chdir(path)
with open("nxus.py") as f:
    exec(f.read())
