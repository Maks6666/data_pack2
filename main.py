# 2
# При старті програми з’являється меню з наступними
# пунктами:
# 1. Завантаження даних;
# 2. Збереження даних;
# 3. Додавання даних;
# 4. Видалення даних.
# Використайте список цілих як сховища даних. Також
# застосуйте стиснення/розпакування даних.

import pickle

class ListOfNumbers:
    def __init__(self, lst):
        self.lst = lst

    def print_info(self):
        print(f"The list is {self.lst}")

    def upload_data(self, data):
        with open("data.pickle", "wb") as file:
            pickle.dump(data, file)

    def add_data(self, data):
        with open("data.pickle", "wb") as file:
            num_of_values = int(input("How many numbers fo you want to append?: "))
            for i in range(num_of_values):
                num = int(input(f"Input number #{i+1}:"))
                data.append(num)
            pickle.dump(data, file)


    def del_data(self, data):
        with open("data.pickle", "wb") as file:
            num_of_values = int(input("How many numbers fo you want to delete?: "))
            for i in range(num_of_values):
                data.pop()
            pickle.dump(data, file)


    def output_data(self):
        with open("data.pickle", "rb") as file:
            read_person = pickle.load(file)
            return read_person



list_1 = [1, 2, 3, 4]
lst = ListOfNumbers(list_1)
lst.print_info()

lst.upload_data(list_1)
lst.add_data(list_1)
lst.del_data(list_1)
print(lst.output_data())








