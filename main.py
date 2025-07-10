from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from open_types import *
import json

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.button_click()
    
    def initUI(self):
        self.input_box_path = QTextEdit()
        self.submit = QPushButton("Submit")
        self.input_type = QComboBox()
        self.input_box_title = QTextEdit()
        self.input_box_title.setFixedHeight(30)

        self.input_type.addItems(TYPES)

        self.master = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()
        col3 = QVBoxLayout()

        col1.setSpacing(5)
        col2.setSpacing(5)
        col3.setSpacing(5)

        # Add widgets to columns
        col1.addWidget(QLabel("File Path:"))  # Add labels
        col1.addWidget(self.input_box_path)
        
        col2.addWidget(QLabel("Type:"))
        col2.addWidget(self.input_type)
        
        col3.addWidget(QLabel("Title:"))
        col3.addWidget(self.input_box_title)
        col3.addWidget(self.submit)
        
        # Add stretch to push everything to top
        col1.addStretch()
        col2.addStretch()
        col3.addStretch()
        
        # Add columns to master layout with equal proportions
        self.master.addLayout(col1, 1)
        self.master.addLayout(col2, 1)
        self.master.addLayout(col3, 1)
        
        self.setLayout(self.master)

    def settings(self):
        self.setWindowTitle("Workstation")
        self.setGeometry(250, 250, 600, 600)

    def button_click(self):
        self.submit.clicked.connect(self.submit_path)

    def submit_path(self):
        this_file_path = self.input_box_path.toPlainText()
        this_type = self.input_type.currentText()
        this_title = self.input_box_title.toPlainText()
        print(f'you just sumbitted an entry of type: {this_type} with the title {this_title} which can be found at {this_file_path}')

if __name__ == "__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()