from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

#Accesar o site DemoQA
browser.get("https://demoqa.com/")
browser.maximize_window()

#Escolher a opção Alerts, Frame & Windows na página inicial
lista_btn = browser.find_elements("class name", "category-cards")

for btn_alerts in lista_btn:
    if "Alerts, Frame & Windows" in btn_alerts.text:
        btn_alerts.click()
        break

browser.execute_script("document.body.style.zoom='60%'")
time.sleep(1)

#Mesmo selecionando todos os itens da lista, tentar identificar por nome ou ID o selenium não clica no submenu
submenulist = browser.find_elements("class name","menu-list")
for menubtn in submenulist:
    if "Browser Windows" in menubtn.text:
        menubtn.click()
        time.sleep(10)
        break

new_window_btn = browser.find_element("css selector","#windowButton")
new_window_btn.click()

#validar nova janela

newWindow = browser.window_handles[1]
browser.switch_to.window(newWindow)

validarMensagem = browser.find_element("id","sampleHeading")
conteudoMensagem = validarMensagem.text
if conteudoMensagem in "This is a sample page":
    print("Mensagem ok")
else:
    print("Mensagem não encontrada, verificar")
browser.close()

time.sleep(10)