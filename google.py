import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'http://google.com'

def chrome():    
    display = Display(visible=0, size=(800, 600))
    display.start()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('DevOps')
    search_box.submit()

    RESULTS_LOCATOR = "//div/h3/a"
    results = driver.find_elements_by_css_selector('div > div > h3 > a')

    if(len(results) != 0):
        print('%s results have been found on the first page' % len(results))
    else:
        print('no results have been found')
 

    driver.quit()
    display.stop()

if __name__ == '__main__':
    chrome()
    
    
