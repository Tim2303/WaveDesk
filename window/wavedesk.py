from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from os import listdir

# Import inner modules
from core.files import ConfigManager
from core.audio import AudioManager

# Import settings images
import rc_icons

# Window subclass
class WDWindow(QWidget):
    def __init__(self):
        super(WDWindow, self).__init__()

        self.conf_manager = ConfigManager()
        # self.audio_manager = AudioManager()
        # self.load_audio()

        uic.loadUi("window.ui", self)
        self.setWindowTitle("WaveDesk")

        self.menu.mousePressEvent = lambda event: self.change_page(0)
        self.settings.mousePressEvent = lambda event: self.change_page(1)
        self.about.mousePressEvent = lambda event: self.change_page(2)

        self.change_page(0)

    def change_page(self, index):
        buttons = [self.menu, self.settings, self.about]
        self.stackedWidget.setCurrentIndex(index)

        # Reset styles for all buttons and set active button style
        for b in buttons:
            b.setStyleSheet("background-color: rgb(102, 0, 0); border-radius: 30px;")
        buttons[index].setStyleSheet("background-color: rgb(140, 0, 0); border-radius: 30px;")

    def load_audio(self):
        dirs = self.conf_manager.get("dirs_array")

        #TODO: rework this crutch
        device = (self.audio_manager.get_output_devices())[0]
        self.audio_manager.play_sound(dirs[0][0], device)

if __name__ == "__main__":
    app = QApplication([])
    window = WDWindow()
    window.show()
    app.exec()
