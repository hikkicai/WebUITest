from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestTurtle():

    def __init__(self):
        pass

    def get_webdriver(self):
        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        self.driver = sl._current_browser()

    def setup(self):
        self.driver.implicitly_wait(15)
        self.driver.get("http://www.baidu.com")
        print(self.driver.title)

    def test_crawl(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()

    def test_run(self):
        settings = self.driver.find_element_by_css_selector('#u > a.pf')
        ActionChains(self.driver).move_to_element(settings).perform()
        self.driver.find_element_by_css_selector('#wrapper > div.bdpfmenu > a.setpref').click()

        WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 's1_2')))
        self.driver.find_element_by_id('s1_2').click()

        self.driver.find_element_by_id('nr').click()
        self.driver.find_element_by_css_selector('#nr > option:nth-child(2)').click()

    def tearDownClass(self):
        print("This is test teardown of test web")