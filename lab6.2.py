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

'''
KEKW +
BlessRNG +
Kappa -
LUL +
SMOrc -
'''


class Teachers:
    # Учителя заполняют списки присутствующих
    @staticmethod
    def getting_info_of_absence():
        position_now = 0
        way_to_directory_open = str(input("Введіть шлях до папки, де ви хочете зчитати файли : "))
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

    # Воспитатели получают квитанцию от родителей
    @staticmethod
    def getting_receipt_from_parents():
        parents_get_receipt = Parents.paying_receipt()
        print(parents_get_receipt)


class Director(Teachers):
    # Директор получает список
    @staticmethod
    def getting_list_of_absence():
        director_get_data_of_all_days = Teachers.getting_info_of_absence()
        return director_get_data_of_all_days


class Parents(Director, Teachers):
    # Родители оплачивают квитанцию
    @staticmethod
    def paying_receipt():
        receipt = [[r.randint(0, 1) for k in range(len(Director.getting_list_of_absence()))]
                   for l in range(len(Director.getting_list_of_absence()))]
        for row in range(len(receipt)):
            print(receipt[row])
        return receipt


class Nurse:
    pass


k = Parents()
