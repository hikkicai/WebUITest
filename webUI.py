from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.get("http://www.baidu.com")
    print(driver.title)

    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    settings = driver.find_element_by_css_selector('#u > a.pf')
    ActionChains(driver).move_to_element(settings).perform()
    driver.find_element_by_css_selector('#wrapper > div.bdpfmenu > a.setpref').click()

    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 's1_2')))
    driver.find_element_by_id('s1_2').click()

    driver.find_element_by_id('nr').click()
    # locator = (By.CSS_SELECTOR, '#nr > option:nth-child(2)')
    # WebDriverWait(driver, 0, 0.5).until(EC.element_to_be_clickable(locator))
    driver.find_element_by_css_selector('#nr > option:nth-child(2)').click()
    # rightcontainer > div.tsz > div.tabletsz > table > tbody > tr:nth-child(1) > td:nth-child(1)

    # rightcontainer > div.tsz > div.tabletsz > table > tbody > tr:nth-child(1) > td:nth-child(2)

    # rightcontainer > div.tsz > div.tabletsz > table > tbody > tr:nth-child(1) > td:nth-child(3)


