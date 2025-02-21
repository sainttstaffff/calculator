import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

@pytest.fixture
def browser():
    options = Options()
    options.headless = True  
    service = Service('/path/to/geckodriver', log_path='/path/to/logfile.log') 
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

def test_addition(browser):
    browser.get('http://localhost:5000')  
    browser.find_element(By.NAME, 'num1').send_keys('3')
    browser.find_element(By.NAME, 'num2').send_keys('2')
    browser.find_element(By.NAME, 'operation').send_keys('add')
    browser.find_element(By.NAME, 'operation').send_keys(Keys.RETURN)
    time.sleep(1)  
    result = browser.find_element(By.ID, 'result').text  
    assert result == '5.0'  

def test_subtraction(browser):
    browser.get('http://localhost:5000')
    browser.find_element(By.NAME, 'num1').send_keys('3')
    browser.find_element(By.NAME, 'num2').send_keys('2')
    browser.find_element(By.NAME, 'operation').send_keys('subtract')
    browser.find_element(By.NAME, 'operation').send_keys(Keys.RETURN)
    time.sleep(1)
    result = browser.find_element(By.ID, 'result').text
    assert result == '1.0'

def test_multiplication(browser):
    browser.get('http://localhost:5000')
    browser.find_element(By.NAME, 'num1').send_keys('3')
    browser.find_element(By.NAME, 'num2').send_keys('2')
    browser.find_element(By.NAME, 'operation').send_keys('multiply')
    browser.find_element(By.NAME, 'operation').send_keys(Keys.RETURN)
    time.sleep(1)
    result = browser.find_element(By.ID, 'result').text
    assert result == '6.0'

def test_division(browser):
    browser.get('http://localhost:5000')
    browser.find_element(By.NAME, 'num1').send_keys('3')
    browser.find_element(By.NAME, 'num2').send_keys('2')
    browser.find_element(By.NAME, 'operation').send_keys('divide')
    browser.find_element(By.NAME, 'operation').send_keys(Keys.RETURN)
    time.sleep(1)
    result = browser.find_element(By.ID, 'result').text
    assert result == '1.5'

def test_degree(browser):
    browser.get('http://localhost:5000')
    browser.find_element(By.NAME, 'num1').send_keys('3')
    browser.find_element(By.NAME, 'num2').send_keys('2')
    browser.find_element(By.NAME, 'operation').send_keys('degree')
    browser.find_element(By.NAME, 'operation').send_keys(Keys.RETURN)
    time.sleep(1)
    result = browser.find_element(By.ID, 'result').text
    assert result == '9.0'  
def test_maximum(browser):
    browser.get('http://localhost:5000')
    browser.find_element(By.NAME, 'num1').send_keys('3')
    browser.find_element(By.NAME, 'num2').send_keys('5')
    browser.find_element(By.NAME, 'operation').send_keys('maximum')
    browser.find_element(By.NAME, 'operation').send_keys(Keys.RETURN)
    time.sleep(1)
    result = browser.find_element(By.ID, 'result').text
    assert result == '5.0'  
def test_minimum(browser):
    browser.get('http://localhost:5000')
    browser.find_element(By.NAME, 'num1').send_keys('3')
    browser.find_element(By.NAME, 'num2').send_keys('5')
    browser.find_element(By.NAME, 'operation').send_keys('minimum')
    browser.find_element(By.NAME, 'operation').send_keys(Keys.RETURN)
    time.sleep(1)
    result = browser.find_element(By.ID, 'result').text
    assert result == '3.0'