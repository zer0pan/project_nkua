class Person:
    def __init__(self,_name,_surname,_city,_number):
        self.name = _name
        self.surname = _surname
        self.city = _city
        self.number = _number
        
    def get_unique_code(self, code):
        self.new_code =  code