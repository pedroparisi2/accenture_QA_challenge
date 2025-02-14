from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import Select
import time
import random

browser = webdriver.Chrome()

#Accesar o site DemoQA
browser.get("https://demoqa.com/")
browser.maximize_window()

#Escolher a opção Alerts, Frame & Windows na página inicial
lista_btn = browser.find_elements("class name", "category-cards")

for btn_elements in lista_btn:
    if "Widgets" in btn_elements.text:
        btn_elements.click()
        break

#**Workaround
browser.execute_script("window.open('https://demoqa.com/progress-bar', '_blank')")
browser.switch_to.window(browser.window_handles[1])
browser.maximize_window()
browser.execute_script("document.body.style.zoom='60%'")

starStoptbtn = browser.find_element("id","startStopButton")
starStoptbtn.click()

#parar antes dos 25% e verificar
time.sleep(1)
progressBar = browser.find_element("id","progressBar")
percentage = progressBar.get_property('innerText')
numChar = len(percentage)
percentageFormatada = percentage[:numChar-1]
intPercentageFormatada = int(percentageFormatada)
print (percentageFormatada)
if intPercentageFormatada < 25:
    starStoptbtn.click()
time.sleep(1)

#iniciar novamente esperar chegar aos 100% verificar e resetar
starStoptbtn.click()
progressBar = browser.find_element("id","progressBar")
percentage = progressBar.get_property('innerText')
numChar = len(percentage)
percentageFormatada = percentage[:numChar-1]
intPercentageFormatada = int(percentageFormatada)
timeout = 0
while intPercentageFormatada != 100:
    progressBar = browser.find_element("id","progressBar")
    percentage = progressBar.get_property('innerText')
    numChar = len(percentage)
    percentageFormatada = percentage[:numChar-1]
    intPercentageFormatada = int(percentageFormatada)
    time.sleep(1)
    if timeout == 90:
        break
    else: 
        timeout = timeout+1

print (intPercentageFormatada)
time.sleep(1)

resetbtn = browser.find_element("id","resetButton")
resetbtn.click()
time.sleep(1)
progressBar = browser.find_element("id","progressBar")
percentage = progressBar.get_property('innerText')
numChar = len(percentage)
percentageFormatada = percentage[:numChar-1]
intPercentageFormatada = int(percentageFormatada)
if intPercentageFormatada == 0:
    print ("Teste realizado com sucesso")    
else:   
    print ("Teste falhou, verificar")




