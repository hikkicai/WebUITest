from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time
from nose import with_setup
import logging


def setUp():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.get("http://www.baidu.com")
    print(driver.title)

def tearDown():
    driver.close()

def test_dataframe():
    elem1 = driver.find_element_by_id("kw")
    elem2 = driver.find_element_by_id("su")
    elem3 = None
    df = pd.DataFrame(data=[elem1, elem2, elem3], index=[1, 2, 3])
    print(df)


def test_searching():
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()


def test_changesetting():
    settings = driver.find_element_by_css_selector('#u > a.pf')
    ActionChains(driver).move_to_element(settings).perform()
    driver.find_element_by_css_selector('#wrapper > div.bdpfmenu > a.setpref').click()

    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 's1_2')))
    driver.find_element_by_id('s1_2').click()

    driver.find_element_by_id('nr').click()
    driver.find_element_by_css_selector('#nr > option:nth-child(2)').click()


if __name__ == '__main__':
    setUp()
    test_searching()
    test_changesetting()
    tearDown()