# 1
# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.

import pickle

class ListToAppend:
    def __init__(self, lst):
        self.lst = lst

    def length(self):
        self.length_list = int(input("Input length of list: "))
        for i in range(self.length_list):
            num = int(input(f"Input number #{i+1}: "))
            self.lst.append(num)
        return self.lst


    def save_data(self, data):
        self.data = data
        with open("data.pickle", "wb") as file:
            pickle.dump(data, file)
        return "Data saved."

    def read_data(self, data):
        with open("data.pickle", "rb") as file:
            read_data = pickle.load(file)
        return read_data

list_1 = []

lst = ListToAppend(list_1)
lst.length()
print(lst.save_data(list_1))
print(f"Saved data: {lst.read_data(list_1)}")




