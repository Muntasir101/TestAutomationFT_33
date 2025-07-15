from selenium import webdriver

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/")

driver.close()



