import openpyxl
from raw_text_function import sum_of_recipe, data_of_recipe, nip_of_recipe, get_description_from_google\
    , type_of_transation, description, adres
import datetime

path_to_excel = r'C:\Users\Marek\Desktop\python_291223_cost_of_life\cost_of_life.xlsx'
path_to_backup = r'C:\Users\Marek\Desktop\python_291223_cost_of_life\backup.xlsx'


sheet = openpyxl.load_workbook(path_to_excel)

active_sheet = sheet.active

sheet.save(path_to_backup)

data_txt = r'C:\Users\Marek\Desktop\python_291223_cost_of_life\raw\177_output_text.txt'

with open(data_txt, 'r', encoding='utf-8') as data:
    lines = [linia.strip() for linia in data.readlines()]

last_row = active_sheet.max_row
new_row = last_row +1
active_sheet[f'A{new_row}'] = new_row - 1

current_data = datetime.datetime.now()
active_sheet[f'B{new_row}'] = (current_data.strftime('%G,%m,%d'))

sum = sum_of_recipe(lines)
active_sheet[f'F{new_row}'] = sum

data = data_of_recipe(lines)
active_sheet[f'C{new_row}'] = data

transation = type_of_transation(lines)
active_sheet[f'G{new_row}'] = transation

nip = nip_of_recipe(lines)
shop_description = get_description_from_google(nip)
active_sheet[f'D{new_row}'] = shop_description

transation = type_of_transation(lines)
active_sheet[f'G{new_row}'] = transation

description = description(lines)
active_sheet[f'H{new_row}'] = description

adres = adres(lines)
active_sheet[f'E{new_row}'] = adres

sheet.save(path_to_excel)
