from selenium import webdriver
import time
if __name__ == '__main__':
    driver =webdriver.Chrome()
    url = 'https://www.baidu.com'
    driver.get(url)
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id('su').click()
    driver.quit()