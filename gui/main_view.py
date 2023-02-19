import sys
from PyQt5.QtWidgets import QApplication, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit, \
    QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QAction
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QActionEvent


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Expenses Tool")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        #Exit QAction
        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl + Q")
        self.exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(self.exit_action)

    @pyqtSlot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":

    # Qt Application
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec())    
