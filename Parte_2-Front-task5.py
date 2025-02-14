from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()

#Accesar o site DemoQA
browser.get("https://demoqa.com/")
browser.maximize_window()

#Escolher a opção Alerts, Frame & Windows na página inicial
lista_btn = browser.find_elements("class name", "category-cards")

for btn_interactions in lista_btn:
    if "Interactions" in btn_interactions.text:
        btn_interactions.click()
        break

browser.execute_script("window.open('https://demoqa.com/sortable', '_blank')")
browser.switch_to.window(browser.window_handles[1])
browser.maximize_window()
#browser.execute_script("document.body.style.zoom='60%'")

time.sleep(5)
i = 0
j = 1
tableListItemProperty = "" 
while i < 4:    
    while tableListItemProperty != 'One':
        xpath = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
        tableListItem = browser.find_element("xpath",xpath)
        tableListItemProperty = tableListItem.get_property("innerText")
        print(tableListItemProperty)
        if tableListItemProperty != 'One':
            j = j+1
        else:
            if i == j-1:
               j = 1
               break
            else: 
                xpathdrag = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
                xpathdrop = '//*[@id="demo-tabpane-list"]/div/div['+str(i+1)+']'
                drag = browser.find_element("xpath",xpathdrag)
                drop = browser.find_element("xpath",xpathdrop)
                ActionChains(browser).drag_and_drop(drag, drop).perform()
                time.sleep(3)
                j = 1
                break
    i=i+1
    j = 1
    while tableListItemProperty != 'Two':
        xpath = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
        tableListItem = browser.find_element("xpath",xpath)
        tableListItemProperty = tableListItem.get_property("innerText")
        if tableListItemProperty != 'Two':
            j = j+1
        else:
            if i == j-1:
               j=1
               break
            else: 
                xpathdrag = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
                xpathdrop = '//*[@id="demo-tabpane-list"]/div/div['+str(i+1)+']'
                drag = browser.find_element("xpath",xpathdrag)
                drop = browser.find_element("xpath",xpathdrop)
                ActionChains(browser).drag_and_drop(drag, drop).perform()
                time.sleep(3)
                j = 1
                break
    i= i+1
    while tableListItemProperty != 'Three':    
        xpath = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
        tableListItem = browser.find_element("xpath",xpath)
        tableListItemProperty = tableListItem.get_property("innerText")
        if tableListItemProperty != 'Three':
            j = j+1
        else:
            if i == j-1:
               j = 1
               break
            else: 
                xpathdrag = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
                xpathdrop = '//*[@id="demo-tabpane-list"]/div/div['+str(i+1)+']'
                drag = browser.find_element("xpath",xpathdrag)
                drop = browser.find_element("xpath",xpathdrop)
                ActionChains(browser).drag_and_drop(drag, drop).perform()
                time.sleep(3)
                j = 1
                break
    i = i+1
    while tableListItemProperty != 'Four':    
        xpath = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
        tableListItem = browser.find_element("xpath",xpath)
        tableListItemProperty = tableListItem.get_property("innerText")
        if tableListItemProperty not in 'Four':
            j = j+1
        else:
            if i == j-1:
               j = 1
               break
            else: 
                xpathdrag = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
                xpathdrop = '//*[@id="demo-tabpane-list"]/div/div['+str(i+1)+']'
                drag = browser.find_element("xpath",xpathdrag)
                drop = browser.find_element("xpath",xpathdrop)
                ActionChains(browser).drag_and_drop(drag, drop).perform()
                time.sleep(3)
                j = 1
                break
    i = i+1
    while tableListItemProperty != 'Five':    
        xpath = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
        tableListItem = browser.find_element("xpath",xpath)
        tableListItemProperty = tableListItem.get_property("innerText")
        if tableListItemProperty != "Five":
            j = j+1
        else:
            if i == j-1:
               j = 1
               break
            else: 
                xpathdrag = '//*[@id="demo-tabpane-list"]/div/div['+str(j)+']'
                xpathdrop = '//*[@id="demo-tabpane-list"]/div/div['+str(i+1)+']'
                drag = browser.find_element("xpath",xpathdrag)
                drop = browser.find_element("xpath",xpathdrop)
                ActionChains(browser).drag_and_drop(drag, drop).perform()
                time.sleep(3)
                j = 1
                break

#não é necessario fazer do ultimo pois ele sempre estará na ultima posição quando os outros forem recolocados 

