import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class CathaybkAutomation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")

    def test_capture_main_page_screenshot(self):
        self.driver.save_screenshot("main.png")
    
    def test_credit_card_info(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[1]/div/div/div[1]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="lnk_SiteMenuLink"]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div').click()

        

        elements = self.driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]')
        
        actions = ActionChains(self.driver)
        actions.move_to_element(elements).perform()

        x = elements.find_elements(By.XPATH, 'a')
        print("信用卡項目有：" + str(len(x)))

        self.driver.save_screenshot("credit.png")
    
    def test_quit_cards(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[1]/div/div/div[1]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="lnk_SiteMenuLink"]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="lnk_Link"]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/main/article/div/div/div/div[1]/div/div/a[6]').click()

        elements = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]')

        actions = ActionChains(self.driver)
        actions.move_to_element(elements).perform()

        x = elements.find_elements(By.XPATH, 'div')

        print("停發卡：" + str(len(x)))

        self.driver.save_screenshot("quit.png")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
