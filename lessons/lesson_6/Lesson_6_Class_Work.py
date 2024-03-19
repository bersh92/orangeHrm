"""
Classwork Assignment Description:

Objective:
The goal of this assignment is to practice interacting with web elements using Selenium WebDriver.
You will open a web application, log in, navigate to the 'HR Administration' section via the side menu,
click on the 'More' dropdown menu, and then retrieve and print all section names listed under this dropdown.

Steps to Complete the Assignment:
1. Open the web application in a web browser using Selenium WebDriver.
2. Log into the application using the credentials provided by your instructor.
3. After logging in, locate the side menu and navigate to the 'HR Administration' section.
   You might need to click on the menu to expand it and reveal the 'HR Administration' option.
4. Within the 'HR Administration' section, find and click on the 'More' dropdown menu to reveal more options.
5. Identify all the sections listed under the 'More' dropdown.
6. Use a loop to iterate through these sections and collect their names or any identifiable text.
7. Print the names of all sections found under the 'More' dropdown to the console.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://portnov_admin-trials711.orangehrmlive.com/client/#/dashboard")

driver.find_element(By.CSS_SELECTOR, "input[id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[id='txtPassword']").send_keys("qTJn5@5APu")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)

sidebar_toggle = driver.find_element(By.CSS_SELECTOR, '#sidebar-toggle[class="circle"]')
sidebar_menu = driver.find_element(By.CSS_SELECTOR, '#left-menu[class="sidebar menu-visible"]')
if not sidebar_menu.is_displayed():
    sidebar_toggle.click()
    time.sleep(1)
    # driver.find_element(By.XPATH, '//a/span[text()="HR Administration"][1]').click()
    # I suppose you meant to click on 'Employee Management' because 'HR Administration' doesn't have 'More' section
    driver.find_element(By.XPATH, '//a/span[text()="Employee Management"][1]').click()
else:
    # driver.find_element(By.XPATH, '//a/span[text()="HR Administration"][1]').click()
    driver.find_element(By.XPATH, '//a/span[text()="Employee Management"][1]').click()
time.sleep(3)

driver.find_element(By.XPATH, '//a[text()="More "]').click()
more_dropdown = driver.find_elements(By.XPATH, "//a[contains(text(),'More ')]/following-sibling::sub-menu-container//a")
more_dropdown_names = []
for name in more_dropdown:
    more_dropdown_names.append(name.text)
print(more_dropdown_names)
#I give up
#I tried using XPath and CSS to find only the element from the 'More' section dropdown.
# However, when searching for them in the DevTools on a webpage,
# it found 16 elements that are truly related to the 'More' section. But PyCharm prints unexpected text and also text not from More section
driver.quit()