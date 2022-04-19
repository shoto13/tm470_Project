#TM470 Project

from selenium import webdriver
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


ffile = open("intecc.html", "w")

# BROWSER SETUP
chrome_options = webdriver.ChromeOptions()
PATH = "/home/vxv/chromedriver"
driver = webdriver.Chrome(
    executable_path=PATH,
    chrome_options=chrome_options
)

driver.get('https://flagstoneprojects.com')


# search = driver.find_element(By.ID, "twotabsearchtextbox")
# search.send_keys("mario")
# search.send_keys(Keys.RETURN)

a = 3

if a == 1:
    try:
        elem1 = driver.find_element(By.TAG_NAME, 'body')
        print("done that")
        driver.execute_script("arguments[0].style.display='none';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that shit tbh')

#ROTATE THE PAGE 180
if a == 2:
    try:
        elem1 = driver.find_element(By.CSS_SELECTOR, 'body')
        print("done that")
        driver.execute_script("arguments[0].style.transform ='rotate(180deg)';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that shit tbh')


if a == 3:
    try:
        elem1 = driver.find_element(By.CSS_SELECTOR, '*')
        print("done that")
        driver.execute_script("arguments[0].style.color='red';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that shit tbh')

#WRITE THE PAGE SOURCE TO A NEW DOC
if a == 4:
    try:
        ffile.write(driver.page_source)
    except:
        print('could not find that shit tbh')




# try:
#     elem1 = driver.find_element(By.TAG_NAME, 'h1')
#     print("done that")
#     driver.execute_script("arguments[0].style.color='red';", elem1)
#     print('Found <%s> element with that class name!' % (elem1.tag_name))
# except:
#     print('could not find that shit tbh')
# try:
#     elem1 = driver.find_element(By.TAG_NAME, 'h2')
#     print("done that")
#     driver.execute_script("arguments[0].style.color='red';", elem1)
#     print('Found <%s> element with that class name!' % (elem1.tag_name))
# except:
#     print('could not find that shit tbh')
#
# try:
#     elem1 = driver.find_element(By.TAG_NAME, 'h3')
#     print("done that")
#     driver.execute_script("arguments[0].style.color='red';", elem1)
#     print('Found <%s> element with that class name!' % (elem1.tag_name))
# except:
#     print('could not find that shit tbh')
#
# try:
#     elem1 = driver.find_element(By.TAG_NAME, 'p')
#     print("done that")
#     driver.execute_script("arguments[0].style.color='red';", elem1)
#     print('Found <%s> element with that class name!' % (elem1.tag_name))
# except:
#     print('could not find that shit tbh')
#
# try:
#     elem1 = driver.find_element(By.TAG_NAME, 'footer')
#     print("done that")
#     driver.execute_script("arguments[0].style.color='red';", elem1)
#     print('Found <%s> element with that class name!' % (elem1.tag_name))
# except:
#     print('could not find that shit tbh')
#
# try:
#     elem1 = driver.find_element(By.TAG_NAME, 'section')
#     print("done that")
#     driver.execute_script("arguments[0].style.color='red';", elem1)
#     print('Found <%s> element with that class name!' % (elem1.tag_name))
# except:
#     print('could not find that shit tbh')
#


