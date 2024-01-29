from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# open google and copy description of first serched result


def get_description_from_google(query):

    driver_path = r'C:\chromedriver_win32\chromedriver.exe'
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.google.com")

    time.sleep(2)

    search_box = driver.find_element("name", "q")

    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    try:
        first_result = driver.find_element("css selector", 'div.tF2Cxc')
        description = first_result.text
    except Exception as e:
        print("can t find solution:", str(e))
        description = ""

    driver.quit()
    description = description.split()
    description = str(description[0:3])
    return description


# from recipe find row with text = sum pln and match to excel
def sum_of_recipe(lines):
    suma = "error"
    for phrases in lines:
        if "SUMA" in phrases and "PLN" in phrases:
            row_suma = phrases.split()
            for word in row_suma:
                try:
                    word = word.replace(",", ".")
                    suma = float(str(word))
                except:
                    print(" ")
    return suma


def data_of_recipe(lines):
    data = "error"
    for phrases in lines:

        if "2023" in phrases or "2024" in phrases:
            data = phrases

    return data

# find number of nip for shop
def nip_of_recipe(lines):
    nip = "error"
    for phrases in lines:
        if "NIP" in phrases:
            nip = phrases
    return nip


def type_of_transation(lines):
    transation = "error"
    for phrases in lines:
        if "karta" in phrases or "KARTA":
            transation = "karta"
        elif "GOTÓWKA" in phrases:
            transation = "gotówka"
    return transation

def  description(lines):
    n = 0
    end_description = 0
    start_description = 0
    for phrases in lines:
        n = n+1
        if "PARAGON" in phrases:
            start_description = n + 1
        elif "SUMA" in phrases or "Suma":
            end_description = n - 1
    description = str(lines[start_description:end_description])
    return description

def  adres(lines):
    n = 0
    end_adres = 0
    start_adres = 0
    for phrases in lines:
        n = n+1
        if "ul." in phrases or "Ul." in phrases or "UL." in phrases:
            start_adres = n - 1
            end_adres = n + 1
            print(start_adres)
            print(end_adres)
    adres = str(lines[start_adres:end_adres])
    print(adres)
    return adres