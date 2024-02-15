from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import time
import json

with open('Config/config.json') as file:
    config_data = json.load(file)


def get_text(_data, tag, class_name):
    detail = _data.find(tag, class_=class_name)
    try:
        detail = detail.text.replace('\n', '')
    except AttributeError:
        detail = 'n/a'
    return detail


def click_item(driver, wait_time: int, x_path: str):
    (WebDriverWait(driver, wait_time)
     .until(EC.presence_of_element_located((By.XPATH, x_path)))
     .click())

    time.sleep(wait_time)


def send_data(driver, wait_time: int, x_path: str, data: str):
    (WebDriverWait(driver, wait_time)
     .until(EC.element_to_be_clickable((By.XPATH, x_path)))
     .send_keys(data))

    time.sleep(wait_time)


def perform_action_chain(driver, wait_time: int, x_path: str):
    element = (WebDriverWait(driver, wait_time)
               .until(EC.element_to_be_clickable((By.XPATH, x_path))))

    ActionChains(driver).move_to_element(element).perform()

    time.sleep(wait_time)
