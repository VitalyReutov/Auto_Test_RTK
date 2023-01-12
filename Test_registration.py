from Data import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_1(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    button = selenium.find_element(By.ID, "kc-register").click()
    firstname = selenium.find_element(By.NAME, "firstName").send_keys("Ян")
    lastname = selenium.find_element(By.NAME, "lastName").send_keys("ТесТесТесТеТесТесТесТесТесТесТ")
    email = selenium.find_element(By.ID, "address").send_keys(random_mail)
    password = selenium.find_element(By.ID, "password").send_keys("Exa12!@#")
    password2 = selenium.find_element(By.ID, "password-confirm").send_keys("Exa12!@#")
    button_confirm = selenium.find_element(By.NAME, "register").click()
    area1 = selenium.find_element(By.CLASS_NAME, "register-confirm-form-container__desc")
    x1 = area1.text
    assert x1 == f"Kод подтверждения отправлен на адрес {random_mail}"


def test_2(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    button = selenium.find_element(By.ID, "kc-register").click()
    firstname = selenium.find_element(By.NAME, "firstName").send_keys("ТесТесТесТе-ТесТесТесТесТесТес")
    lastname = selenium.find_element(By.NAME, "lastName").send_keys("Я-")
    phone = selenium.find_element(By.ID, "address").send_keys(random_phone)
    password = selenium.find_element(By.ID, "password").send_keys("Exa12!@#Exa12!@#Exa1")
    password2 = selenium.find_element(By.ID, "password-confirm").send_keys("Exa12!@#Exa12!@#Exa1")
    button_confirm = selenium.find_element(By.NAME, "register").click()
    area1 = selenium.find_element(By.CLASS_NAME, "register-confirm-form-container__desc")
    x1 = area1.text
    assert x1 == f"Kод подтверждения отправлен на номер {random_phone_with_spaces}"

def test_3(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    button = selenium.find_element(By.ID, "kc-register").click()
    firstname = selenium.find_element(By.NAME, "firstName").send_keys("Я")
    lastname = selenium.find_element(By.NAME, "lastName").send_keys("ТесТесТесТесТесТесТесТесТесТесТ")
    email = selenium.find_element(By.ID, "address").send_keys("example")
    password = selenium.find_element(By.ID, "password").send_keys("Abc12!@")
    password2 = selenium.find_element(By.ID, "password-confirm").send_keys("Exa12!@#Exa12!@#Exa12")
    button_confirm = selenium.find_element(By.NAME, "register").click()

    area1 = selenium.find_element(By.CSS_SELECTOR, "#page-right > div > div > div > form > div.name-container > div:nth-child(1) > span")
    x1 = area1.text
    assert x1 == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    area2 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.name-container > div:nth-child(2) > span")
    x2 = area2.text
    assert x2 == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    area3 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.rt-input-container.rt-input-container--error.email-or-phone.register-form__address > span")
    x3 = area3.text
    assert x3 == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    area4 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.new-password-container > div.rt-input-container.rt-input-container--error.new-password-container__password > span")
    x4 = area4.text
    assert x4 == "Длина пароля должна быть не менее 8 символов"

    area5 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.new-password-container > div.rt-input-container.rt-input-container--error.new-password-container__confirmed-password > span")
    x5 = area5.text
    assert x5 == "Длина пароля должна быть не более 20 символов"

def test_4(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    button = selenium.find_element(By.ID, "kc-register").click()
    firstname = selenium.find_element(By.NAME, "firstName").send_keys("ТесТесТесТесТесТесТесТесТесТесТ")
    lastname = selenium.find_element(By.NAME, "lastName").send_keys("Я")
    phone = selenium.find_element(By.ID, "address").send_keys("+7999111223311")
    password = selenium.find_element(By.ID, "password").send_keys("Exa12!@#Exa12")
    password2 = selenium.find_element(By.ID, "password-confirm").send_keys("Example12!@#")
    button_confirm = selenium.find_element(By.NAME, "register").click()
    area1 = selenium.find_element(By.CSS_SELECTOR, "#page-right > div > div > div > form > div.name-container > div:nth-child(1) > span")
    x1 = area1.text
    assert x1 == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    area2 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.name-container > div:nth-child(2) > span")
    x2 = area2.text
    assert x2 == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    area3 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.rt-input-container.rt-input-container--error.email-or-phone.register-form__address > span")
    x3 = area3.text
    assert x3 == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    area5 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.new-password-container > div.rt-input-container.rt-input-container--error.new-password-container__confirmed-password > span")
    x5 = area5.text
    assert x5 == "Пароли не совпадают"

def test_5(selenium):

    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    button = selenium.find_element(By.ID, "kc-register").click()
    firstname = selenium.find_element(By.NAME, "firstName").send_keys("Ян")
    lastname = selenium.find_element(By.NAME, "lastName").send_keys("ТесТесТесТеТесТесТесТесТесТесТ")
    email = selenium.find_element(By.ID, "address").send_keys("example@gmail.com")
    password = selenium.find_element(By.ID, "password").send_keys("Exa12!@#")
    password2 = selenium.find_element(By.ID, "password-confirm").send_keys("Exa12!@#")
    button_confirm = selenium.find_element(By.NAME, "register").click()
    area1 = selenium.find_element(By.CSS_SELECTOR,
                                      "#page-right > div > div > div > form > div.base-modal-wrapper.card-modal > div > div > h2")
    x1 = area1.text
    assert x1 == "Учётная запись уже существует"

    area2 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.base-modal-wrapper.card-modal > div > div > div.card-modal__btns > button")
    x2 = area2.text
    assert x2 == "Войти"

    area3 = selenium.find_element(By.CSS_SELECTOR,
                                  "#reg-err-reset-pass")
    x3 = area3.text
    assert x3 == "Восстановить пароль"

def test_6(selenium):

    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    button = selenium.find_element(By.ID, "kc-register").click()
    firstname = selenium.find_element(By.NAME, "firstName").send_keys("Ян")
    lastname = selenium.find_element(By.NAME, "lastName").send_keys("ТесТесТесТеТесТесТесТесТесТесТ")
    phone = selenium.find_element(By.ID, "address").send_keys("+79998769120")
    password = selenium.find_element(By.ID, "password").send_keys("Exa12!@#")
    password2 = selenium.find_element(By.ID, "password-confirm").send_keys("Exa12!@#")
    button_confirm = selenium.find_element(By.NAME, "register").click()
    area1 = selenium.find_element(By.CSS_SELECTOR,
                                      "#page-right > div > div > div > form > div.base-modal-wrapper.card-modal > div > div > h2")
    x1 = area1.text
    assert x1 == "Учётная запись уже существует"

    area2 = selenium.find_element(By.CSS_SELECTOR,
                                  "#page-right > div > div > div > form > div.base-modal-wrapper.card-modal > div > div > div.card-modal__btns > button.rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.rt-btn--transparent")
    x2 = area2.text
    assert x2 == "Зарегистрироваться"

def test_7(selenium):

    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    button = selenium.find_element(By.ID, "kc-register").click()
    firstname = selenium.find_element(By.NAME, "firstName").send_keys("Ян")
    lastname = selenium.find_element(By.NAME, "lastName").send_keys("ТесТесТесТеТесТесТесТесТесТесТ")
    email = selenium.find_element(By.ID, "address").send_keys("example@gmail.com")
    password = selenium.find_element(By.ID, "password").send_keys("Exa12!@#")
    password2 = selenium.find_element(By.ID, "password-confirm").send_keys("Exa12!@#")
    button_confirm = selenium.find_element(By.NAME, "register").click()
    area1 = selenium.find_element(By.CSS_SELECTOR,
                                          "#page-right > div > div > h1")
    x1 = area1.text
    assert x1 == "Авторизация"

def test_8(selenium):

    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))
    )
    button = selenium.find_element(By.ID, "kc-register").click()
    firstname = selenium.find_element(By.NAME, "firstName").send_keys("Ян")
    lastname = selenium.find_element(By.NAME, "lastName").send_keys("ТесТесТесТеТесТесТесТесТесТесТ")
    phone = selenium.find_element(By.ID, "address").send_keys("+79998769120")
    password = selenium.find_element(By.ID, "password").send_keys("Exa12!@#")
    password2 = selenium.find_element(By.ID, "password-confirm").send_keys("Exa12!@#")
    button_confirm = selenium.find_element(By.NAME, "register").click()
    button2 = selenium.find_element(By.CSS_SELECTOR, "#page-right > div > div > div > form > div.base-modal-wrapper.card-modal > div > div > div.card-modal__btns > button.rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.rt-btn--transparent").click()

    area1 = selenium.find_element(By.CSS_SELECTOR,
                                              "#page-right > div > div > div > p")
    x1 = area1.text
    assert x1 == f"Kод подтверждения отправлен на номер {random_phone_with_spaces}"



