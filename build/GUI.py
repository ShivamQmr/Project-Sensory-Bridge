import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from subprocess import Popen

class FileRunnerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Created buttons
        btn_run_file1 = QPushButton('Object Detection and Distance Estimation', self)
        btn_run_file2 = QPushButton('Detect ASL', self)

        # Connected buttons to functions
        btn_run_file1.clicked.connect(self.run_file1)
        btn_run_file2.clicked.connect(self.run_file2)

        # Created layout
        layout = QVBoxLayout()
        layout.addWidget(btn_run_file1)
        layout.addWidget(btn_run_file2)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Sensory Bridge Application')

        # Added some styling
        self.setStyleSheet("""
            FileRunnerApp {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                height: 40px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def run_file1(self):
        # File name in the quotation
        process = Popen(['python', './ObjectDetection-and-DistanceEstimation/DistanceEstimation.py'])

    def run_file2(self):
        # File name in the quotation to be run
        process = Popen(['python', './Sign-Language-Detection/Main.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileRunnerApp()
    ex.show()
    sys.exit(app.exec_())
