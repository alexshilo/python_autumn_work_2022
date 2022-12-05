# импортируем модули!
import xml.etree.ElementTree as Etree
import os
import xlsxwriter


# вспомогательные функции поиска данных
def getEnumValues(type_property_enumerated_value):
    """Фукнция поиска EnumItem в EnumList. Записывание в виде списка через запятую."""
    enum_list = type_property_enumerated_value.find('EnumList')
    enum_item_list = []
    for enum_item in enum_list.iter("EnumItem"):
        enum_item_list.append(enum_item.text)
    return ','.join(enum_item_list)


def getPropertyType(element_property_type):
    """Функция поиска типа данных (DataType, TypePropertyReferenceValue, TypePropertyEnumeratedValue)"""
    for child in element_property_type.iter():
        if child.tag == 'TypePropertySingleValue':
            return child.find('DataType').get('type')
        if child.tag == 'TypePropertyReferenceValue':
            return child.get('reftype')
        if child.tag == 'TypePropertyEnumeratedValue':
            return getEnumValues(child)


def getNameAlias(name_aliases, required_lang):
    """Функция поиска нужного языка для NameAlias"""
    for name_alias in name_aliases.iterfind('NameAlias'):
        lang = name_alias.get('lang')
        if lang == required_lang:
            return name_alias.text
    return ''


def getDefinitionAlias(definition_aliases, required_lang):
    """Функция поиска нужного языка для DefinitionAlias"""
    for definition_alias in definition_aliases.iterfind('DefinitionAlias'):
        lang = definition_alias.get('lang')
        if lang == required_lang:
            return definition_alias.text
    return ''

def convertXmlToXlsx(XML_path, XLSX_path):
    "Основаня функция по парсингу XML и созданию XLSX-таблицы"
    tree = Etree.parse(XML_path)                                             # создаем дерево
    workbook = xlsxwriter.Workbook(XLSX_path)                                # создаем xlsx
    worksheet = workbook.add_worksheet()                                     # добавляем лист в xlsx-документе
    worksheet.write_row(0, 0, ['Наименование', 'Наименование ENG', 'Наименование RUS', 'Тип данных', 'Описание RUS'])
    row_index = 1                                                            # делаем столбцы и названия
    property_set_def = tree.getroot()
    property_defs = property_set_def.find('PropertyDefs')                    # ищем property_defs в структуре XML
    for property_def in property_defs.iterfind('PropertyDef'):               # цикл для поиска всех нужных данных
        name = property_def.find('Name').text
        property_type = getPropertyType(property_def.find('PropertyType'))
        name_aliases = property_def.find('NameAliases')
        en_name_alias = getNameAlias(name_aliases, "en")
        ru_name_alias = getNameAlias(name_aliases, "ru-RU")
        definition_aliases = property_def.find('DefinitionAliases')
        def_alias = getDefinitionAlias(definition_aliases, "ru-RU")
        worksheet.write_row(row_index, 0, [name, en_name_alias, ru_name_alias, property_type, def_alias])
        row_index += 1
    workbook.close()

# создание и вывод XLSX-файлов
path_to_program = "C:/Users/shilo_av/OneDrive/Python"                       # обращаемся к корневой папке
path_to_XML = path_to_program + "/psd/"                                     # папка с XML-файлами
path_to_XLSX = path_to_program + "/xlsx/"                                   # папка, где будем записывать XLSX
files_list = os.listdir(path_to_XML)                                        # назначаем, где лежит список файлов

for file in files_list:                                                     # цикл для записи файлов в XLSX
    convertXmlToXlsx(path_to_XML + file, path_to_XLSX + file + ".xlsx")






