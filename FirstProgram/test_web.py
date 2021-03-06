from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import time
import logging
from nose.tools import eq_
from nose.tools import ok_

def setup():
    global driver
    opt = webdriver.ChromeOptions()
    opt.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    opt.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    opt.add_argument("window-size=1920x1080")
    opt.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    opt.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    driver = webdriver.Chrome(options=opt)
    # driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.get("http://www.baidu.com")
    print(driver.title)


def teardown():
    driver.close()


def test_dataframe():
    elem1 = driver.find_element_by_id("kw")
    elem2 = driver.find_element_by_id("su")
    elem3 = None
    df = pd.DataFrame(data=[[elem1, elem2, elem3], [elem1, elem2, elem3]], index=[1, 2])
    # logging.error("This is an error msg")


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
    driver.find_element_by_css_selector('#sugConf>th').click()


if __name__ == '__main__':
    setup()
    test_searching()
    test_changesetting()
    teardown()
