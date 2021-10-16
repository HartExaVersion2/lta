from common.constant import COMMANDS, FOCUS
from common.errors import *
from merger.add_file.add_file_in_english import AddFileInEnglish
from merger.add_file.add_file_in_russian import AddFileInRussian
from merger.translate.translate_file import TranslateFile
from merger.transfer.transfer_file import TransferFile
from merger.streamline.streamline_file import StreamlineFile
from merger.general.general_work_with_directory import GeneralWorkWithDirectory
from merger.search_untrans_string.search_untrans_string import SearchUntransString
from merger.search_update_string.search_update_string import SearchUpdateString
from visual_interfaces.work_with_interface import WorkWIthInterface
from translator_helper.translator_helper import TranslatorHealper

def __check_input(general_path):
    if not general_path:
        raise NotEnterPath
    if '.yml' not in general_path and '.txt' not in general_path:
        raise PathNotLeadToFile

def __check_input_two_path(general_path, add_path):
    if general_path == add_path:
        raise PathMatch
    __check_input(general_path)
    __check_input(add_path)

def __check_input_three_path(general_path, add_path, other_path):
    if general_path in (add_path, other_path) or add_path in (general_path, other_path) or other_path in (general_path, add_path):
        raise PathMatch
    __check_input(general_path)
    __check_input(add_path)
    __check_input(other_path)

def __translator(interface, general_file_path, additional_file_path, helper=True):
    interface.Close()
    interface = work_with_interface.change_interfase(mode=COMMANDS.WHITH_HEALPER, extra_options=['тут будет оригинальное название фокуса',
                                                                                                 'тут будет оригинальное описание фокуса',
                                                                                                 'тут будет переведённое название фокуса',
                                                                                                 'тут будет переведённое описание фокуса'])
    translator_healper = TranslatorHealper(path_general_file='/home/mitry/переводы/lta/test/focus_BEX_l_english.yml', add_path='/home/mitry/переводы/lta/test/focus_BEX_l_russian.yml')#path_general_file=general_file_path, add_path=additional_file_path #ToDo не забыть убрать
    while True:
        event, values = interface.read()
        if event in (None, 'Exit', 'Cancel', 'Назад'):
            translator_healper.save()
            break
        elif event == 'Сохранить':
            translator_healper.save()
        elif event == 'Далее':
            translator_healper.save()
            next_focus = translator_healper.further(values['title'], values['desc'])
            interface.Close()
            interface = work_with_interface.change_interfase(mode=COMMANDS.WHITH_HEALPER,
                                                             extra_options=[next_focus[FOCUS.TITLE],
                                                                            next_focus[FOCUS.DESC],
                                                                            next_focus[FOCUS.TRANSLATE_TITLE],
                                                                            next_focus[FOCUS.TRANSLATE_DESC]])
        print(event, values)
    interface.Close()
    interface = work_with_interface.get_default_interface()
    return interface

work_with_interface = WorkWIthInterface()

work_with_interface.get_theme()#ToDo можно сделать это настройкой, не забыть прокинуть логгер, создать вкладку для переводчиков и progressbar
interface = work_with_interface.get_default_interface()

while True:
    try:
        event, values = interface.read()
        #print(event, values) #debug
        if event in (None, 'Exit', 'Cancel'):
            break
        elif event == 'MODE':
            interface.Close()
            interface = work_with_interface.change_interfase(values['MODE'])
        elif event == 'Назад':
            interface.Close()
            interface = work_with_interface.get_default_interface()
        elif event == COMMANDS.INTERFACE_TRANSLATOR_PATH:
            interface.Close()
            interface = work_with_interface.change_interfase(COMMANDS.INTERFACE_TRANSLATOR_PATH)
        elif event == COMMANDS.BEGIN_TRANSLATE:
            general_file_path = values['GENERAL_PATH']
            additional_file_path = values['ADDITIONAL_FILE']
            if values['HELPER']:
                interface = __translator(interface, general_file_path, additional_file_path)
            else:
                interface.Close()
                interface = work_with_interface.change_interfase(COMMANDS.WHITHOUT_HELPER)
        elif event == 'Выполнить':
            try:
                mode = values['MODE']
                general_file_path = values['GENERAL_PATH']
                additional_file_path = values['ADDITIONAL_FILE']
                other_path = values['OTHER_FILE']
            except:
                pass
            if mode == COMMANDS.ADDITIONAL_ENGLISH:
                __check_input_two_path(general_file_path, additional_file_path)
                merger = AddFileInEnglish()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.ADDITIONAL_RUSSIAN:
                __check_input_two_path(general_file_path, additional_file_path)
                merger = AddFileInRussian()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.TRANSLATE_FILE:
                __check_input_two_path(general_file_path, additional_file_path)
                merger = TranslateFile()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.ALL_TRANSLATE_DIRECTRY:
                __check_input(general_file_path)
                merger = GeneralWorkWithDirectory(TranslateFile)
                merger.excution_operation_with_directory(general_file_path)
            elif mode == COMMANDS.TRANSFER_FILE:
                __check_input_two_path(general_file_path, additional_file_path)
                merger = TransferFile()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.ALL_TRANSFER_DIRECTORY:
                __check_input(general_file_path)
                merger = GeneralWorkWithDirectory(TransferFile)
                merger.excution_operation_with_directory(general_file_path)
            elif mode == COMMANDS.STREAMLINE_FILE:
                __check_input_two_path(general_file_path, additional_file_path)
                merger = StreamlineFile()
                merger.execute_operation(general_file_path, additional_file_path)
            elif mode == COMMANDS.STREAMLINE_DIRECTORY:
                __check_input(general_file_path)
                merger = GeneralWorkWithDirectory(StreamlineFile)
                merger.excution_operation_with_directory(general_file_path)
            elif mode == COMMANDS.SEARCH_UPDATE_STRING_FILE:
                __check_input_three_path(general_file_path, additional_file_path, other_path)
                merger = SearchUpdateString()
                merger.execute_operation(general_path_new_v=general_file_path,
                                         add_path=additional_file_path,
                                         general_path_old_v=other_path)
            elif mode == COMMANDS.SEARCH_UNTRANS_STRING_FILE:
                merger = SearchUntransString()
                merger.execute_operation(additional_file_path)

    except NotADirectoryError:
        print('Указанный путь не является папкой, укажите путь до папки')
    except FileNotFoundError:
        print('Указанные пути не ведут к файлам')
    except NotEnterPath:
        print('Один или несколько путей не введены, введите оба пути')
    except PathNotLeadToFile:
        print('Указанный путь не является файлом, укажите путь до файла')
    except PathMatch:
        print('Пути должны отличаться, укажите пути к разным файлам')
    except ConnectError:
        print('Отсутствует соединение с интернетом')
    except Exception as error:
        print('Неизвестная ошибка {} пожалуйста вышлите её автору проекта'.format(error))


#   /home/mitry/переводы/lta/localisation_eng/focus_BEX_l_english.yml
#   /home/mitry/переводы/lta/test/focus_BEX_l_russian.yml