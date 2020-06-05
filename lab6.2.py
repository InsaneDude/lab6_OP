'''
10. Детский садик.
Для вычисления платы за пребывание детей в детском саду утром воспитателями производится учёт поступающих детей.
Собранные сведения о пришедших детях передаются заведующей садиком;
на основании этих сведений формируется квитанция об оплате (за месяц),
которая передаётся родителям через воспитателей. После оплаты квитанция приносится воспитателям.
Если в течении 10 дней квитанция не оплачивается, то ребёнок в детский садик не принимается.
Сведения об отсутствующих детях передаются медицинской сестре. Те дети, которые отсутствовали более 3 дней,
принимаются в садик только при наличии медицинской справки о здоровье.
Сформировать коллекцию данных с информацией о посещаемости детьми детского сада.
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
    @staticmethod
    def getting_info_of_absence():
        import os
        position_now = 0
        way_to_directory_open = str(input("Введіть шлях до папки, де ви хочете зчитати файли : "))
        files_in_dir_list = os.listdir(way_to_directory_open)
        os.chdir(way_to_directory_open)
        data_of_all_days = [[] for k in range(len(files_in_dir_list))]
        for i in range(len(files_in_dir_list)):
            with open(files_in_dir_list[i], "r") as readedDayNow:
                for iRead in readedDayNow:
                    data_of_all_days[position_now].append(list(iRead.split()))
                print(data_of_all_days[position_now])
                position_now += 1
        return data_of_all_days


class Director(Teachers):
    pass


class Parents:
    pass


class Nurse:
    pass


b = Teachers()
b.getting_info_of_absence()