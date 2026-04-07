from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel
from person import Person
from file_handler1 import *
import random
import sys


def uniqe_code_gen():
    new_code = int()
    while True:
        new_code = random.randint(1,999999)
        if not(code_in_set(new_code)):
            add_code_to_set(new_code)
            break
    str_code = "%06d"%new_code
    return str_code

class MainWindow(QMainWindow):
        
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,350)
        
        self.data_label = QLabel(self)
        self.data_label.setText("Data Input")
        self.data_label.move(90,20)
        
        self.search_label = QLabel(self)
        self.search_label.setText("Data Search:")
        self.search_label.move(220,20)
        self.search_input = QLineEdit(self)
        self.search_input.move(320,20)
        
        self.name_label = QLabel(self)
        self.name_label.setText("Name")
        self.name_label.move(20,50)
        self.name_input = QLineEdit(self)
        self.name_input.move(90,50)
        
        self.surname_label = QLabel(self)
        self.surname_label.setText("Surname")
        self.surname_label.move(20,80)
        self.surname_input = QLineEdit(self)
        self.surname_input.move(90,80)

        self.city_label = QLabel(self)
        self.city_label.setText("City")
        self.city_label.move(20,110)
        self.city_input = QLineEdit(self)
        self.city_input.move(90,110)
        
        self.number_label = QLabel(self)
        self.number_label.setText("Number")
        self.number_label.move(20,140)
        self.number_input = QLineEdit(self)
        self.number_input.move(90,140)
        
        self.search_button = QPushButton(self, text = "search")
        self.search_button.move(320,60)
        self.search_button.clicked.connect(self.retrieve_data)

        self.add_button = QPushButton(self, text = "add")
        self.add_button.move(90,170)
        self.add_button.clicked.connect(self.add_data_to_list)
        
        self.clear_button = QPushButton(self, text = "clear")
        self.clear_button.move(90,230)
        self.clear_button.clicked.connect(self.clear_data)
        
        self.save_button = QPushButton(self, text = "save")
        self.save_button.move(90,200)
        self.save_button.clicked.connect(self.save_data)

    def retrieve_data(self):
        data_dict = retrieve_data_by_code(self.search_input.text())
        self.name_input.setText(data_dict["Name"])
        self.surname_input.setText(data_dict["Surname"])
        self.city_input.setText(data_dict["City"])
        self.number_input.setText(data_dict["Number"])
                    
    def add_data_to_list(self):
        person = Person(self.name_input.text(),
                        self.surname_input.text(),
                        self.city_input.text(),
                        self.number_input.text())
        
        
        unique_code = uniqe_code_gen()
        person.get_unique_code(unique_code)
        new_person_dict = dict()
        new_person_dict["Name"] = person.name
        new_person_dict["Surname"] = person.surname
        new_person_dict["City"] = person.city
        new_person_dict["Number"] = person.number
        new_person_dict["Code"] = person.new_code
        add_new_data(new_person_dict)
        self.name_input.setText("")
        self.surname_input.setText("")
        self.city_input.setText("")
        self.number_input.setText("")
        
    def save_data(self):
        empty_list()
        save_new_data()
        save_code_set()
        
    def clear_data(self):
        self.name_input.setText("")
        self.surname_input.setText("")
        self.city_input.setText("")
        self.number_input.setText("")
        self.search_input.setText("")
        
        
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

window.show()
sys.exit(app.exec())