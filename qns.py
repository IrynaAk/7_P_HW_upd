import work1 as w1


def choice():
    while True:
        text = input('Выберите действие с запсью: 1 - просмотр, 2 - добавление, 3 - экспорт, 4 - импорт, 5 - выйти из программы: ')
        if text == '1':
            w1.view_data()
            print('Вывод записей закончен')
        elif text == '2':
            # w1.get_info()
            w1.write_data()
            print('\nДанные добавлены')
        elif text == '3':
            v = input('Выберите вариант выгрузки: 1 - выгрузка в столбик, 2 - выгрузка в строку: ')
            if v == '1':
                w1.export_data()
            elif v == '2':
                w1.export_with_commas()
            else:
                print('Введите верный вариант:')
            print('\nЭкспорт закончен. Проверьте файл "Export.csv"')
        elif text == '4':
            question = input('Сохраните файл в текущей папке !!!с именем "Import.txt"!!! Подтвердите сохранение (да/нет) ')
            if question == 'да':
                w1.import_data()
                print('\nИмпорт завершен.')
        elif text == '5':
            break
        else:
            print('Введена некорректная команда.')

choice()