from PyQt6 import uic
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget

# Import settings images
import rc_icons

# Window subclass
class WDWindow(QWidget):
    def __init__(self):
        super(WDWindow, self).__init__()

        self.setWindowTitle("WaveDesk Sound Pad")
        self.setMinimumSize(QSize(500, 700))

        uic.loadUi("window.ui", self)


if __name__ == "__main__":
    app = QApplication([])
    window = WDWindow()
    window.show()
    app.exec()
