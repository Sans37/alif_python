class ProductFoods:
    name_file = None
    action_number = None

    def __init__(self, name_file, action_number):
        self.name_file = name_file
        self.action_number = action_number


    # Метод работы с действиями    
    def actions(self): 
        if self.action_number == 1:
            self.add_list_foods()

        elif self.action_number == 2:
            self.change_list_foods()

        elif self.action_number == 3:
            self.delete_list_foods()

        elif self.action_number == 4:
            self.summa_costs_foods()

    # Метод добавить запись в списке        
    def add_list_foods(self):
        with open(self.name_file, 'a', encoding='cp1251') as File:
            line = str(input("Добавте продукты в список: "))
            line += '\n'
            File.write(line)

    # Метод изменить запись в списке
    def change_list_foods(self):
        with open(self.name_file, 'r', encoding='cp1251') as File:
            olf_file = File.read()
        old_line = str(input("Введите исходный продкут: "))
        new_line = str(input("Введите новый продукт: "))
        new_file = olf_file.replace(old_line, new_line)
        with open(self.name_file, 'w', encoding='cp1251') as File:
            File.write(new_file)

    # Метод удалить запись из списка
    def delete_list_foods(self):
        with open(self.name_file, 'r', encoding='cp1251') as File:
            old_file = File.read()
        delete_line = str(input("Введите из списка продукты: "))
        new_file = old_file.replace(delete_line, "")
        with open(self.name_file, 'w', encoding='cp1251') as File:
            File.write(new_file)

    # Метод вычислить сумму общей цены из списка
    def summa_costs_foods(self):
        with open(self.name_file, 'r', encoding='cp1251') as File:
            costs = [line.strip().split('-')[1] for line in File]
        summa_costs = 0
        for i in range(len(costs)):
            summa_costs += int(costs[i])

        print("Общая цена продутков:", summa_costs)


# Метод меню
def print_menu():
    print("[______________Menu______________]")
    print("[ (1)  Добавить в список         ]")
    print("[ (2)  Изменить запись в списке  ]")
    print("[ (3)  Удалить из списка         ]")
    print("[ (4)  Вычесть общую сумму       ]")
    print("[ (0)  Выход из программы        ]")


# Метод ввода данных
def input_data():
    print()
    name_file = str(input("Создайте или откройте файл со списком продкутами: "))
    action_number = int(input("Выберите номер действии: "))
    return name_file, action_number

def finished():
    print("Программа завершена!")

# Главный метод
def main():
    flag = True
    while flag:
        print_menu()
        name_file, action_number = input_data()
        product = ProductFoods(name_file, action_number)
        product.actions()
        if action_number == 0:
            input_1 = input("Вы действительно хотите завершить программу? [y/n]\n")
            if input_1 == 'y':
                finished()
                flag = False
        if action_number != 0:
            input_2 = input("Вы хотите продолжить программу? [y/n]\n")
            if input_2 == 'n':
                finished()
                flag = False


if __name__ == '__main__':
    main()