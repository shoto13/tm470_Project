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
from tkinter import *


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
        print('could not find that ')


# CHANGE FONT COLOUR
def make_text_red():
    try:
        elem1 = driver.find_element(By.TAG_NAME, 'body')
        print("done that")
        driver.execute_script("arguments[0].style.color='red';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that')


    try:
        elem2 = driver.find_elements(By.TAG_NAME, 'p')

        for element in elem2:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem2.tag_name))
    except:
        print('could not find that')


    try:
        elem3 = driver.find_element(By.TAG_NAME, 'h1')
        print("done that")
        driver.execute_script("arguments[0].style.color='red';", elem3)
        print('Found <%s> element with that class name!' % (elem3.tag_name))
    except:
        print('could not find that')


    try:
        elem4 = driver.find_elements(By.TAG_NAME, 'h2')

        for element in elem4:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem4.tag_name))
    except:
        print('could not find that')


    try:
        elem5 = driver.find_elements(By.TAG_NAME, 'iframe')
        for element in elem5:
            driver.execute_script("arguments[0].style.color='red';", element)

        print('Found <%s> element with that class name!' % (elem5.tag_name))
    except:
        print('could not find that')


    try:
        elem6 = driver.find_elements(By.TAG_NAME, 'ul')
        for element in elem6:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem6.tag_name))
    except:
        print('could not find that')


    try:
        elem7 = driver.find_elements(By.TAG_NAME, 'div')
        for element in elem7:
            driver.execute_script("arguments[0].style.color='red';", element)
    except:
        print('could not find that')

    try:
        elem8 = driver.find_elements(By.TAG_NAME, 'a')
        for element in elem8:
            driver.execute_script("arguments[0].style.color='red';", element)
    except:
        print('could not find that')


# CHANGE FONT SIZE
def make_text_larger():
    try:
        elem20 = driver.find_element(By.TAG_NAME, 'p')
        driver.execute_script("arguments[0].style.font-size='20px';", elem20)
        print('Found <%s> element with that class name!' % (elem20.tag_name))
    except:
        print('could not find that')


# DISABLE JAVASCRIPT
def disable_js():
    try:
        elem1 = driver.find_element(By.TAG_NAME, 'html')
        print("done that")
        driver.execute_script("arguments[0].style.font-weight='bold';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that')



# DOWNLOAD WEB PAGE TO FILE


# GUI SETUP
window = tk.Tk()

window.geometry('500x500')
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

# FONT COLOUR BUTTON
recolourButton = ttk.Button(window, text="Recolour text", command=make_text_red)
recolourButton.pack(fill='x', expand=True, pady=10)

# FONT SIZE BUTTON
resizeButton = ttk.Button(window, text="Change font size", command=make_text_larger)
resizeButton.pack(fill='x', expand=True, pady=10)

# DISABLE JS BUTTON
disableJsButton = ttk.Button(window, text="Disable JavaScript", command=make_text_red())
disableJsButton.pack(fill='x', expand=True, pady=10)

# DOWNLOAD PAGE TO FILE
downloadPageButton = ttk.Button(window, text="Download page source", command=make_text_red)
downloadPageButton.pack(fill='x', expand=True, pady=10)



chrome_options = webdriver.ChromeOptions()
PATH = "/home/vxv/chromedriver"
driver = webdriver.Chrome(
    executable_path=PATH,
    chrome_options=chrome_options
)


window.mainloop()

#
# ffile = open("intecc.html", "w")
#
# #WRITE THE PAGE SOURCE TO A NEW DOC
# if False:
#     try:
#         ffile.write(driver.page_source)
#     except:
#         print('could not find that')


