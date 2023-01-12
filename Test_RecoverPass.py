from Data import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_22(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "forgot_password"))
    )
    button = selenium.find_element(By.ID, "forgot_password").click()

    area1 = selenium.find_element(By.CSS_SELECTOR, "#page-right > div > div > h1")
    x1 = area1.text
    assert x1 == "Восстановление пароля"

def test_23(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "forgot_password"))
    )
    button = selenium.find_element(By.ID, "forgot_password").click()

    area1 = selenium.find_element(By.ID, "t-btn-tab-phone")
    x1 = area1.text
    assert x1 == "Телефон"

def test_24(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "forgot_password"))
    )
    button = selenium.find_element(By.ID, "forgot_password").click()

    area1 = selenium.find_element(By.ID, "t-btn-tab-mail")
    x1 = area1.text
    assert x1 == "Почта"

def test_25(selenium):
    selenium.get(URL)
    button = WebDriverWait(selenium, 15).until(
        EC.element_to_be_clickable((By.ID, "forgot_password"))
    )
    button = selenium.find_element(By.ID, "forgot_password").click()

    area1 = selenium.find_element(By.ID, "reset")
    x1 = area1.text
    assert x1 == "Продолжить"

    area2 = selenium.find_element(By.ID, "reset-back")
    x2 = area2.text
    assert x2 == "Вернуться назад"