from PyQt5.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys, os
def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
stylesheet = """
    QMainWindow {
        background-image: url(os.getcwd() + "/nzxt.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
print (os.getcwd() + "/nzxt.png")



# Your application won't reach here until you exit and the event
# loop has stopped.
print("You can now cloase the terminal, or run other commands.")

