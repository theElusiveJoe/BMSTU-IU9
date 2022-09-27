from models import regex_node
from tools import alt_splitter
from tools import concat_splitter
from tools import brackets_helper
from tools import graph_creator


class Regex_parser():

    def __init__(self, filepath=None, raw_text=None):
        if filepath is not None:
            with open(filepath, 'r') as f:
                self.raw_text = f.read()
        else:
            self.raw_text = raw_text

    def parse(self):
        # self.raw_text = self.raw_text.strip()

        # убираем пробелы
        self.raw_text = ''.join(filter(lambda x: x != ' ', self.raw_text))

        if self.raw_text == '':
            return regex_node.Symbol_node('')

        # проверяем на наличие запрещенных символов
        for x in self.raw_text:
            if not x.isalpha() and not x in '()|*':
                raise Exception(
                    f'в "{self.raw_text}" недопустимый символ: "{x}"')

        # проверяем, как дела со скобками
        i = 0
        for x in self.raw_text:
            if x == '(':
                i += 1
            elif x == ')':
                i -= 1
        if i != 0:
            raise Exception(f'в "{self.raw_text}" проблема со скобками')

        return self.parse_alternative(self.raw_text)

    def parse_alternative(self, raw_string):
        # # print('->>  ALT RAW', raw_string)
        raw_string = brackets_helper.remove_side_extra_brackets(raw_string)
        # # print('->>  ALT NO BRACKETS', raw_string)
        if alt_splitter.substrs_num(raw_string) == 1:
            return self.parse_concat(raw_string)

        # # # print('>>>parse_alt\n    ', raw_string, '==>', children)
        children = alt_splitter.get_list_of_subs(raw_string)
        # # print('->>  ALT RAW CHLIDREN', children)
        for i in range(len(children)):
            children[i] = self.parse_concat(children[i])
        return regex_node.Alternative_node(children)

    def parse_concat(self, raw_string):
        # # print('->>  CONCAT RAW', raw_string)
        concat_num = concat_splitter.concats_num(raw_string)
        if concat_num == 1:
            return self.parse_asterix(raw_string)

        children = concat_splitter.get_list_of_subs(raw_string)
        # # print('->>  CONCAT RAW CHLIDREN', children)
        for i in range(len(children)):
            children[i] = self.parse_asterix(children[i])
        return regex_node.Concat_node(children)

    def parse_asterix(self, raw_string):
        # # print('->>  ASTERIX RAW', raw_string)
        
        if raw_string == '':
            # # print('это пустая строка')
            return regex_node.Symbol_node('')

        if raw_string == '*':
            raise Exception(
                'найдена подрегулярка, состоящая только из звездочки')

        if raw_string[-1] == '*':
            if raw_string[0] == '(':
                # # print('скобочки со звездочкой')
                child = self.parse_alternative(raw_string[:-1])
                return regex_node.Asterix_node([child])
            elif raw_string[0].isalpha() and len(raw_string) == 2:
                # # print('буковка со зведочкой')
                child = regex_node.Symbol_node(raw_string[0])
                return regex_node.Asterix_node([child])
            else:
                raise Exception(
                    f'в подрегулярке {raw_string} итерация Клини применяется к чему-то некорректному')

        if raw_string[0] == '(':
            # # print('скобочки без звездочки')
            return self.parse_alternative(raw_string)
        elif raw_string[0].isalpha() and len(raw_string) == 1:
            # # print('буковка без звездочки')
            return regex_node.Symbol_node(raw_string[0])
        else:
            raise Exception(f'найдено что-то непонятное: {raw_string}')
