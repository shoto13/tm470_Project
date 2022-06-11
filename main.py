#TM470 Project
import selenium
from selenium import webdriver
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup


#SET STANDARD ZOOM
zoom = 1.0

disablejs = False
disableimages = False

## FUNCTIONS ##

# LOAD URL FUNCTION
def url_button_clicked():
    url = urlString.get()

    #make sure URL has correct prefix
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + urlString.get()

    msg = f'Your entered URL {url} has been displayed'

    driver.get(url)
    showinfo(
        title='Information',
        message=msg
    )


# FLIP PAGE FUNCTION
def flip_page_180():
    try:
        elem1 = driver.find_element(By.CSS_SELECTOR, 'body')
        driver.execute_script("arguments[0].style.transform ='rotate(180deg)';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that element')


# CHANGE FONT COLOUR
def colour_text_red():
    try:
        elem1 = driver.find_element(By.TAG_NAME, 'body')
        driver.execute_script("arguments[0].style.color='red';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that element')


    try:
        elem2 = driver.find_elements(By.TAG_NAME, 'p')
        for element in elem2:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem2.tag_name))
    except:
        print('could not find that element')


    try:
        elem3 = driver.find_element(By.TAG_NAME, 'h1')
        driver.execute_script("arguments[0].style.color='red';", elem3)
        print('Found <%s> element with that class name!' % (elem3.tag_name))
    except:
        print('could not find that element')


    try:
        elem4 = driver.find_elements(By.TAG_NAME, 'h2')
        for element in elem4:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem4.tag_name))
    except:
        print('could not find that element')


    try:
        elem5 = driver.find_elements(By.TAG_NAME, 'iframe')
        for element in elem5:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem5.tag_name))
    except:
        print('could not find that element')


    try:
        elem6 = driver.find_elements(By.TAG_NAME, 'ul')
        for element in elem6:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem6.tag_name))
    except:
        print('could not find that element')


    try:
        elem7 = driver.find_elements(By.TAG_NAME, 'div')
        for element in elem7:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem7.tag_name))
    except:
        print('could not find that element')

    try:
        elem8 = driver.find_elements(By.TAG_NAME, 'a')
        for element in elem8:
            driver.execute_script("arguments[0].style.color='red';", element)
        print('Found <%s> element with that class name!' % (elem8.tag_name))
    except:
        print('could not find that element')


# ZOOM PAGE
def zoom_page():
    global zoom
    zoom = zoom + 0.1
    try:
        driver.execute_script("document.body.style.zoom='%s';" % zoom)
    except:
        print('Zooming unsuccessful')


# ZOOM PAGE OUT
def zoom_page_out():
    global zoom
    zoom = zoom - 0.1
    try:
        driver.execute_script("document.body.style.zoom='%s';" % zoom)
    except:
        print('Zooming unsuccessful')


# DISABLE/ENABLE JAVASCRIPT
def toggle_js():
    try:

        # Global functions to let us work with driver from within our functions
        global disablejs
        global driver

        # Switch disablejs boolean without knowing its value
        disablejs = not disablejs
        msg = "Restarting the browser with updated JavaScript settings"

        # Close - BUT DO NOT KILL - driver so that we can update chrome options.
        driver.close()
        chrome_options_set()

        driver = webdriver.Chrome(
            executable_path=PATH,
            chrome_options=options
        )

        showinfo(
            title='Information',
            message=msg
        )

        #Re-get the URL
        url_button_clicked()
        print('Sent the commands to disable/enable JS')
        print('disable javascript: ' + str(disablejs))

    except:
        print('could not find that')


# DISABLE/ENABLE IMAGES
def toggle_images():
    try:

        # Global functions to let us work with driver from within our functions
        global disableimages
        global driver

        # Switch disableimages boolean without knowing its value
        disableimages = not disableimages
        msg = "Restarting the browser with updated Image display settings"

        # Close - BUT DO NOT KILL - driver so that we can update chrome options.
        driver.close()
        chrome_options_set()

        driver = webdriver.Chrome(
            executable_path=PATH,
            chrome_options=options
        )

        showinfo(
            title='Information',
            message=msg
        )

        # Re-get the URL
        url_button_clicked()
        print('Sent the commands to disable/enable Images')
        print('disable images: ' + str(disableimages))

    except:
        print('could not find that')


def dl_page_source():
    try:
        dfile = open("psDown.html", "w")
        dfile.write(driver.page_source)
        showinfo(
            title='Information',
            message='The page source was downloaded'
        )

    except:
        print('could not download page source')

def display_text_content_exclusive():
    try:
        url = 'https://' + urlString.get() +'/'
        print(url)
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        elem1 = driver.find_element(By.TAG_NAME, 'p')

        print(text)
        #TODO GET THIS WORKING SO THAT THE TEXT CONTENT IS DISPLAYED IN THE WEB BROWSER
        driver.execute_script('document.body.innerHTML = "{html}";'.format(html=text), elem1)

    except:
        print('could not download page source')



def change_bg_colour():
    try:
        elem1 = driver.find_element(By.CSS_SELECTOR, 'body')
        driver.execute_script("arguments[0].style.backgroundColor ='blue';", elem1)
        print("That seems to have worked to be honest")

    except:
        print("That didn't work at all")

def block_adverts():
    try:
        all_iframes = driver.find_elements_by_tag_name("iframe")
        if len(all_iframes) > 0:
            print("Ad Found\n")
            driver.execute_script("""
                var elems = document.getElementsByTagName("iframe"); 
                for(var i = 0, max = elems.length; i < max; i++)
                     {
                         elems[i].hidden=true;
                     }
                                  """)
            print('Total Ads: ' + str(len(all_iframes)))
        else:
            print('No frames found')

    except:
        print("That did not work for some reason")



# GUI SETUP
window = tk.Tk()

window.geometry('500x700')
window.resizable(False, False)
window.title('TM470 application test')

urlString = tk.StringVar()

# URL ENTRY INFO
urlLabel = ttk.Label(window, text="Enter URL:")
urlLabel.pack(fill='x', expand=True)

urlEntry = ttk.Entry(window, textvariable=urlString)
urlEntry.pack(fill='x', expand=True)
urlEntry.focus()


# URL RUN BUTTON
urlButton = ttk.Button(window, text="Get Page", command=url_button_clicked)
urlButton.pack(fill='x', expand=True, pady=10)

# FLIP PAGE BUTTON
flipButton = ttk.Button(window, text="Flip page 180", command=flip_page_180)
flipButton.pack(fill='x', expand=True, pady=10)

# FONT COLOUR BUTTON
recolourButton = ttk.Button(window, text="Recolour text", command=colour_text_red)
recolourButton.pack(fill='x', expand=True, pady=10)

# ZOOM PAGE IN
resizeButton = ttk.Button(window, text="Zoom page in", command=zoom_page)
resizeButton.pack(fill='x', expand=True, pady=10)

# ZOOM PAGE OUT
resizeButton = ttk.Button(window, text="Zoom page out", command=zoom_page_out)
resizeButton.pack(fill='x', expand=True, pady=10)

# DISABLE JS BUTTON
toggleJsButton = ttk.Button(window, text="Toggle JavaScript On/Off", command=toggle_js)
toggleJsButton.pack(fill='x', expand=True, pady=10)

# DOWNLOAD PAGE TO FILE
downloadPageButton = ttk.Button(window, text="Download page source", command=dl_page_source)
downloadPageButton.pack(fill='x', expand=True, pady=10)

# DISPLAY JUST TEXTUAL CONTENT
textOnlyButton = ttk.Button(window, text="Display page text", command=display_text_content_exclusive)
textOnlyButton.pack(fill='x', expand=True, pady=10)

# REMOVE IMAGES
disableImagesButton = ttk.Button(window, text="Toggle page images On/Off", command=toggle_images)
disableImagesButton.pack(fill='x', expand=True, pady=10)

# CHANGE BACKGROUND COLOURS
changeBackgroundButton = ttk.Button(window, text="Change Background colour", command=change_bg_colour)
changeBackgroundButton.pack(fill='x', expand=True, pady=10)

# BLOCK ADVERTS
blockAdsButton = ttk.Button(window, text="Block Adverts", command=block_adverts)
blockAdsButton.pack(fill='x', expand=True, pady=10)


options = Options()

def chrome_options_set():

    if disablejs:
        options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
    else:
        options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 1})

    if disableimages:
        options.add_argument('--blink-settings=imagesEnabled=false')
    else:
        options.add_argument('--blink-settings=imagesEnabled=true')


PATH = "/home/vxv/chromedriver"

driver = webdriver.Chrome(
    executable_path=PATH,
    options=options
)


window.mainloop()




