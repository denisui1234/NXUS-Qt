import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NCalc")
        self.setWindowIcon(QIcon("NCalc.png"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)

        buttons = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            '0', '.', '=', '/',
            'C'
        ]

        grid_layout = QVBoxLayout()

        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.button_click)
            grid_layout.addWidget(btn)

        self.layout.addLayout(grid_layout)

    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.line_edit.text())
                self.line_edit.setText(str(result))
            except:
                self.line_edit.setText("Error")

        elif text == 'C':
            self.line_edit.clear()

        else:
            current_text = self.line_edit.text()
            self.line_edit.setText(current_text + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
