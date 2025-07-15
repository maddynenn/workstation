from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QGroupBox
from open_types import *
import json
import os
import webbrowser

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
    
    from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QFrame, QGroupBox
from PyQt5.QtCore import Qt
from open_types import *
import json
import os
import webbrowser
import subprocess

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
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        main_layout.addWidget(QLabel("Workstation Group:"))
        self.input_group = QComboBox()
        self.input_group.addItems(self.get_group_display_names())
        main_layout.addWidget(self.input_group)
        
        main_layout.addWidget(QLabel("Title:"))
        self.input_box_title = QTextEdit()
        self.input_box_title.setFixedHeight(30)
        main_layout.addWidget(self.input_box_title)
        
        type_path_row = QHBoxLayout()
        
        type_col = QVBoxLayout()
        type_col.addWidget(QLabel("Type:"))
        self.input_type = QComboBox()
        self.input_type.addItems(TYPES)
        type_col.addWidget(self.input_type)
        type_col.addStretch()  # Push type dropdown to top
        
        path_col = QVBoxLayout()
        path_col.addWidget(QLabel("File Path:"))
        self.input_box_path = QTextEdit()
        path_col.addWidget(self.input_box_path)
        
        type_path_row.addLayout(type_col)
        type_path_row.addLayout(path_col)
        main_layout.addLayout(type_path_row)
        
        button_row = QHBoxLayout()
        self.submit = QPushButton("Submit")
        self.run_button = QPushButton("Run Group")
        button_row.addWidget(self.submit)
        button_row.addWidget(self.run_button)
        main_layout.addLayout(button_row)

        main_layout.addStretch()      
        self.setLayout(main_layout)

    def settings(self):
        self.setWindowTitle("Workstation")
        self.setGeometry(250, 250, 600, 600)

    def button_click(self):
        self.submit.clicked.connect(self.submit_path)
        self.run_button.clicked.connect(self.run_group)

    def submit_path(self):
        this_group = self.input_group.currentText()
        this_file_path = self.input_box_path.toPlainText()
        this_type = self.input_type.currentText()
        this_title = self.input_box_title.toPlainText()
        self.add_item_to_group(this_group, this_file_path, this_type, this_title)

    
    def add_item_to_group(self, group, file_path, type, title):
        if os.path.exists(file_path) or type == "browser tab":
            item = {"title": title, "type":type, "path": file_path}
            group_key = self.get_group_key_by_name(group)
            if group_key in self.data:
                self.data[group_key]["items"].append(item)
                self.save_data(self.data)

                self.input_box_path.clear()
                self.input_box_title.clear()
                return True
        else:
            alert = QMessageBox.warning(self, "Error", "File path does not exist")
        return False
    
        
    
    def get_group_key_by_name(self, display_name):
        for group_key, group_data in self.data.items():
            if group_data.get("name", group_key) == display_name:
                return group_key
        return None
            
    def start_workgroup(self, group):
        group_key = self.get_group_key_by_name(group)

        if group_key in self.data:
            for item in self.data[group_key]["items"]:
                if item.get("type") == "browser tab":
                   webbrowser.open(item.get("path")) 
                else:
                    os.startfile(item.get("path")) 
    
    def run_group(self):
        this_group = self.input_group.currentText()
        self.start_workgroup(this_group)

if __name__ == "__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()