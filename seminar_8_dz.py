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

import os

# функция вывода данных
def show_data(data: list[str]):
    '''
    Функция выводит построчно элементы списка, добавляя в начало номер строки, начиная с 1
    '''
    for index, element in enumerate(data, 1):
        print(f'{index}) {element}', end="")

# функция чтения данных из файла
def read_data(file: str = 'file name'):
    '''
    Функция производит чтение данных из заданного файла.\n
    Обработка исключений проводится. (Если файл не найден - выведем сообщение о этом).\n
    Записывает полученные данные в список (элементы - строки из файла).\n
    Возвращает список.
    '''
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('\u001b[31mФайл  не найден. Необходимо создать новый контакт\n\u001b[0m')
        return []    

# функция записи данных в файл
def write_data(data: list[str], file: str):
    '''
    Функция записывает данные из списка (поэлементно) в указанный файл.
    '''
    with open(file, 'w', encoding='utf-8') as f:
        for element in data:
            f.write(element)

# функция записи нового контакта
def write_contact(file: str = 'file name'):
    '''
    Функция запрашивает ввод данных и записывает в указанный файл.
    '''
    print('Введите данные контакта:')
    first_name = input('  Введите фамилию: ')
    last_name = input('  Введите имя: ')
    patronymic = input('  Введите отчество: ')
    phone_number = input('  Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')
    print('\u001b[32mЗапись внесена\u001b[0m')

# функция поиска данных
def search_data(contacts: list[str]):
    '''
    Функция производит поиск введенных данных по элементам указанного списка. \n
    Приводит к нижнему регистру данные и запроса и элементов списка. \n
    Совпадающие с запросом элементы записывает в новый список.\n
    Возвращает список.
    '''
    search_str = input('Введите данные для поиска: ')
    founded = []
    for contact in contacts:
        if search_str.lower() in contact.lower():
            founded.append(contact)
    return founded

# функция выбора элемента
def select_entry(data: list[str]):
    '''
    Функция возвращает введенное пользователем число. \n
    Если введенное число больше, чем длина списка на входе - возвращает -1.
    '''
    entry = int(input('Введите номер записи, c которой будем работать: '))
    if entry > len(data):
        print('\u001b[31mТакого номера в этом списке нет\u001b[0m')
        return -1
    return entry

# функция редактирования данных
def edit_data(data: list[str], number_element: int):
    '''
    Функция редактирует список: \n
    - удаляет элемент списка по указанному индексу, \n
    - сохраняет введенные данные в элемент списка под тем же индексом. \n
    Возвращает обновленный список.
    '''
    data.pop(number_element - 1)
    print('Введите новые данные контакта:')
    first_name = input('  Введите фамилию: ')
    last_name = input('  Введите имя: ')
    patronymic = input('  Введите отчество: ')
    phone_number = input('  Введите номер телефона: ')
    update_element = (f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')  
    data.insert(number_element-1, update_element)
    print(f'Контакт {number_element}) обновлен.')
    return data

# функция удаления данных
def del_data(data: list[str], number_element: int):
    '''
    Функция удаляет элемент списка по указанному индексу. \n
    Возвращает обновленный список.
    '''
    print(f'Контакт {number_element}) удален.')
    data.pop(number_element - 1)
    return data

# функция копирования данных
def copy_data(data: list[str], number_element: int):
    '''
    Функция добавляет из указанного списка указанный элемент в файл, указанный пользователем. \n
    Если файл не существует - он будет создан.
    '''
    new_file = input('Введите имя файла, в который будем сохранять контакт: ')
    with open(new_file, 'a', encoding='utf-8') as f:
        f.write(data[number_element - 1])
    print(f'Контакт успешно добавлен в файл {new_file}')

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
            os.system('cls')
            print('Выбрано: \u001b[32mВыход из программы \u001b[0m')
            flag = False
        elif answer == '1':
            print('Выбрано: \u001b[32mПоказать все контакты \u001b[0m')
            data = read_data(file_name)
            show_data(data)
        elif answer == '2':
            print('Выбрано: \u001b[32mПоиск контакта \u001b[0m')
            data = read_data(file_name)
            founded_data = search_data(data)
            print('\u001b[32mПо Вашему запросу найдено: \u001b[0m')
            show_data(founded_data)
        elif answer == '3':
            print('Выбрано: \u001b[32mСохранить новый контакт \u001b[0m')
            write_contact(file_name)
        elif answer == '4':
            print('Выбрано: \u001b[32mРедактировать контакт \u001b[0m')
            data = read_data(file_name)
            show_data(data)
            number_element = select_entry(data)
            if number_element > 0:
                update_data = edit_data(data, number_element)
            write_data(update_data, file_name)
        elif answer == '5':
            print('Выбрано: \u001b[32mУдалить контакт \u001b[0m')
            data = read_data(file_name)
            show_data(data)
            number_element = select_entry(data)
            if number_element > 0:
                update_data = del_data(data, number_element)
            write_data(update_data, file_name)
        elif answer == '6':
            print('Выбрано: \u001b[32mСохранить контакт в новый файл \u001b[0m')
            data = read_data(file_name)
            show_data(data)
            number_element = select_entry(data)
            if number_element > 0:
                update_data = copy_data(data, number_element)
            #copy_data(data)

if __name__ == '__main__':
    main()




