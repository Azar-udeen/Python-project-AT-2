

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_1 = webdriver.Firefox()
driver_1.maximize_window()
driver_1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(2)
driver_1.implicitly_wait(20)
driver_1.find_element(By.XPATH, "//*[@placeholder='Username']").send_keys("Admin")
driver_1.find_element(By.XPATH, "//*[@type='password']").send_keys("admin123")
driver_1.find_element(By.XPATH, "//*[@type='submit']").click()
driver_1.implicitly_wait(20)
print("You are logged in Successfully")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]").click()
driver_1.implicitly_wait(20)
print("Admin option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]").click()
driver_1.implicitly_wait(20)
print("PIM option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[3]").click()
driver_1.implicitly_wait(20)
print("Leave option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[4]").click()
driver_1.implicitly_wait(20)
print("Time option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[5]").click()
driver_1.implicitly_wait(20)
print("Recruitment option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[6]").click()
driver_1.implicitly_wait(20)
print("My Info option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[7]").click()
driver_1.implicitly_wait(20)
print("Performance option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[8]").click()
driver_1.implicitly_wait(20)
print("Dashboard option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[9]").click()
driver_1.implicitly_wait(20)
print("Directory option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[10]").click()
driver_1.implicitly_wait(20)
print("Maintenance option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[11]").click()
driver_1.implicitly_wait(20)
print("Claim option present in menu option")

driver_1.find_element(By.XPATH, "(//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[12]").click()
driver_1.implicitly_wait(20)
print("Buzz option present in menu option")

driver_1.quit()