from program_interfaces.general_operations_interface import GeneralOperationsInterface
import shutil
import codecs
import os

from common.decorator_for_output_errors import decorator_for_output_errors

class GeneralOperations(GeneralOperationsInterface):

    @decorator_for_output_errors()
    def file_in_list(self, path_on_file: str) -> list:
        file = self.file_for_read(path_on_file)
        list_string = []
        for line in file:
            if line and (':' in line):
                try:
                    list_string.append(line.split(':', 1)[0])
                except:
                    pass
        file.close()
        return list_string

    @decorator_for_output_errors()
    def file_in_dict(self, path_on_file: str) -> dict:
        file = self.file_for_read(path_on_file)
        dict_string = {}
        for line in file:
            if line and line != '\n':
                try:
                    dict_string[line.split(':', 1)[0]] = ':' + line.split(':', 1)[1]
                except:
                    pass
        file.close()
        return dict_string

    @decorator_for_output_errors()
    def encod_utf8_bom(self, path_on_file: str):
        with codecs.open(path_on_file, encoding="utf-8") as f_in, codecs.open(path_on_file + ".yml", encoding="utf-8-sig", mode="w") as f_out:
            f_out.write(f_in.read())
        shutil.move(path_on_file + ".yml", path_on_file)

    @decorator_for_output_errors()
    def file_for_read(self, path_to_file: str):
        return codecs.open(path_to_file, 'r', 'utf_8_sig')

    @decorator_for_output_errors()
    def file_for_write(self, path_to_file: str):
        return codecs.open(path_to_file, 'w', 'utf_8_sig')