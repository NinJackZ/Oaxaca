from driver import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

browser = webdriver.Chrome(ChromeDriverManager().install())

class TestStringMethods(unittest.TestCase):
    
    def test_login(self):
        browser.get('http://127.0.0.1:5000/login')
        browser.find_element(By.ID, "id_username").send_keys("Tommy")
        browser.find_element(By.ID, "id_password").send_keys("password")
        browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        assert browser.title != "401 Unauthorized"
        browser.get('http://127.0.0.1:5000/logout')
        browser.get('http://127.0.0.1:5000/status-waiter')
        assert browser.title == "401 Unauthorized"

    def test_orders(self):
        browser.get('http://127.0.0.1:5000/menu')
        browser.find_element(By.ID, "num").send_keys("3678")
        browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        #browser.find_element(By.ID, "order_button").click()
        browser.get('http://127.0.0.1:5000/orders/3678')
        assert "3678" in browser.find_element(By.ID, "table_number").text
        assert "1" in browser.find_element(By.ID, "total_items").text

        browser.get('http://127.0.0.1:5000/login')
        browser.find_element(By.ID, "id_username").send_keys("Tommy")
        browser.find_element(By.ID, "id_password").send_keys("password")
        browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        browser.get('http://127.0.0.1:5000/status-waiter')
        sleep(0.1)
        browser.find_elements(By.TAG_NAME, 'button')[0].click()
        browser.get('http://127.0.0.1:5000/logout')
        browser.get('http://127.0.0.1:5000/menu/3678')

    def test_menu(self):
        browser.get('http://127.0.0.1:5000/login')
        browser.find_element(By.ID, "id_username").send_keys("Tommy")
        browser.find_element(By.ID, "id_password").send_keys("password")
        browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click() 
        browser.get('http://127.0.0.1:5000/edit-menu')

        browser.find_element(By.ID, "item_name").send_keys("Fish and Chips")
        browser.find_element(By.ID, "price").send_keys("ao10.55")
        browser.find_element(By.ID, "calories").send_keys("995")
        browser.find_element(By.ID, "order_button").click()
        assert "ao10.55" in browser.find_elements(By.TAG_NAME, 'table')[0].text
        
    def test_buttons(self):
        None
        #browser.get('http://127.0.0.1:5000/')

if __name__ == '__main__':
    unittest.main()