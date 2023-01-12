from Data import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_18(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    username = selenium.find_element(By.ID, "username").send_keys(valid_phone)
    Password = selenium.find_element(By.ID, "password").send_keys(valid_password)
    button = selenium.find_element(By.ID, "kc-login").click()

    button2 = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "phone_action"))
    )

    area1 = selenium.find_element(By.CLASS_NAME, "user-contacts-item__title")
    x1 = area1.text
    assert x1 == "Мобильный телефон"
    area2 = selenium.find_element(By.CSS_SELECTOR, "#app > main > div > div.home > div.base-card.home__info-card > div.user-contacts.home__user-contacts > div:nth-child(1) > div > span.dots-table-item__right > span")
    x2 = area2.text
    assert x2 == random_phone_with_spaces


def test_19(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    username = selenium.find_element(By.ID, "username").send_keys(valid_mail)
    Password = selenium.find_element(By.ID, "password").send_keys(valid_password)
    button = selenium.find_element(By.ID, "kc-login").click()

    button2 = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "phone_action"))
    )

    area1 = selenium.find_element(By.CSS_SELECTOR, "#app > main > div > div.home > div.base-card.home__info-card > div.user-contacts.home__user-contacts > div:nth-child(2) > div > span.dots-table-item__left > span")
    x1 = area1.text
    assert x1 == "Электронная почта"
    area2 = selenium.find_element(By.CSS_SELECTOR, "#app > main > div > div.home > div.base-card.home__info-card > div.user-contacts.home__user-contacts > div:nth-child(2) > div > span.dots-table-item__right > span")
    x2 = area2.text
    assert x2 == valid_mail


def test_20(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    username = selenium.find_element(By.ID, "username").send_keys(valid_phone)
    Password = selenium.find_element(By.ID, "password").send_keys("Example12!")
    button = selenium.find_element(By.ID, "kc-login").click()

    button2 = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-error-message"))
    )

    area1 = selenium.find_element(By.CSS_SELECTOR, "#form-error-message")
    x1 = area1.text
    assert x1 == "Неверный логин или пароль"



def test_21(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    username = selenium.find_element(By.ID, "username").send_keys(valid_mail)
    Password = selenium.find_element(By.ID, "password").send_keys("Example12!")
    button = selenium.find_element(By.ID, "kc-login").click()


    button2 = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-error-message"))
    )

    area1 = selenium.find_element(By.CSS_SELECTOR, "#form-error-message")
    x1 = area1.text
    assert x1 == "Неверный логин или пароль"
