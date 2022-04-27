#TM470 Project

from selenium import webdriver
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


## FUNCTIONS ##
# LOAD URL FUNCTION
def url_button_clicked():
    # ADD HTTP PREFIX TO ENTERED URL SO THAT IT RUNS CORRECTLY
    url = 'https://' + urlString.get()
    msg = f'Your entered URL was: {url}'

    driver.get(url)
    showinfo(
        title='Information',
        message=msg
    )

# FLIP PAGE FUNCTION
def flip_page_180():
    try:
        elem1 = driver.find_element(By.CSS_SELECTOR, 'body')
        print("done that")
        driver.execute_script("arguments[0].style.transform ='rotate(180deg)';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that shit tbh')



# GUI SETUP
window = tk.Tk()

window.geometry('500x300')
window.resizable(False, False)
window.title('TM470 application test')

urlString = tk.StringVar()

# URL ENTRY INFO
urlLabel = ttk.Label(window, text="Enter URL:")
urlLabel.pack(fill='x', expand=True)

urlEntry = ttk.Entry(window, textvariable=urlString)
urlEntry.pack(fill='x', expand=True)
urlEntry.focus()


#URL RUN BUTTON
urlButton = ttk.Button(window, text="Get Page", command=url_button_clicked)
urlButton.pack(fill='x', expand=True, pady=10)

#FLIP PAGE BUTTON
flipButton = ttk.Button(window, text="Flip page 180", command=flip_page_180)
flipButton.pack(fill='x', expand=True, pady=10)


chrome_options = webdriver.ChromeOptions()
PATH = "/home/vxv/chromedriver"
driver = webdriver.Chrome(
    executable_path=PATH,
    chrome_options=chrome_options
)




window.mainloop()


ffile = open("intecc.html", "w")


a = 0

if a == '1':
    try:
        elem1 = driver.find_element(By.TAG_NAME, 'body')
        print("done that")
        driver.execute_script("arguments[0].style.display='none';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that shit tbh')

#ROTATE THE PAGE 180
if a == '2':
    try:
        elem1 = driver.find_element(By.CSS_SELECTOR, 'body')
        print("done that")
        driver.execute_script("arguments[0].style.transform ='rotate(180deg)';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that shit tbh')


if a == '3':
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


