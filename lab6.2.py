import random as r
import os
'''
10. Детский садик.
+++ Для вычисления платы за пребывание детей в детском саду утром воспитателями производится учёт поступающих детей.
+++ Собранные сведения о пришедших детях передаются заведующей садиком.
+++ На основании этих сведений формируется квитанция об оплате, которая передаётся родителям через воспитателей.
+++ После оплаты квитанция приносится воспитателям.
--- Если в течении 10 дней квитанция не оплачивается, то ребёнок в детский садик не принимается.
--- Сведения об отсутствующих детях передаются медицинской сестре.
--- Те дети, которые отсутствовали более 3 дней, принимаются в садик только при наличии медицинской справки о здоровье.
--- Сформировать коллекцию данных с информацией о посещаемости детьми детского сада.
'''


# C:\Users\insane_dude\Documents\GitHub\lab6_OP\6.2input


class Teachers:
    # Учителя заполняют списки присутствующих
    @staticmethod
    def getting_info_of_absence():
        position_now = 0
        way_to_directory_open = r'C:\Users\insane_dude\Documents\GitHub\lab6_OP\6.2input'
        # way_to_directory_open = str(input("Введіть шлях до папки, де ви хочете зчитати файли : "))
        files_in_dir_list = os.listdir(way_to_directory_open)
        os.chdir(way_to_directory_open)
        data_of_all_days = [[] for _ in range(len(files_in_dir_list))]
        for i in range(len(files_in_dir_list)):
            with open(files_in_dir_list[i], "r") as readedDayNow:
                for iRead in readedDayNow:
                    data_of_all_days[position_now].append(list(iRead.split()))
                print(data_of_all_days[position_now])
                position_now += 1
        return data_of_all_days

    # Воспитатели получают квитанцию от родителей и проверяют на наличие оплаты (1 - оплачено, 0 - нет)
    def getting_receipt_from_parents(self):
        self.from_parents_get_receipt = Parents.paying_receipt()
        for row in range(len(self.from_parents_get_receipt)):
            print(self.from_parents_get_receipt[row])
        f_array = [0]*10
        lines_with_zero = 0
        print("test to detect")
        for i in range(len(self.from_parents_get_receipt[0])):
            list_checker = []
            num_iter = 0
            for j in range(len(self.from_parents_get_receipt)):
                list_checker.append(self.from_parents_get_receipt[j][i])
                if f_array == list_checker[(0 + num_iter):(10 + num_iter)]:
                    num_iter += 1
                    print("zeros not found")
                    if num_iter is 5:
                        continue
                else:
                    print('found zeros')
                    lines_with_zero += 1
                    print(lines_with_zero)
                    return False
            print(list_checker)



class Director(Teachers):
    # Директор получает список
    def getting_list_of_absence(self):
        director_get_data_of_all_days = self.getting_info_of_absence()
        return director_get_data_of_all_days


class Parents(Director, Teachers):
    # Родители оплачивают квитанцию
    @staticmethod
    def paying_receipt():
        len_of_getting_info = len(Director.getting_info_of_absence())
        # receipt = [[r.randint(0, 1) for k in range(5)] for k in range(len_of_getting_info)]
        receipt = [[0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 1, 1, 0, 0],
                   [0, 1, 1, 0, 0],
                   [1, 0, 0, 0, 0],
                   [1, 1, 1, 0, 0],
                   [1, 1, 0, 0, 0],
                   [0, 1, 1, 0, 0],
                   [1, 1, 1, 0, 0],
                   [1, 1, 1, 0, 0],
                   [1, 1, 0, 0, 0],
                   [1, 1, 1, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0]]
        return receipt


class Nurse:
    pass


k = Parents()
k.getting_receipt_from_parents()
print("Кашевар К.С.")
print("Вариант 10")

