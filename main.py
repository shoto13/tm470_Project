#TM470 Project
import tkinter
import pymongo
import pandas as pd
import selenium
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
import pymongo
from itertools import cycle


# GET THE USER
user_settings = dbfile.u_settings_collection.find_one({"username": "test_user"})
print(user_settings)

# USER DEFINED SETTINGS
text_colour_preference = user_settings['text_colour_preference']
background_colour_preference = user_settings['background_colour_preference']
javascript_on = user_settings['javascript_on']
images_on = user_settings['images_on']
ads_on = user_settings['ads_on']

#SET STANDARD ZOOM
zoom = 1.0
# SET INITIALISED TO FALSE SO WE KNOW THE STATE OF THE APPLICATION
initialised = False

## FUNCTIONS ##
profiles_list = dbfile.u_settings_collection.distinct("profile_name")
print(profiles_list)

# ALL SCRIPTS ---___---
# START UP SCRIPTS
def startup_init_jsimgs():
    global initialised
    chrome_options_set()
    toggle_js()
    #initialised = True

def startup_init_colorise():
    global initialised
    colour_text()
    change_bg_colour()
    initialised = True

# LOAD URL FUNCTION
def url_button_clicked():
    global initialised
    url = urlString.get()

    #initialised = False

    #make sure URL has correct prefix
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + urlString.get()

    msg = 'Your entered URL ' + url + ' has been displayed'

    driver.get(url)

    showinfo(
        title='Information',
        message=msg
    )

    # IF APP IS NOT INITIALISED, RUN THE COLORISE FUNCTION WHEN URL IS LOADED
    if not initialised:
        startup_init_colorise()

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
    global initialised
    global text_colour_preference

    # ONLY LAUNCH THE COLOUR PICKER IF THE APP IS ALREADY INITIALISED,
    # IF NOT WE WILL USE THE COLOUR VALUE PREV DEFINED AND STORED IN MONGO
    print("Trying to figure out order")

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

    #UPDATE THE DICT
    user_settings['text_colour_preference'] = text_colour_preference

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
        global initialised
        global javascript_on
        global driver

        print(f"the initialised state at the beginning of toggle_js is {initialised}")

        # Switch disablejs boolean without knowing its value
        if initialised:
            javascript_on = not javascript_on
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
        print('disable javascript: ' + str(javascript_on))

        # UPDATE THE DICT
        user_settings['javascript_on'] = javascript_on

    except:
        print('could not find that')

# DISABLE/ENABLE IMAGES
def toggle_images():
    try:

        # Global functions to let us work with driver from within function
        global initialised
        global driver
        global images_on

        # Switch image preference boolean without knowing its value
        if initialised:
            images_on = not images_on
        msg = "Restarting the browser with updated Image display settings"

        # Close BUT DO NOT KILL driver so that we can update chrome options.
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
        print('disable images: ' + str(images_on))

        user_settings['images_on'] = images_on

    except:
        print('could not perform the image toggle action')

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

# BACKGROUND COLOUR CHANGER FUNCTION
def change_bg_colour():
    global initialised
    global background_colour_preference

    if initialised:
        background_colour_preference = change_color()

    try:
        elem1 = driver.find_element(By.CSS_SELECTOR, 'body')
        driver.execute_script("arguments[0].style.backgroundColor ='{}';".format(background_colour_preference), elem1)
        print("That seems to have worked to be honest")

    except:
        print("That didn't work at all")


    #UPDATE THE DICT
    user_settings['background_colour_preference'] = background_colour_preference

# AD BLOCKER FUNCTION
def block_adverts():
    try:
        iframes_collection = driver.find_elements(By.TAG_NAME, "iframe")
        if len(iframes_collection) > 0:
            print("Advert Found\n")
            driver.execute_script("""
                var elems = document.getElementsByTagName("iframe");
                for(var i = 0, max = elems.length; i < max; i++)
                     {
                         elems[i].hidden=true;
                     }
                                  """)
            print('Number of frames located: ' + str(len(iframes_collection)))
        else:
            print('No frames located')

    except:
        print("Ad blocking failed")

# COLOUR PICKER FUNC
def change_color():
    colors = askcolor(title="Tkinter Color Chooser")[1]
    print(colors)
    return colors

# SUMMARISATION FUNCTION
def summarise_page():
    try:
        elem1 = driver.find_elements(By.TAG_NAME, 'h1')

        #SET UP HMTL PAGE
        text_file = open("page_content_summary.html", "w")
        text_file.write("<html><head></head><body>")
        text_file.close()

        text_file = open("page_content_summary.html", "a")

        text_file.write("<h2>Primary page headers</h2><ul>")
        for x in range(len(elem1)):
            text_file.write("<li>" + elem1[x].text + "</li>")
            print(elem1[x].text)
        text_file.write("</ul>")

        elem2 = driver.find_elements(By.TAG_NAME, 'h2')

        text_file.write("<h2>Secondary page headers</h2><ul>")
        for x in range(len(elem2)):
            text_file.write("<li>" + elem2[x].text + "</li>")
            print(elem2[x].text)
        text_file.write("</ul>")

        elem3 = driver.find_elements(By.TAG_NAME, 'h3')

        text_file.write("<h2>Tertiary page headers</h2><ul>")
        for x in range(len(elem3)):
            text_file.write("<li>" + elem3[x].text + "</li>")
            print(elem3[x].text)
        text_file.write("</ul></body></html>")

        text_file.close()

        #driver.execute_script("window.open('file:///home/vxv/PycharmProjects/tm470_Project/page_content_summary.html')")
        driver.switch_to.new_window()
        driver.get('file:///home/vxv/PycharmProjects/tm470_Project/page_content_summary.html')
    except:
        print('could not download page source')


# NEW PROFILE CREATION FUNCTION
def new_profile():
    global profileString

    # PRINT ALL INFO ON NEW PROFILE
    print("The text colour for this profile is: ", text_colour_preference)
    print("The background colour for this profile is: ", background_colour_preference)
    print("The Javascript preference for this profile is set to: ", javascript_on)
    print("The page images preference for this profile is set to: ", images_on)
    print("The ads preference for this profile is set to: ", ads_on)
    # GET NAME OF NEW PROFILE
    profileName = profileString.get()
    print("The profile name here is: ", profileName)

    if profileName:
        new_profile_doc = {
            "username": "test_user",
            "profile_name": profileName,
            "text_colour_preference": text_colour_preference,
            "background_colour_preference": background_colour_preference,
            "javascript_on": javascript_on,
            "images_on": images_on,
            "ads_on": ads_on
        }
        dbfile.u_settings_collection.insert_one(new_profile_doc)

        msg = f'Your profile: {profileName} has been saved.'

        showinfo(
            title='Information',
            message=msg
        )
    else:
        msg = 'Please enter a profile name to save a new profile'

        showinfo(
            title='Information',
            message=msg
        )

# GUI SETUP
window = tk.Tk()

window.geometry('500x800')
window.resizable(True, True)
window.title('TM470 application test')

# TAB DISPLAY SETUP
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Controls')
tabControl.add(tab2, text='Settings')
tabControl.pack(expand=1, fill="both")

# SET INITIAL THEME
style = ThemedStyle(window)
style.theme_use('radiance')
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

# SUMMARISE MAIN PAGE CONTENT
summariseButton = ttk.Button(tab1, text="Summarise page", command=summarise_page)
summariseButton.pack(fill='x', expand=True, pady=8)

# REMOVE IMAGES
disableImagesButton = ttk.Button(tab1, text="Toggle page images On/Off", command=toggle_images)
disableImagesButton.pack(fill='x', expand=True, pady=8)

# CHANGE BACKGROUND COLOURS
changeBackgroundButton = ttk.Button(tab1, text="Change Background colour", command=change_bg_colour)
changeBackgroundButton.pack(fill='x', expand=True, pady=8)

# BLOCK ADVERTS
blockAdsButton = ttk.Button(tab1, text="Block Adverts", command=block_adverts)
blockAdsButton.pack(fill='x', expand=True, pady=8)


#PROFILE SETTINGS
#DROPDOWN FOR THEME DISPLAY
profileString = tk.StringVar()

value_in = tk.StringVar(window)
value_in.set("Select a profile")

# profile_menu = tk.OptionMenu(window, value_in, *profiles_list)
# profile_menu.pack(fill='x', expand=True, pady=8)

profile_menu_two = ttk.Combobox(window, textvariable=value_in, values=profiles_list, state='readonly')
profile_menu_two.pack(fill='x', expand=True, pady=8)

def change_values(*args):
    print(value_in.get())
    global user_settings
    val = value_in.get()
    profile_selected(val)

value_in.trace('w', change_values)


# PROFILE SELECITON SCRIPT
# TODO: refactor preferences so we do not store them in strings and so that we are not repeating ourselves below.
def profile_selected(profile_name):
    global user_settings
    global initialised
    initialised = False
    user_settings = dbfile.u_settings_collection.find_one({"profile_name": profile_name})
    print(user_settings)

    global text_colour_preference
    global background_colour_preference
    global javascript_on
    global images_on
    global ads_on

    text_colour_preference = user_settings['text_colour_preference']
    background_colour_preference = user_settings['background_colour_preference']
    javascript_on = user_settings['javascript_on']
    images_on = user_settings['images_on']
    ads_on = user_settings['ads_on']


    #initialised = True
    startup_init_jsimgs()
    if not ads_on:
        block_adverts()
    #startup_init_colorise()


#SET NEW PROFILE
# PROFILE ENTRY INFO
newProfileLabel = ttk.Label(tab1, text="New Profile: ")
newProfileLabel.pack(fill='x', expand=False)

profileNameEntry = ttk.Entry(tab1, textvariable=profileString)
profileNameEntry.pack(fill='x', expand=False)
profileNameEntry.focus()

# PROFILE SET BUTTON
setProfileButton = ttk.Button(tab1, text="Set New Profile", command=new_profile)
setProfileButton.pack(fill='x', expand=False, pady=8)


#TAB 2 ====!!!!====
textColourLabel = ttk.Label(tab2, text="Text colour preference: " + text_colour_preference, foreground=text_colour_preference)
textColourLabel.pack(fill='x', expand=True)
backgroundColourLabel = ttk.Label(tab2, text="Background colour preference: " + background_colour_preference, foreground=background_colour_preference)
backgroundColourLabel.pack(fill='x', expand=True)


if (javascript_on):
    jsp = "JavaScript ON"
else:
    jsp = "JavaScript OFF"

javascriptPreferenceLabel = ttk.Label(tab2, text="JavaScript on/off preference: " + jsp)
javascriptPreferenceLabel.pack(fill='x', expand=True)


if (images_on):
    pip = "Image display ON"
else:
    pip = "Image display OFF"

imagesPreferenceLabel = ttk.Label(tab2, text="Page images preference: " + pip)
imagesPreferenceLabel.pack(fill='x', expand=True)

if (ads_on):
    sap = "Adverts ON"
else:
    sap = "Adverts OFF"

adsPreferenceLabel = ttk.Label(tab2, text="Ad display preference: " + sap)
adsPreferenceLabel.pack(fill='x', expand=True)


options = Options()

def chrome_options_set():

    global javascript_on
    global images_on

    if javascript_on:
        options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 1})
    else:
        options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})

    if not images_on:
        options.add_argument('--blink-settings=imagesEnabled=false')
    else:
        options.add_argument('--blink-settings=imagesEnabled=true')

# desk path
PATH = "/home/vxv/chromedriver"

# mac path
#PATH = "/Applications/chromedriver"

print(f"Initialised value before init is {initialised}")
startup_init_jsimgs()

driver = webdriver.Chrome(
    executable_path=PATH,
    options=options
)

window.mainloop()
