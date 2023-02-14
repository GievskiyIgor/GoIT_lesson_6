import shutil
import base64
from pathlib import *
import re
# from string import *
# import sys

# # 1
# Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.

# Приклад файлу:

# Alex Korp, 3000
# Nikita Borisenko, 2000
# Sitarama Raju, 1000
# Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

# Розробіть функцію total_salary(path)(параметр path - шлях до файлу), яка буде розбирати текстовий файл і
# повертати загальну суму заробітної плати всіх розробників компанії.

# Вимоги до завдання:

# функція total_salary повертає значення типу float
# для читання файлу функція total_salary використовує лише метод readline
# ми поки що не використовуємо менеджер контексту with

def total_salary(path):
    summ_ = 0
    fh = open(path +'test.txt', 'r')
    # fh = open(path, 'r')
    lines = fh.readlines()
    for il in lines:
        summ_ += float(re.findall(r'\d+', il)[0])

    fh.close()
    return summ_

path_ = 'E:\LessonsPython\GoIT_lesson_6\\'
print(total_salary(path_))
# ***

# 2
# У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:

# ['Robert Stivenson,28', 'Alex Denver,30']
# Це список рядків із прізвищем та віком співробітника, розділеними комами.

# Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.

# Функція запису в файл write_employees_to_file(employee_list, path), де:

# path – шлях до файлу.
# employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
# [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# Вимоги:

# запишіть вміст employee_list у файл, використовуючи режим "w".
# ми поки що не використовуємо менеджер контексту with
# кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19

def write_employees_to_file(employee_list, path):

    # fh.write('hello!') - запись в файл
    # fh = open(path +'test2.txt', 'w')
    fh = open(path, 'w')
    for il in employee_list:
        for i_ in il:
            fh.write(i_+'\n')

    fh.close()
    return fh

employee_list_ = [['Robert Stivenson,28','Alex Denver,30'], ['Drake Mikelsson,19']]
path_ = 'E:\LessonsPython\GoIT_lesson_6\\'
print(write_employees_to_file(employee_list_, path_))
# ***

# 3
# У попередній задачі ми записали співробітників у файл у такому вигляді:

# Robert Stivenson, 28
# Alex Denver, 30
# Drake Mikelsson, 19
# Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

# ['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
# Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при додаванні прочитаного рядка до списку.

# Вимоги:

# прочитайте вміст файлу за допомогою режиму "r".
# ми поки що не використовуємо менеджер контексту with
# поверніть із функції список співробітників із файлу


def read_employees_from_file(path):
    employee_list_ = []
    fh = open(path, 'r')

    while True:
        line = fh.readline()
        if not line:
            break
        employee_list_.append(re.sub('\\n', '', line))

    fh.close()
    return employee_list_

path_ = 'E:\LessonsPython\GoIT_lesson_6\\test2.txt'
print(read_employees_from_file(path_))
# ***

# 4
# Реалізуйте функцію add_employee_to_file(record, path), яка у файл(параметр path - шлях до файлу) буде додавати співробітника(параметр record)
# у вигляді рядка "Drake Mikelsson,19".

# Вимоги:

# параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
# кожен запис у файл має починатися з нового рядка.
# необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі з файлом відкрийте файл у режимі 'a',
# додайте співробітника record у файл і закрийте його
# ми поки що не використовуємо менеджер контексту with

def add_employee_to_file(record, path):

    fh = open(path, 'a+')
    fh.write((record_+'\n'))
    fh.close()
#     return employee_list_


record_ = input('>>>')
path_ = 'E:\LessonsPython\GoIT_lesson_6\\test3.txt'
print(add_employee_to_file(record_, path_))
# ***

# 5
# Ми маємо таку структуру файлу:

# 60b90c1c13067a15887e1ae1, Tayson, 3
# 60b90c2413067a15887e1ae2, Vika, 1
# 60b90c2e13067a15887e1ae3, Barsik, 2
# 60b90c3b13067a15887e1ae4, Simon, 12
# 60b90c4613067a15887e1ae5, Tessi, 5
# Кожен запис складається з трьох частин і починається з нового рядка. Наприклад, для першого запису початок 60b90c1c13067a15887e1ae1 —
# це первинний ключ бази даних MongoDB. Він завжди містить 12 байтів або рівно 24 символи. Далі ми бачимо прізвисько кота Tayson та його вік 3.
# Всі частини запису розділені символом кома,

# Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:

# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
# Параметри функції:

# path - шлях до файлу
# Вимоги:

# прочитайте вміст файлу за допомогою режиму "r".
# ми використовуємо менеджер контексту with
# поверніть із функції список котів із файлу у потрібному форматі

def get_cats_info(path):

    key_list = ['id', 'name', 'age']
    list_cat = []

    with open(path, 'r') as fh:
          while True:
            dict_cat = {}
            line = re.sub('\\n', '', fh.readline())
            line_ = re.split(',', line)
            if not line:
                break

            n= 0
            for li in line_:
                dict_cat[key_list[n]] = li.strip()
                n += 1

            list_cat.append(dict_cat)

    # fh.close()
    return list_cat

path_ = 'E:\LessonsPython\GoIT_lesson_6\\test3.txt'
print(get_cats_info(path_))
# ****

# 6
# Нагадаємо, що у 4 модулі ми для кулінарного блогу писали функцію format_ingredients, яка приймала на вхід список
# з інгредієнтами рецепта.

# Ми продовжимо працювати в цьому напрямку та створимо функцію, яка шукатиме рецепт у файлі та повертатиме знайдений рецепт
# у вигляді словника певної форми.

# У вас є файл, який містить рецепти у вигляді:

# 60b90c1c13067a15887e1ae1, Herbed Baked Salmon, 4 lemons, 1 large red onion, 2 tablespoons chopped fresh basil
# 60b90c2413067a15887e1ae2, Lemon Pancakes, 2 tablespoons baking powder, 1 cup vanilla-flavored almond milk, 1 lemon
# 60b90c2e13067a15887e1ae3, Chicken and Cold Noodles, 6 ounces dry Chinese noodles, 1 tablespoon sesame oil, 3 tablespoons soy sauce
# 60b90c3b13067a15887e1ae4, Watermelon Cucumber Salad, 1 large seedless watermelon, 12 leaves fresh mint, 1 cup crumbled feta cheese
# 60b90c4613067a15887e1ae5, State Fair Lemonade, 6 lemons, 1 cups white sugar, 5 cups cold water
# Кожен рецепт записаний з нового рядка(не забуваємо під час вирішення завдання про кінець рядка). Кожен запис починається
# з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, а потім через кому, йде перелік інгредієнтів рецепта.

# Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт у вигляді словника для кожної страви що шукається.
# Створіть функцію get_recipe(path, search_id), яка повертатиме словник для рецепта із зазначеним ідентифікатором MongoDB.

# Де параметри функції:

# path — шлях до файлу.
# search_id — первинний ключ MongoDB для пошуку рецепта
# Вимоги:

# Використовуйте менеджер контексту with для читання з файлу
# Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
# Приклад: для файлу, вказаного вище, виклик функції у вигляді

# get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
# Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4, Watermelon Cucumber Salad, 1 large seedless watermelon,
# 12 leaves fresh mint, 1 cup crumbled feta cheese і повернути результат у вигляді словника такої структури:

# {
#     "id": "60b90c3b13067a15887e1ae4",
#     "name": "Watermelon Cucumber Salad",
#     "ingredients": [
#         "1 large seedless watermelon",
#         "12 leaves fresh mint",
#         "1 cup crumbled feta cheese",
#     ],
# }

#  1 вариант
def get_recipe(path, search_id):

    key_list = ['id', 'name', 'ingredients']
    list_ingredients = []
    dict_recipe = {}

    with open(path, 'r') as fh:

        while True:
            line = re.sub('\\n', '', fh.readline())
            if not line:
                break

            if line.startswith(search_id):
                line_ = re.split(',', line)
                n = 0
                for li in line_:
                    if n <= 1:
                        dict_recipe[key_list[n]] = li.strip()
                        n += 1
                    else:
                        list_ingredients.append(li.strip())
                        dict_recipe[key_list[n]] = list_ingredients

        if len(dict_recipe) == 0:
            return None

    # fh.close()
    return dict_recipe

# 2 вариант от Владимира
# def get_recipe(path, search_id):
#     result = None
#     recipe_list = None

#     with open(path, 'r') as f:
#         recipe_list = f.readlines()

#     for recipe in recipe_list:
#         recipe = recipe.replace('\n', '').split(',')

#         if search_id in recipe:
#             result = {'id': recipe[0], 'name': recipe[1],
#                       'ingredients': recipe[2:]}
#     return result

search_id_ = "60b90c3b13067a15887e1ae4"
path_ = 'E:\LessonsPython\GoIT_lesson_6\\test6.txt'
print(get_recipe(path_, search_id_))
# ***

# 7
# Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.
# Вимоги:
# прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
# запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
# запис нового вмісту файлу output має бути одноразовий і використовувати метод write
def sanitize_file(source, output):

    with open(source, 'r') as fn:
        line = re.sub('[0-9]', '', fn.read())

    with open(output, 'w') as fh:
        fh.write(line)

source_ = 'E:\LessonsPython\GoIT_lesson_6\\test7_source.txt'
output_ = 'E:\LessonsPython\GoIT_lesson_6\\test7_output.txt'
print(sanitize_file(source_, output_))
# ***

# 8
# Задано відомість абітурієнтів, які склали вступні іспити до університету.
# Структура даних щодо абітурієнтів подана у вигляді наступного списку:

# [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]
# У кожному словнику цього списку записано прізвище абітурієнта — ключ name, код спеціальності, на яку він поступив — ключ specialty,
# та отримані ним бали з окремих дисциплін — ключі math(математика), lang(українська мова) та eng(англійська мова)

# Розробіть функцію save_applicant_data(source, output), яка буде вказаний список із параметра source зберігати у файл із параметра output

# Структура файлу для зберігання повинна бути наступною. У кожному новому рядку файлу повинні бути записані через кому без прогалин
# прізвище абітурієнта, код спеціальності, на яку він поступив, та отримані ним бали за окремими дисциплінами.

# Kovalchuk Oleksiy, 301, 175, 180, 155
# Ivanchuk Boryslav, 101, 135, 150, 165
# Karpenko Dmitro, 201, 155, 175, 185
# Вимоги:

# відкрийте файл output для запису, використовуючи менеджер контексту with та режим w.
# запис нового вмісту файлу output має бути або за допомогою методу writelines, або використовувати метод write

# 1 вариант
def save_applicant_data(source, output):
    line = ''
    lines =''
    for la in source:
        for val in la.values():
            line += str(val) + ','

        if line:
            lines += line[:-1] + '\n'
            line =''

    with open(output, 'w') as fh:
        fh.write(lines)

# 2 вариант от Vladyslav Zeleniak
# def save_applicant_data(source, output):

#     lines = ''
#     for la in source:
#         lines += f"{la['name']},{la['specialty']},{la['math']},{la['lang']},{la['eng']}\n"

#     with open(output, 'w') as fh:
#         fh.write(lines[:-1])

# 3 варинат от Vladyslav Zeleniak
# def save_applicant_data(source, output):

#     with open(output, 'a') as fh:
#         for s in source:
#             lines  = []
#             for val in s.values():
#                 lines.append(str(val))
#             fh.write(','.join(lines) + '\n')


source_ = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

output_ = 'E:\LessonsPython\GoIT_lesson_6\\test8_output.txt'
print(save_applicant_data(source_, output_))
# ***

# 9
# Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

# Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють собі,
# і False — якщо ні.

def is_equal_string(utf8_string, utf16_string):
    
    # utf8_string - закодирован в BYTES, utf8
    # utf16_string - закодирован в 16 системе,  utf16
    #  Сделаем декоде строке приведем в символы и сразу нормализуем с помощью метода casefold, который
    # зозвращает строку, где все симлолы в нижнем регистре и без необнознаностей, любой симлов имеет только одину
    # возможную форму записи

    strutf8 = utf8_string.decode().casefold()
    strutf16 = utf16_string.decode('utf-16').casefold()
    return True if strutf8 == strutf16 else False
# ***


# 10
# Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію,
# яка буде записувати логін та пароль користувача у файл.

# Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями
# в бінарний файл.

# Де:

# path – шлях до файлу.
# users_info - словник типу {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}, де ключ — логін(username) користувача,
# а значення — його пароль(password).
# Вимоги:

# Кожен рядок файлу повинен мати такий вигляд username: password. Такий формат запису використовують при Базовій
# аутентифікації.
# Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого
# рядка username: password для кожного елемента словника users_info

def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for key, val in users_info.items():
            lines = (f"{key}:{val}\n").encode()
            # lines = line.encode()
            fh.write(lines)

users_info_ = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
path_ = 'E:\LessonsPython\GoIT_lesson_6\\user_password.bin'
save_credentials_users(path_, users_info_)
# ***

# 11
# Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

# path – шлях до файлу.
# Формат файлу:

# andry: uyro18890D
# steve: oppjM13LL9e
# Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його з функції 
# get_credentials_users у наступному форматі:

# ['andry:uyro18890D', 'steve:oppjM13LL9e']
# Вимоги:

# Використовуйте менеджер контексту для читання з файлу
def get_credentials_users(path):
    with open(path, 'rb') as fh:
        list_get_user = []
        line = fh.readlines()
        for li in line:
            line = li.decode()
            list_get_user.append(line.replace('\n', ''))
    
    return list_get_user    
        

path_ = 'E:\LessonsPython\GoIT_lesson_6\\raw_data.bin'
print(get_credentials_users(path_))
# ****

# 12
# Функція get_credentials_users із попереднього завдання повертає нам список рядків username: password:

# ['andry:uyro18890D', 'steve:oppjM13LL9e']
# Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує кодування кожної 
# пари username: password у формат Base64 та повертає список із закодованими парами username: password у вигляді:

# ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
# import base64

def encode_data_to_base64(data):
    list_base64 = []
    for dt in data:
        list_ = dt.encode()
        list_ = base64.b64encode(list_)
        list_ = list_.decode()
        list_base64.append(list_)
    
    return list_base64

# # Функція encode_data_to_base64 працює невірно і повертає: [b'YW5kcnk6dXlybzE4ODkwRA==', b'c3RldmU6b3Bwak0xM0xMOWU='] Очікувався 
# # результат: ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU='] для списку[b'YW5kcnk6dXlybzE4ODkwRA==', b'c3RldmU6b3Bwak0xM0xMOWU=']
list_ =  ['andry:uyro18890D', 'steve:oppjM13LL9e']
print(encode_data_to_base64(list_))
# ***

#  13
# Щоб дізнатися, які формати підтримує пакет і які для них використовуються позначення, можна викликати функцію get_archive_formats.


# for shortcut, description in shutil.get_archive_formats():
#     print('{:<10} | {:<10}'.format(shortcut, description))
# --------------------------------------------------------------------
# Реалізуйте функцію create_archive(path, file_name, employee_residence)

# Де:

# path — шлях до файлу
# file_name — ім'я файлу
# employee_residence — словник, у якому ключ — ім'я користувача, а значення — країна проживання. 
# Вигляд: {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
#     Функція повинна працювати так:

#     Створювати бінарний файл file_name за шляхом path
#     Зберігати дані словника employee_residence у файл, де кожен новий рядок — це ключ значення через пробіл як "Michael Canada"
#     Архівувати теку по шляху path за допомогою shutil
#     Ім'я архіву має бути 'backup_folder.zip'
#     Функція має повернути рядок шляху до архіву 'backup_folder.zip'
#     Вимоги:

#     запишіть вміст словника employee_residence у бінарний файл з ім'ям file_name у теку path за допомогою оператора with .
#     використовуйте символ /, щоб розділити шлях для path та file_name
#     вигляд рядка файлу — Michael Canada, в кінці кожного рядка додається перенесення рядка '\n'.
#     при збереженні кожен рядок файлу кодується методом encode
#     при записі рядків використовуємо лише метод write
#     архів має бути у форматі zip з ім'ям 'backup_folder', створений за допомогою make_archive.

def create_backup(path, file_name, employee_residence):
    
    with open(path + '/' + file_name, 'wb') as fh:
        for key, val in employee_residence.items():
            line = f'{key} {val}\n'
            line = line.encode()
            fh.write(line)

    archive_name = shutil.make_archive('backup_folder', 'zip', path)

    return archive_name

# # Error
# # expected call not found. Expected: make_archive('backup_folder', 'zip', 'folder') Actual: make_archive('file.bin', 'zip', 'folder')
list_ = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
path_ = 'E:\LessonsPython\GoIT_lesson_6\\'
file_name_ = 'backup_folder'
print(create_backup(path_, file_name_, list_))
# ***

# 14
# Створіть функціонал для розпакування архіву.

# Зробіть import пакету shutil

# Створіть функцію unpack(archive_path, path_to_unpack), яка викликатиме метод пакета shutil unpack_archive та розпаковуватиме 
# архів archive_path у місце path_to_unpack.

# Функція нічого не повертає.

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, )

archive_path_  = 'Имя архива'
path_to_unpack_ = 'Путь к архиву'
unpack(archive_path_, path_to_unpack_)