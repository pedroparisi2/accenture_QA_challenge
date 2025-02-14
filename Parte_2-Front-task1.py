from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
import time

browser = webdriver.Chrome()

#Accesar o site DemoQA
browser.get("https://demoqa.com/")
browser.maximize_window()

#Escolher a opção Forms na página inicial
lista_btn = browser.find_elements("class name", "category-cards")
for btn_forms in lista_btn:
    if "Forms" in btn_forms.text:
        btn_forms.click()
        break

#Escolher o submenu Practice Form
lista_btn2 = browser.find_elements("class name", "header-text")
for lista_form in lista_btn2:
    if "Forms" in lista_form.text:
        lista_form.click()
        break

time.sleep(1)

lista_btn3 = browser.find_elements("class name", "menu-list")
for practice_form_btn in lista_btn3:
    if "Practice Form" in practice_form_btn.text:
        practice_form_btn.click() 
        break 
time.sleep(1)    

#diminuindo o zoom da pagina para não ter problema com pop up de AD 
browser.execute_script("document.body.style.zoom='60%'")

#Preencher formulario
first_name = browser.find_element("id","firstName")
first_name.send_keys("Ulisses")

last_name = browser.find_element("id","lastName")
last_name.send_keys("Godoy")

email = browser.find_element("id","userEmail")
email.send_keys("ulisses_god@bol.com.br")

time.sleep(1) #instavel pelo ad que aparece no rodapé da pagina
waitgender = WebDriverWait(browser,10).until(EC.element_to_be_clickable(("css selector", "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)")))
genderbtn = browser.find_element("css selector", "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)")
genderbtn.click() 

mobile_num = browser.find_element("id","userNumber")
mobile_num.send_keys("11987654321")
mobile_num.send_keys(Keys.PAGE_DOWN)

time.sleep(1)
subjects = browser.find_element("id","subjectsInput")
subjects.click()
subjects.send_keys("Computer")
subjects.send_keys(Keys.TAB)

time.sleep(1)
hobbies = browser.find_element("css selector", "#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)")
hobbies.click()

address = browser.find_element("id","currentAddress")
address.send_keys("Rua generica 1000, são paulo")

#upload do arquivo txt - **colocar o arquivo no C:\\temp

#unico jeito de clicar no botão foi por xpath da div 
select_pic = browser.find_element("xpath",'//*[@id="userForm"]/div[8]/div[2]/div/label')
select_pic.click()
time.sleep(2) #esperar a tela do windows carregar

keyboard = Controller()
keyboard.type("C:\\Temp\\Teste.txt") 
time.sleep(1)
keyboard.press(Key.enter)
time.sleep(1)

state = browser.find_element("xpath",'//*[@id="react-select-3-input"]')
state.send_keys("NCR")
state.send_keys(Keys.TAB)

time.sleep(1)
city = browser.find_element("xpath",'//*[@id="react-select-4-input"]')
city.send_keys("Noida")
city.send_keys(Keys.ENTER)
time.sleep(1)

submitbtn = browser.find_element("id", "submit")
submitbtn.click()

#validação do pop up

validacao_msg_sucesso = browser.find_elements("id","example-modal-sizes-title-lg")
for msgsucesso in validacao_msg_sucesso:
    if "Thanks for submitting the form" in msgsucesso.text:
        print("Form validado com sucesso!")
        closebtn = browser.find_element("id","closeLargeModal")
        closebtn.click()
        time.sleep(2)
        break  
    else: 
        print("Erro! Favor revisar")
        break

time.sleep(10)



