from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from open_types import *
import json
import os

class Home(QWidget):
    def __init__(self, file_path="app_data.json"):
        super().__init__()

        self.file_path = file_path
        self.data = self.load_or_create_data()

        self.settings()
        self.initUI()
        self.button_click()

    def load_or_create_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error reading file {e}")
                return self.create_default_data()
        else:
            default_data = self.create_default_data()
            self.save_data(default_data)
            return default_data

    def create_default_data(self):
        return {
            "work_group": {
                "name": "Work Setup",
                "items": []
            },
            "personal_group": {
                "name": "Personal Setup",
                "items": []
            }
        }

    def save_data(self, data=None):
        if data is None:
            data = self.data
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=2)
            return True
        except IOError as e:
            print(f"Error saving file: {e}")
            return False
    
    def get_group_display_names(self):
        return [group_data.get("name", group_key) for group_key, group_data in self.data.items()]
    
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