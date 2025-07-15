from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://muntasir101.github.io/Movie-Ticket-Booking/")

number_of_tickets = driver.find_element(by=By.ID, value="tickets")
number_of_tickets.send_keys("0")

book_now_button = driver.find_element(by=By.CSS_SELECTOR, value="body > div > button")
book_now_button.click()