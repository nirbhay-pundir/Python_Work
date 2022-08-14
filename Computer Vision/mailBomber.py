import os
from pprint import pprint
import selenium
import  time
import pyautogui as py
from os import system
from msedge.selenium_tools import Edge, EdgeOptions

mails = ['kbcresponse@setindia.com','livsupport@sonyliv.com','kbcmarathi@setindia.com','info@crm.sonyliv.com',
         'Kenichiro.Yoshida@jp.sony.com','nps@setindia.com','feedback.set@setindia.com','vrmhgs@hgsinteractive.com']


for i in range(10):
    options = EdgeOptions()
    options.use_chromium = True
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    path = 'edge91.exe'
    driver = Edge(path, options=options)

    for mail in mails:
        driver.get("https://www.guerrillamail.com/compose")
        py.click(300, 620)
        py.write(mail)
        py.click(300, 690)
        py.write('Bug in Sony LIV Play Along!!!')
        py.click(300,780)
        py.hotkey('ctrl','v')
        py.click(105, 545)
        py.click(300, 575)
        time.sleep(20)
    driver.close()



