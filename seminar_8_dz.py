# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# 	(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5. Реализовать функционал для изменения и удаления данных. Пользователь также может ввести имя или фамилию
# 6. Дополнить справочник возможностью копирования данных из одного файла в другой. 
#    Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# функция вывода данных
def show_data():
    pass

# функция чтения данных
def read_data(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('\u001b[31mФайл  не найден. Необходимо создать новый контакт\n\u001b[0m')
        return []    

# функция записи данных
def write_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

# функция поиска данных
def search_data():
    pass

# функция редактирования данных
def edit_data():
    pass

# функция удаления данных
def del_data():
    pass

# функция копирования данных
def copy_data():
    pass

# Код действий пользователя
def main():
    file_name = 'phone_book.txt'
    flag = True
    while flag:
        print()
        print('\u001b[32m 0 \u001b[0m - Выход из программы')
        print('\u001b[32m 1 \u001b[0m - Показать все контакты')
        print('\u001b[32m 2 \u001b[0m - Поиск контакта')
        print('\u001b[32m 3 \u001b[0m - Сохранить новый контакт')
        print('\u001b[32m 4 \u001b[0m - Редактировать контакт')
        print('\u001b[32m 5 \u001b[0m - Удалить контакт')
        print('\u001b[32m 6 \u001b[0m - Сохранить контакт в новый файл')
        print()
        answer = input('\u001b[4mВыберите необходимое действие:\u001b[0m ')
        if answer == '0':
            print('\u001b[32mВыход из программы \u001b[0m')
            flag = False
        elif answer == '1':
            print('\u001b[32mПоказать все контакты \u001b[0m')
            data = read_data(file_name)
            show_data(data)
        elif answer == '2':
            print('\u001b[32mПоиск контакта \u001b[0m')
            data = read_data(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '3':
            print('\u001b[32mСохранить новый контакт \u001b[0m')
            write_data(file_name)
        elif answer == '4':
            print('\u001b[32mРедактировать контакт \u001b[0m')
            data = read_data(file_name)
            edit_data(data)
        elif answer == '5':
            print('\u001b[32mУдалить контакт \u001b[0m')
            data = read_data(file_name)
            del_data(data)
        elif answer == '6':
            print('\u001b[32mСохранить контакт в новый файл \u001b[0m')
            data = read_data(file_name)
            copy_data(data)

if __name__ == '__main__':
    main()




