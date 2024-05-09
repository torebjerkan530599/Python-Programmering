class Employee:
    def __init__(self, name, id_number, department, title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__title = title

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title
    
    def get_name(self):
        return self.__name
        
    def get_id_number(self):
        return self.__id_number
        
    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

    def __str__(self):
        result = 'Name: ' + self.get_name() + \
                 ' ID number: ' + self.get_id_number() + \
                 ' Department: ' + self.get_department() + \
                 ' Title: ' + self.get_title()
        return result

