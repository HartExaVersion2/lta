import PySimpleGUI as sg
from common.constant import COMMANDS

list_commands = [COMMANDS.ADDITIONAL_ENGLISH, COMMANDS.ADDITIONAL_RUSSIAN, COMMANDS.TRANSFER_FILE,
                 COMMANDS.ALL_TRANSLATE_DIRECTRY, COMMANDS.TRANSLATE_FILE, COMMANDS.ALL_TRANSFER_DIRECTORY,
                 COMMANDS.STREAMLINE_FILE, COMMANDS.STREAMLINE_DIRECTORY, COMMANDS.SEARCH_UPDATE_STRING_FILE,
                 COMMANDS.SEARCH_UNTRANS_STRING_FILE]

class Interfaces:
    def get_add_file_eng(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ADDITIONAL_ENGLISH, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_add_file_ru(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ADDITIONAL_RUSSIAN, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_search_untrans_str(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.SEARCH_UNTRANS_STRING_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Файл для поиска непереведённых слов:')],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор')],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_search_update_str(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.SEARCH_UPDATE_STRING_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Файл локализации (новый):')],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Файл локализации (старый):')],
        [sg.InputText(key='OTHER_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_streamline_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.STREAMLINE_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_trinsfer_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.TRANSFER_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_translate_file(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.TRANSLATE_FILE, size=(85, 1), enable_events=True)],
        [sg.Text('Оригинальный файл:', size=(20, 1))],
        [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Text('Ваш файл:', size=(20, 1))],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.ProgressBar(max_value=100, orientation='h', size=(45, 15), key='progressbar')],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_transfer_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ALL_TRANSFER_DIRECTORY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_translate_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.ALL_TRANSLATE_DIRECTRY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_streamline_directory(self):
        return [[sg.Combo(values=list_commands, key='MODE', default_value=COMMANDS.STREAMLINE_DIRECTORY, size=(85, 1), enable_events=True)],
        [sg.Text('Дирректория с файлами локализации:')],
        [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
        [sg.Button(button_text='Назад'), sg.Button(button_text='Выполнить')]]

    def get_interface_translator_path(self):
        return [[sg.Checkbox(default=True, text='Помощник в переводе', key='HELPER')],
         [sg.Text('Оригинальный файл:', size=(20, 1))],
         [sg.InputText(key='GENERAL_PATH', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
         [sg.Text('Ваш файл:', size=(20, 1))],
         [sg.InputText(key='ADDITIONAL_FILE', size=(55, 1)), sg.FileBrowse(size=(10, 1), button_text='Обзор'), ],
         [sg.Button(button_text='Назад'), sg.Button(button_text=COMMANDS.BEGIN_TRANSLATE)]]

    def get_interface_translator_without_helper(self, param: list):
        return [[sg.Text(param[0], size=(60, 10)), sg.Multiline(size=(60, 10), key='title')],
                [sg.Text(param[1], size=(60, 40)), sg.Multiline(size=(60, 40), key='desc')],
                [sg.Button(button_text='Назад'), sg.Button(button_text='Сохранить'), sg.Button(button_text='Далее')]]

    def get_interface_translator_with_helper(self, param: list):
        return [[sg.Text(param[0], size=(60, 10)), sg.Text(param[2], size=(60, 10)), sg.Multiline(size=(60, 10), key='title')],
                [sg.Text(param[1], size=(60, 40)), sg.Text(param[3], size=(60, 40)), sg.Multiline(size=(60, 40), key='desc')],
                [sg.Button(button_text='Назад'), sg.Button(button_text='Сохранить'), sg.Button(button_text='Далее')]]

    def get_default(self):
        return [[sg.Text('Привет, выбери желаемый режим'), sg.Text('||Новая тема'), sg.Combo(values=sg.theme_list(), size=(20, 1), key='NEW_THEME', enable_events=True)],
        [sg.Button(button_text=COMMANDS.INTERFACE_TRANSLATOR_PATH)],
        [sg.Combo(values=list_commands, key='MODE', size=(85, 1), enable_events=True)]]
