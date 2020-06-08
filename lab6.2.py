import random as r
import os
'''
10. Детский садик.
1) +++ Для вычисления платы за пребывание детей в детском саду утром воспитателями производится учёт поступающих детей.
2) +++ Собранные сведения о пришедших детях передаются заведующей садиком.
3) +++ На основании этих сведений формируется квитанция об оплате, которая передаётся родителям через воспитателей.
4) +++ После оплаты квитанция приносится воспитателям.
5) +++ Если в течении 10 дней квитанция не оплачивается, то ребёнок в детский садик не принимается.
6) +++ Сведения об отсутствующих детях передаются медицинской сестре.
7) --- Те дети, которые отсутствовали более 3 дней, принимаются в садик только при наличии медицинской справки о здоровье.
8) --- Сформировать коллекцию данных с информацией о посещаемости детьми детского сада.
'''


# C:\Users\insane_dude\Documents\GitHub\lab6_OP\6.2input


class Teachers:
    # 1) Учителя заполняют списки присутствующих
    @staticmethod
    def getting_info_of_absence():
        position_now = 0
        way_to_directory_open = r'C:\Users\insane_dude\Documents\GitHub\lab6_OP\6.2input'
        files_in_dir_list = os.listdir(way_to_directory_open)
        os.chdir(way_to_directory_open)
        data_of_all_days = [[] for _ in range(len(files_in_dir_list))]
        for i in range(len(files_in_dir_list)):
            with open(files_in_dir_list[i], "r") as readedDayNow:
                for iRead in readedDayNow:
                    data_of_all_days[position_now].append(list(iRead.split()))
                position_now += 1
        return data_of_all_days

    # Вивід
    def output_show(self):
        print(Teachers.getting_info_of_absence())

    # 4, 5) Воспитатели получают квитанцию от родителей и проверяют на наличие оплаты (1 - оплачено, 0 - нет)
    def getting_receipt_from_parents(self):
        self.from_parents_get_receipt = Parents.paying_receipt()
        # for row in range(len(self.from_parents_get_receipt)):
        #     print(self.from_parents_get_receipt[row])
        f_array = [0]*10
        print('f_array', f_array)
        lines_with_zero = 0
        for i in range(len(self.from_parents_get_receipt[0])):
            list_checker = []
            num_iter = 0
            for j in range(len(self.from_parents_get_receipt)):
                list_checker.append(self.from_parents_get_receipt[j][i])
            # print(list_checker)
            for test in range(len(list_checker)//2):
                checking_for_paid_receipt = list_checker[(0 + num_iter):(10 + num_iter)]
                reserve_to_check = [k for k in range(0 + num_iter, 10 + num_iter)]
                # print('reserve_to_check', reserve_to_check)
                num_iter += 1
                if checking_for_paid_receipt == f_array:
                    lines_with_zero += 1
                    print("found zeros :", lines_with_zero)
                    break
        return lines_with_zero

    def updating_list_of_absense(self):
        if self.getting_receipt_from_parents() is 0:
            print("Нічого не відбувається")
        else:
            updated_list = Director.getting_info_of_absence()
            number_to_redact = 3
            while number_to_redact != len(updated_list)-3:
                updated_list[number_to_redact][4][1] = '-'
                number_to_redact += 1
            print("Апдейт списка")
            for row in range(len(updated_list)):
                print(updated_list[row])
            return updated_list


class Director(Teachers):
    # 2) Директор получает список
    def getting_list_of_absence(self):
        director_get_data_of_all_days = self.getting_info_of_absence()
        return director_get_data_of_all_days


class Parents(Director):
    # 3) Родители оплачивают квитанцию
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
                   [1, 1, 1, 1, 0],
                   [1, 1, 0, 0, 0],
                   [0, 1, 1, 0, 0],
                   [1, 1, 1, 0, 0],
                   [1, 1, 1, 0, 0],
                   [1, 1, 0, 0, 0],
                   [1, 1, 1, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0]]
        return receipt


class Nurse(Parents):
    # 6) Медсестра получает список отсутствующих
    def getting_info_of_n_absence(self):
        nurse_getting_info_of_absense = Teachers.updating_list_of_absense(self)
        print("detect")
        for deleting in range(len(nurse_getting_info_of_absense)):
            if '+' in nurse_getting_info_of_absense[deleting][0][1]:
                nurse_getting_info_of_absense[0:][0:][1].pop()
            if IndexError:
                print("Медсестра отримала дані")
                break


k = Nurse()
# k.getting_receipt_from_parents()
k.updating_list_of_absense()
k.getting_info_of_n_absence()
print("ИП-96, Кашевар К.С.")
print("Вариант 10")

