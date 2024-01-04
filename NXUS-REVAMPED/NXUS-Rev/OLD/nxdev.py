import os, sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, QPushButton, QLabel, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hiding Side Panel')
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)

        # Toggle button to show/hide panel
        toggle_button = QPushButton('>', self)
        toggle_button.setFixedWidth(10)
        toggle_button.clicked.connect(self.togglePanel)
        main_layout.addWidget(toggle_button)

        # Side panel
        self.side_panel = QWidget(self)
        self.side_panel.setFixedWidth(250)
        self.side_panel_layout = QVBoxLayout(self.side_panel)

        # Scroll area to display .py files
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        self.py_list_widget = QListWidget(self)
        self.populatePyFiles()

        scroll_area.setWidget(self.py_list_widget)
        self.side_panel_layout.addWidget(scroll_area)

        main_layout.addWidget(self.side_panel)

        # Connect the item clicked signal to a handler
        self.py_list_widget.itemClicked.connect(self.runPyFile)

    def populatePyFiles(self):
        app_folder = "apps"
        py_files = [file for file in os.listdir(app_folder) if file.endswith(".py")]

        for py_file in py_files:
            item = QListWidgetItem(self.py_list_widget)
            item.setText(py_file)

            # Add icon (using a generic Python icon for demonstration)
            icon_path = os.path.join(app_folder, f"{os.path.splitext(py_file)[0]}.png")
            if os.path.exists(icon_path):
                icon = QLabel()
                icon.setPixmap(QPixmap(icon_path))
                item.setSizeHint(icon.sizeHint() + QSize(0, 10))
                self.py_list_widget.setItemWidget(item, icon)

    def togglePanel(self):
        # Toggle the visibility of the side panel
        if self.side_panel.isVisible():
            self.side_panel.hide()
        else:
            self.side_panel.show()

    def runPyFile(self, item):
        # Get the selected .py file
        selected_file = item.text()

        # Construct the full path to the selected .py file
        file_path = os.path.join("apps", selected_file)

        # Run the .py file using subprocess
        subprocess.Popen(["python3", file_path])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
