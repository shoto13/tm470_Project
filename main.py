#TM470 Project

from selenium import webdriver
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# BROWSER SETUP
chrome_options = webdriver.ChromeOptions()
PATH = "/home/vxv/chromedriver"
driver = webdriver.Chrome(
    executable_path=PATH,
    chrome_options=chrome_options
)

driver.get('https://www.youtube.com')