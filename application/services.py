from .data_pack.data import directories, documents


def add_new_shelf(shelf_number):
    """
    Функция спросит номер новой полки и добавит ее в перечень.
    shelf_number: пользовательский ввод - номер новой полки.
    return: результат выполнения операции.
    """
    # print('Создаю новую полку\n')
    if str(shelf_number) not in directories:
        shelf_number = str(shelf_number)
        directories[shelf_number] = []
        return 'Полка успешно добавлена!'

    else:
        return 'Полка уже существует!'


def add_new_doc(shelf_number, type_doc='insurance', doc_number='12345', name='new_name'):
    """
    Функция, которая добавит новый документ в каталог и в перечень полок,
    спросив его номер, тип, имя владельца и номер полки, на которой он будет храниться.
    type_doc: пользовательский ввод - тип документа.
    doc_number: пользовательский ввод - номер документа.
    name: пользовательский ввод - имя владельца документа.
    shelf_number: пользовательский ввод - номер полки, для хранения документа.
    """
    if 1 <= int(shelf_number) <= len(directories):
        documents.append({'type': type_doc, 'number': doc_number, 'name': name})
        for key, value in directories.items():
            if str(shelf_number) in key:
                directories[key] = value + [doc_number]
                return 'Документ с номером успешно добавлен на полку!'
    else:
        return 'Такой полки не существует!'


def move_doc(doc_number='11-2', shelf_number=3):
    """
    Функция спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    doc_number: пользовательский ввод - номер документа.
    shelf_number: пользовательский ввод - номер полки, куда переместить документ.
    return: результат выполнения операции.
    """
    for document in directories.values():
        if doc_number in document:
            if 1 <= int(shelf_number) <= len(directories):
                document.remove(doc_number)
                for key, value in directories.items():
                    if str(shelf_number) in key:
                        directories[key] = value + [doc_number]
                        return 'Документ успешно перемещен!'
            else:
                return 'Такой полки не существует!'
    return 'Документа с таким номером в базе нет!'


def del_doc(doc_number='10006'):
    """
    Функция, спросит номер документа и удалит его из каталога и из перечня полок.
    doc_number: пользовательский ввод - номер документа.
    return: результат выполнения операции.
    """
    for value in directories.values():
        if doc_number in value:
            value.remove(doc_number)
    for document in documents:
        if document.get('number') == doc_number:
            documents.remove(document)
            return 'Документ успешно удален!'
    return 'Документа с таким номером в базе нет!'


def return_name(doc_number='11-2'):
    """
    Функция, по номеру документа, возвращает имя владельца.
    doc_number: пользовательский ввод - номер документа.
    return: имя владельца документа (если документ с таким номером есть в базе).
    """
    print('Поиск владельца по номеру документа.\n')
    for document in documents:
        if document.get('number') == doc_number:
            return 'Владелец документа с таким номером найден!'
    return 'Документа с таким номером в базе нет!'


def return_number_shelf(doc_number='2207 876234'):
    """
    Функция, по номеру документа, возвращает номер полки, на которой он находится.
    doc_number: пользовательский ввод - номер документа.
    return: номер полки на которой находится документ (если документ с таким номером есть в базе).
    """
    print('Поиск полки, на которой хранится документ.\n')
    for key, value in directories.items():
        if doc_number in value:
            return 'Документ с таким номером хранится на полке №'
    return 'Документа с таким номером в базе нет!'


def all_docs_in_base():
    """Функция выводит информацию по всем документам, имеющимся в базе."""
    print("Все документы имеющиеся в базе:\n")
    if len(documents) < 1:
        print('В базе нет документов!')
    for value in documents:
        print(f'{value["type"]} "{value["number"]}" "{value["name"]}"')
    print()


def show_commands():
    """Выводит список всех доступных команд"""
    commands = [
        'l – выведет список всех документов',
        'p – по номеру документа выведет имя человека, которому он принадлежит',
        's – по номеру документа выведет номер полки, на которой он находится',
        'as – добавит в перечень новую полку по номеру',
        'a – добавит новый документ в каталог и в перечень полок',
        'd – по номеру документа удалит его из каталога и из перечня попок',
        'm – по номеру документа и целевой полки переместит его с текущей полки на целевую',
        'q - для завершения сеанса'
    ]
    print("Cписок всех доступных команд: \n")
    print('\n'.join(commands), '\n')


def main():
    commands = {
        'h': show_commands,
        'p': lambda: print(return_name()),
        's': lambda: print(return_number_shelf()),
        'l': all_docs_in_base,
        'as': lambda: print(add_new_shelf(4)),
        'a': lambda: print(add_new_doc(3)),
        'd': lambda: print(del_doc()),
        'm': lambda: print(move_doc()),
        'q': 'Выход из программы',
    }

    print("Мое делопроизводство v1.0")
    print("Введите 'h' что бы получить список всех доступных команд\n")

    while True:
        command = input('Введите команду: ')
        if command in commands:
            if command == 'q':
                print('Сеанс завершен. Хорошего дня!')
                break
            else:
                commands[command]()
        else:
            print('Такой команды нет. Выберите из доступных.')
            print('Введите "h" что бы получить список всех доступных команд')
