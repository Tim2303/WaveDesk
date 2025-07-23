from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTabWidget,
    QWidget, QHBoxLayout, QVBoxLayout, QLabel
)


# Window subclass
class WDWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("WaveDesk Sound Pad")
        self.setMinimumSize(QSize(800, 600))

        # Main container widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Horizontal layout + content area
        main_layout = QHBoxLayout(main_widget)

        # Sidebar (vertical tabs)
        self.sidebar = QTabWidget()
        self.sidebar.setTabPosition(QTabWidget.TabPosition.West)
        self.sidebar.setMovable(False)
        self.sidebar.setMinimumWidth(150)
        self.sidebar.setMaximumWidth(200)

        # Create pages
        self.main_tab = self._create_main_tab()
        self.settings_tab = self._create_settings_tab()
        self.about_tab = self._create_about_tab()

        # Add tabs to sidebar
        self.sidebar.addTab(self.main_tab, "Main")
        self.sidebar.addTab(self.settings_tab, "Settings")
        self.sidebar.addTab(self.about_tab, "About")

        # Add widgets to layout
        main_layout.addWidget(self.sidebar)

    def _create_main_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(QLabel("This is the main soundboard tab."))
        return widget

    def _create_settings_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(QLabel("Settings go here."))
        return widget

    def _create_about_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(QLabel("WaveDesk - A custom Qt-based soundboard.\nCreated by TM2"))
        return widget


if __name__ == "__main__":
    app = QApplication([])
    window = WDWindow()
    window.show()
    app.exec()