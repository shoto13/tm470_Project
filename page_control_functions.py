import main

# FLIP PAGE FUNCTION
def flip_page_180():
    try:
        elem1 = main.driver.find_element(main.By.CSS_SELECTOR, 'body')
        main.driver.execute_script("arguments[0].style.transform ='rotate(180deg)';", elem1)
        print('Found <%s> element with that class name!' % (elem1.tag_name))
    except:
        print('could not find that element')
