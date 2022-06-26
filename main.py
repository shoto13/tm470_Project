#TM470 Project
import selenium
import user_settings
import page_control_functions
import dbfile
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
from ttkthemes import ThemedStyle
from tkinter.colorchooser import askcolor

#DB SETUP
#db username: tm470test
#db pass: dAVg7WKRh01pGudx


# USER DEFINED SETTINGS
text_colour_preference = "#C4826E"
background_colour_preference = "#5865F2"
javascript_on_preference = True
page_images_preference = False
show_ads_preference = False

test_user_settings = dbfile.u_settings_collection.find_one({})
print(test_user_settings)


#SET STANDARD ZOOM
zoom = 1.0

initialised = False

## FUNCTIONS ##

# START UP SCRIPT
def startup_init_jsimgs():
    global initialised
    chrome_options_set()


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
def colour_text():
    global text_colour_preference

    # ONLY LAUNCH THE COLOUR PICKER IF THE APP IS ALREADY INITIALISED,
    # IF NOT WE WILL USE THE COLOUR VALUE PREV DEFINED AND STORED IN MONGO
    if initialised:
        text_colour_preference = change_color()

    try:

        elem1 = driver.find_element(By.TAG_NAME, 'body')
        driver.execute_script('arguments[0].style.color="{}";'.format(text_colour_preference), elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that element')


    try:
        elem2 = driver.find_elements(By.TAG_NAME, 'p')
        for element in elem2:
            driver.execute_script('arguments[0].style.color="{}";'.format(text_colour_preference), element)
        print('Found <%s> element with that class name!' % (elem2.tag_name))
    except:
        print('could not find that element')


    try:
        elem3 = driver.find_element(By.TAG_NAME, 'h1')
        driver.execute_script('arguments[0].style.color="{}";'.format(text_colour_preference), elem3)
        print('Found <%s> element with that class name!' % (elem3.tag_name))
    except:
        print('could not find that element')


    try:
        elem4 = driver.find_elements(By.TAG_NAME, 'h2')
        for element in elem4:
            driver.execute_script('arguments[0].style.color="{}";'.format(text_colour_preference), element)
        print('Found <%s> element with that class name!' % (elem4.tag_name))
    except:
        print('could not find that element')


    try:
        elem5 = driver.find_elements(By.TAG_NAME, 'iframe')
        for element in elem5:
            driver.execute_script('arguments[0].style.color="{}";'.format(text_colour_preference), element)
        print('Found <%s> element with that class name!' % (elem5.tag_name))
    except:
        print('could not find that element')


    try:
        elem6 = driver.find_elements(By.TAG_NAME, 'ul')
        for element in elem6:
            driver.execute_script('arguments[0].style.color="{}";'.format(text_colour_preference), element)
        print('Found <%s> element with that class name!' % (elem6.tag_name))
    except:
        print('could not find that element')


    try:
        elem7 = driver.find_elements(By.TAG_NAME, 'div')
        for element in elem7:
            driver.execute_script('arguments[0].style.color="{}";'.format(text_colour_preference), element)
        print('Found <%s> element with that class name!' % (elem7.tag_name))
    except:
        print('could not find that element')

    try:
        elem8 = driver.find_elements(By.TAG_NAME, 'a')
        for element in elem8:
            driver.execute_script('arguments[0].style.color="{}";'.format(text_colour_preference), element)
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
        global javascript_on_preference
        global driver

        # Switch disablejs boolean without knowing its value
        javascript_on_preference = not javascript_on_preference
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
        print('disable javascript: ' + str(javascript_on_preference))

    except:
        print('could not find that')


# DISABLE/ENABLE IMAGES
def toggle_images():
    try:

        # Global functions to let us work with driver from within our functions
        global driver
        global page_images_preference

        # Switch image preference boolean without knowing its value
        page_images_preference = not page_images_preference
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

# DOWNLOAD PAGE SOURCE TO FILE
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

# DISPLAY THE TEXT CONTENT OF THE WEB PAGE IN A NEW TAB
def display_text_content_exclusive():
    try:

        elem1 = driver.find_element(By.TAG_NAME, 'body')
        #print(elem1.text)
        tttwo = elem1.text

        text_file = open("page_content.html", "w")
        text_file.write(tttwo)
        text_file.close()

        #driver.execute_script("window.open('file:///home/vxv/PycharmProjects/tm470_Project/page_content.html')")
        driver.switch_to.new_window()
        driver.get('file:///home/vxv/PycharmProjects/tm470_Project/page_content.html')
    except:
        print('could not download page source')


def change_bg_colour():
    global background_colour_preference

    if initialised:
        background_colour_preference = change_color()

    try:
        elem1 = driver.find_element(By.CSS_SELECTOR, 'body')
        driver.execute_script("arguments[0].style.backgroundColor ='{}';".format(background_colour_preference), elem1)
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


# COLOUR PICKER FUNC
def change_color():
    colors = askcolor(title="Tkinter Color Chooser")[1]
    print(colors)
    return colors


# GUI SETUP
window = tk.Tk()

window.geometry('500x700')
window.resizable(True, True)
window.title('TM470 application test')

# TAB DISPLAY SETUP
tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Controls')
tabControl.add(tab2, text='Settings')

tabControl.pack(expand=1, fill="both")


# Set the initial theme
style = ThemedStyle(window)
style.theme_use('adapta')

urlString = tk.StringVar()


# TAB 1 ====!!!!!====
# URL ENTRY INFO
urlLabel = ttk.Label(tab1, text="Enter URL:")
urlLabel.pack(fill='x', expand=True)

urlEntry = ttk.Entry(tab1, textvariable=urlString)
urlEntry.pack(fill='x', expand=True)
urlEntry.focus()


# URL RUN BUTTON
urlButton = ttk.Button(tab1, text="Get Page", command=url_button_clicked)
urlButton.pack(fill='x', expand=True, pady=8)


# FLIP PAGE BUTTON
flipButton = ttk.Button(tab1, text="Flip page 180", command=flip_page_180)
flipButton.pack(fill='x', expand=True, pady=8)


# FONT COLOUR BUTTON
recolourButton = ttk.Button(tab1, text="Recolour text", command=colour_text)
recolourButton.pack(fill='x', expand=True, pady=8)

# ZOOM PAGE IN
resizeButton = ttk.Button(tab1, text="Zoom page in", command=zoom_page)
resizeButton.pack(fill='x', expand=True, pady=8)

# ZOOM PAGE OUT
resizeButton = ttk.Button(tab1, text="Zoom page out", command=zoom_page_out)
resizeButton.pack(fill='x', expand=True, pady=8)

# DISABLE JS BUTTON
toggleJsButton = ttk.Button(tab1, text="Toggle JavaScript On/Off", command=toggle_js)
toggleJsButton.pack(fill='x', expand=True, pady=8)

# DOWNLOAD PAGE TO FILE
downloadPageButton = ttk.Button(tab1, text="Download page source", command=dl_page_source)
downloadPageButton.pack(fill='x', expand=True, pady=8)

# DISPLAY JUST TEXTUAL CONTENT
textOnlyButton = ttk.Button(tab1, text="Display page text", command=display_text_content_exclusive)
textOnlyButton.pack(fill='x', expand=True, pady=8)

# REMOVE IMAGES
disableImagesButton = ttk.Button(tab1, text="Toggle page images On/Off", command=toggle_images)
disableImagesButton.pack(fill='x', expand=True, pady=8)

# CHANGE BACKGROUND COLOURS
changeBackgroundButton = ttk.Button(tab1, text="Change Background colour", command=change_bg_colour)
changeBackgroundButton.pack(fill='x', expand=True, pady=8)

# BLOCK ADVERTS
blockAdsButton = ttk.Button(tab1, text="Block Adverts", command=block_adverts)
blockAdsButton.pack(fill='x', expand=True, pady=8)


#TAB 2 ====!!!!====

textColourLabel = ttk.Label(tab2, text="Text colour preference: " + text_colour_preference)
textColourLabel.pack(fill='x', expand=True)

backgroundColourLabel = ttk.Label(tab2, text="Background colour preference: " + background_colour_preference)
backgroundColourLabel.pack(fill='x', expand=True)


if (javascript_on_preference):
    jsp = "JavaScript ON"
else:
    jsp = "JavaScript OFF"

javascriptPreferenceLabel = ttk.Label(tab2, text="JavaScript on/off preference: " + jsp)
javascriptPreferenceLabel.pack(fill='x', expand=True)


if (page_images_preference):
    pip = "Image display ON"
else:
    pip = "Image display OFF"

imagesPreferenceLabel = ttk.Label(tab2, text="Page images preference: " + pip)
imagesPreferenceLabel.pack(fill='x', expand=True)

if (show_ads_preference):
    sap = "Adverts ON"
else:
    sap = "Adverts OFF"

adsPreferenceLabel = ttk.Label(tab2, text="Ad display preference: " + sap)
adsPreferenceLabel.pack(fill='x', expand=True)


options = Options()

def chrome_options_set():

    global javascript_on_preference
    global page_images_preference

    if javascript_on_preference:
        options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
    else:
        options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 1})

    if not page_images_preference:
        options.add_argument('--blink-settings=imagesEnabled=false')
    else:
        options.add_argument('--blink-settings=imagesEnabled=true')


PATH = "/home/vxv/chromedriver"
startup_init_jsimgs()

driver = webdriver.Chrome(
    executable_path=PATH,
    options=options
)

window.mainloop()




