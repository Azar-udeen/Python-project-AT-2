from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
driver_1 = webdriver.Firefox()
driver_1.maximize_window()
driver_1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver_1.implicitly_wait(20)
driver_1.find_element(By.XPATH, "//*[@placeholder='Username']").send_keys("Admin")
driver_1.find_element(By.XPATH, "//*[@type='password']").send_keys("admin123")
driver_1.find_element(By.XPATH, "//*[@type='submit']").click()
driver_1.implicitly_wait(20)
print("You are logged in Successfully")

title_of_PageAdmin = driver_1.title
print(title_of_PageAdmin)
driver_1.find_element(By.LINK_TEXT, "Admin").click()
driver_1.implicitly_wait(20)
driver_1.find_element(By.XPATH, "(//*[@class='oxd-topbar-body-nav-tab-item'])[1]").click()
title_of_PageUser_management = driver_1.title
print(title_of_PageUser_management)

driver_1.find_element(By.XPATH, "(//*[@class='oxd-topbar-body-nav-tab-item'])[2]").click()
title_of_PageUser_Job = driver_1.title
print(title_of_PageUser_Job)

driver_1.find_element(By.XPATH, "(//*[@class='oxd-topbar-body-nav-tab-item'])[3]").click()
title_of_PageUser_Organization = driver_1.title
print(title_of_PageUser_Organization)

driver_1.find_element(By.XPATH, "(//*[@class='oxd-topbar-body-nav-tab-item'])[4]").click()
title_of_PageUser_Qualifications = driver_1.title
print(title_of_PageUser_Qualifications)

driver_1.find_element(By.XPATH, "(//*[@class='oxd-topbar-body-nav-tab-item'])[5]").click()
title_of_PageUser_Nationalities = driver_1.title
print(title_of_PageUser_Nationalities)

driver_1.find_element(By.XPATH, "(//*[@class='oxd-topbar-body-nav-tab-item'])[6]").click()
title_of_PageUser_CorporateBranding = driver_1.title
print(title_of_PageUser_CorporateBranding)

driver_1.find_element(By.XPATH, "(//*[@class='oxd-topbar-body-nav-tab-item'])[7]").click()
title_of_PageUser_Configuration = driver_1.title
print(title_of_PageUser_Configuration)