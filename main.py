# 2
# Маємо певний словник з логінами і паролями користувачів. Логін використовується як ключ, пароль —
# як значення. Реалізуйте: додавання, видалення, пошук,
# редагування, збереження та завантаження даних (використовуючи стиснення та розпакування)..

import pickle
import gzip
class ListOfNumbers:
    def __init__(self, dict):
        self.dict = dict

    def print_info(self):
        print(f"The dictionary is {self.dict}")

    def upload_data(self, data):
        with gzip.open("data.gz", "wb") as file:
            serialized_data = pickle.dumps(data)
            file.write(serialized_data)

    def add_data(self):
        num_of_values = int(input("How many values do you want to append?: "))
        for i in range(num_of_values):
            key = input(f"Input key #{i+1}: ")
            value = input(f"Input value for key '{key}': ")
            self.dict[key] = value
        self.upload_data(self.dict)


    def del_data(self):
        with open("data.pickle", "wb") as file:
            num_of_values = int(input("How many values fo you want to delete?: "))
            for i in range(num_of_values):
                key = input(f"Input key #{i + 1} to delete: ")
                del self.dict[key]
            self.upload_data(self.dict)


    def output_data(self):
        with gzip.open("data.gz", "rb") as file:
            read_person = pickle.load(file)
            return read_person



dict_1 = {"login_1": "password_1", "login_2": "password_2"}
dict = ListOfNumbers(dict_1)
dict.print_info()

dict.del_data()
dict.print_info()
dict.del_data()
dict.print_info()





