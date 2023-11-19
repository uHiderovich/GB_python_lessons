'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''

from csv import DictReader, DictWriter
from os.path import exists

base_file_name = 'phones.csv'


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_valid_phone():
    phone_number = 0
    is_valid = False

    while not is_valid:
        try:
            phone_number = int(input('Введите номер: '))
            # phone_number = 99999999999
            if len(str(phone_number)) != 11:
                raise LenNumberError('Не верная длина номера!')
            else:
                is_valid = True
        except ValueError:
            print('Не валидный номер!')
        except LenNumberError as err:
            print(err)
            continue

    return phone_number


def get_valid_name(name_type):
    name = ''
    is_valid = False

    while not is_valid:
        name = input(f'Введите {name_type}: ')

        if len(name) == 0:
            print(f'Вы не ввели {name_type}!')
        else:
            is_valid = True

    return name


def get_person_info():
    first_name = get_valid_name('имя')
    last_name = get_valid_name('фамилию')
    phone_number = get_valid_phone()

    return {'Имя': first_name, 'Фамилия': last_name, 'Телефон': phone_number}


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, person_info):
    res = read_file(file_name)

    for el in res:
        if el['Телефон'] == str(person_info['Телефон']):
            print('Такой номер телефона уже есть в справочнике!')
            return

    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        res.append(person_info)
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def print_file(file_name):
    for line in read_file(file_name):
        print(line, end='\n')


def copy_line(file_name):
    line = int(input('Введите номер строки для копирования: '))

    lines_of_file = read_file(file_name)

    if len(lines_of_file) < line:
        print(f'Строки под номером {line} в файле {file_name} не существует!')
        return

    line_for_copy = lines_of_file[line - 1]

    new_file_name = input('Введите название файла в который нужно скопировать строку: ')

    if check_file_exists(new_file_name):
        write_file(new_file_name, line_for_copy)


def check_file_exists(file_name):
    is_exists = exists(file_name)

    if not is_exists:
        print(f'Файла c именем {file_name} не существует!')

    return is_exists


def main():
    while True:
        command = input('Введите команду: ')

        if command == 'q':
            break
        elif command == 'w':
            if not check_file_exists(base_file_name):
                create_file(base_file_name)
            write_file(base_file_name, get_person_info())
        elif command == 'r':
            if check_file_exists(base_file_name):
                print_file(base_file_name)
        elif command == 'c':
            if check_file_exists(base_file_name):
                copy_line(base_file_name)
        else:
            print('Такой команды не существует!')


main()
