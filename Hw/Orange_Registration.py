from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from faker import Faker
fake = Faker()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
time.sleep(18)

FirstName = driver.find_element(by=By.ID, value="input-firstname")
FirstName.send_keys(fake.first_name())

LastName = driver.find_element(by=By.ID, value="input-lastname")
LastName.send_keys(fake.last_name())

E_mail = driver.find_element(by=By.ID, value="input-email")
E_mail.send_keys(fake.email())

Telephone = driver.find_element(by=By.ID, value="input-telephone")
Telephone.send_keys(fake.phone_number())

Password = driver.find_element(by=By.ID, value="input-password")
Password.send_keys("123456")

PasswordConfirm = driver.find_element(by=By.ID, value="input-confirm")
PasswordConfirm.send_keys("123456")

Subscribe = driver.find_element(by=By.NAME, value="newsletter")
Subscribe.click()

Privacy_Policy = driver.find_element(by=By.NAME, value="agree")
Privacy_Policy.click()

Continue = driver.find_element(by=By.CSS_SELECTOR, value="input.btn")
Continue.click()