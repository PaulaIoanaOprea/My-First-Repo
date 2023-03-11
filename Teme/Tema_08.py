import time

import button as button
import radio as radio
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # initializare variabila

LINK = 'https://the-internet.herokuapp.com/'  # constanta pt a deschide browser-ul

driver.get(LINK)  # deschidere URL
time.sleep(2)

driver.maximize_window()  # maximizare fereastra
time.sleep(2)

# LINK TEXT

link_add_remove_elements = driver.find_element(By.LINK_TEXT, 'Add/Remove Elements')
print('')
link_add_remove_elements.click()
time.sleep(3)
driver.back()

link_digest_authentication = driver.find_element(By.LINK_TEXT, 'Digest Authentication')
print('')
link_digest_authentication.click()
time.sleep(3)
driver.back()

link_basic_auth = driver.find_element(By.LINK_TEXT, 'Basic Auth')
print('')
link_basic_auth.click()
time.sleep(3)
driver.back()

# PARTIAL LINK TEXT

link_partial_remove_elements = driver.find_element(By.PARTIAL_LINK_TEXT, 'Remove Elements')
link_partial_remove_elements.click()
time.sleep(3)
driver.back()

link_partial_digest = driver.find_element(By.PARTIAL_LINK_TEXT, 'Digest')
link_partial_digest.click()
time.sleep(3)
driver.back()

link_partial_menu = driver.find_element(By.PARTIAL_LINK_TEXT, 'Menu')
link_partial_menu.click()
time.sleep(3)
driver.back()

# TAG NAME

LINK = 'https://formy-project.herokuapp.com/checkbox'  # constanta pt a deschide browser-ul

driver.get(LINK)  # deschidere URL
time.sleep(2)

driver.maximize_window()  # maximizare fereastra
time.sleep(2)

lista_inputuri = driver.find_elements(By.TAG_NAME, "input")
print(f"Avem {len(lista_inputuri)} elemente cu tag-ul <input>")

for element in lista_inputuri:
    element.click()
    time.sleep(1)


LINK = 'https://formy-project.herokuapp.com/datepicker'  # constanta pt a deschide browser-ul

driver.get(LINK)  # deschidere URL
time.sleep(2)

driver.maximize_window()  # maximizare fereastra
time.sleep(2)

lista_inputuri = driver.find_elements(By.TAG_NAME, "input")
print(f"Avem {len(lista_inputuri)} elemente cu tag-ul <input>")

for element in lista_inputuri:
    element.click()
    time.sleep(1)

LINK = 'https://formy-project.herokuapp.com/autocomplete'  # constanta pt a deschide browser-ul

driver.get(LINK)  # deschidere URL
time.sleep(2)

driver.maximize_window()  # maximizare fereastra
time.sleep(2)

lista_inputuri = driver.find_elements(By.TAG_NAME, "input")
print(f"Avem {len(lista_inputuri)} elemente cu tag-ul <input>")

for element in lista_inputuri:
    element.click()
    time.sleep(1)

# ID

LINK = 'https://formy-project.herokuapp.com/form'  # constanta pt a deschide browser-ul

driver.get(LINK)  # deschidere URL
time.sleep(2)

driver.maximize_window()  # maximizare fereastra
time.sleep(2)

first_name_input = driver.find_element(By.ID, 'first-name')
assert first_name_input.is_displayed()

# CLASS NAME

LINK = 'https://formy-project.herokuapp.com/switch-window'  # constanta pt a deschide browser-ul

driver.get(LINK)  # deschidere URL
time.sleep(2)

driver.maximize_window()  # maximizare fereastra
time.sleep(2)

lista_elemente_form_group = driver.find_elements(By.CLASS_NAME, 'form-group')
print(f"Avem {len(lista_elemente_form_group)} elemente cu clasa 'form-group'")

for element in lista_elemente_form_group:
    element.click()
    time.sleep(1)

lista_elemente_navbar = driver.find_elements(By.CLASS_NAME, 'navbar')
print(f"Avem {len(lista_elemente_navbar)} elemente cu clasa 'navbar'")

for element in lista_elemente_navbar:
    element.click()
    time.sleep(1)

lista_elemente_container = driver.find_elements(By.CLASS_NAME, 'container')
print(f"Avem {len(lista_elemente_container)} elemente cu clasa 'container'")

for element in lista_elemente_container:
    element.click()
    time.sleep(1)

# CSS

LINK = 'https://formy-project.herokuapp.com/form'  # constanta pt a deschide browser-ul

driver.get(LINK)  # deschidere URL
time.sleep(2)

driver.maximize_window()  # maximizare fereastra
time.sleep(2)

id_css = driver.find_element(By.CSS_SELECTOR, '#job-title')  # dupa ID
id_css.send_keys('Inginer')
time.sleep(3)
id_css.clear()
time.sleep(3)

class_css = driver.find_element(By.CSS_SELECTOR, 'input.form-control')  # dupa clasa
class_css.send_keys('Oprea')
time.sleep(3)
class_css.clear()
time.sleep(3)

atribut_css = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
assert atribut_css.is_selected()
print('Pasul urmator')

# XPATH

LINK = 'https://formy-project.herokuapp.com/form'  # constanta pt a deschide browser-ul

driver.get(LINK)  # deschidere URL
time.sleep(2)

driver.maximize_window()  # maximizare fereastra
time.sleep(2)

atribut_1 = driver.find_element(By.XPATH, '/html/body/div/form/div/div[3]/input')
valoare_atribut_1 = driver.find_element(By.XPATH, '//*[@id="radio-button-3"]')
atribut_2 = driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[7]/input')
valoare_atribut_2 = driver.find_element(By.XPATH, '//*[@id="datepicker"]')
atribut_3 = driver.find_element(By.XPATH, '/html/body/div/form/div/div[6]/select')
valoare_atribut_3 = driver.find_element(By.XPATH, '//*[@id="select-menu"]')
print('')

text_integral_1 = driver.find_element(By.XPATH, '/html/body/div/form/div/div[1]/input')
text_1 = driver.find_element(By.XPATH, '//*[@id="first-name"]')
text_integral_2 = driver.find_element(By.XPATH, '/html/body/div/form/div/div[2]/input')
text_2 = driver.find_element(By.XPATH, '//*[@id="last-name"]')
text_integral_3 = driver.find_element(By.XPATH, '/html/body/div/form/div/div[2]/input')
text_3 = driver.find_element(By.XPATH, '//*[@placeholder="Enter last name"]')
print('')

text_partial = driver.find_element(By.XPATH, '//*[@class = "form-control"]')
print('')
