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
    if "Elements" in btn_elements.text:
        btn_elements.click()
        break

browser.execute_script("document.body.style.zoom='60%'")
time.sleep(1)

#Mesmo selecionando todos os itens da lista, tentar identificar por nome ou ID o selenium não clica no submenu
menulist = browser.find_elements("class name", "header-text")
for menubtn in menulist:
    if "Elements" in menubtn.text:
        menubtn.click()
        break

browser.execute_script("document.body.style.zoom='60%'")


submenulist = browser.find_elements("class name","menu-list")
for submenubtn in submenulist:
    if "Web Tables" in submenubtn.text:
        submenubtn.click()
        time.sleep(1)
        break

time.sleep(10)

#Adicionando 12 usuarios de maneira dinamica já automatizados, podemos usar uma base de dados aqui para pegarmos os valores. 
#Optei por criar randomicamente atraves de Id's unicos

add_button = browser.find_element("id","addNewRecordButton")

emaillist=[]
i = 0 
while i <= 11:    
    add_button.click()
    #buscar campos     
    first_name = browser.find_element("id","firstName")
    last_name = browser.find_element("id", "lastName")
    email = browser.find_element("css selector","#userEmail")
    age = browser.find_element("id", "age")
    salary = browser.find_element("id","salary")
    Department = browser.find_element("id","department")
    #inserir campos
    firstnameText = "User"
    first_name.send_keys(firstnameText)
    lastNameText = random.randrange(1000,9999)
    last_name.send_keys(str(lastNameText))
    emailText = firstnameText+str(lastNameText)+"@ig.com.br"
    email.send_keys(emailText)
    ageNumber = random.randrange(18,65)
    age.send_keys(str(ageNumber))
    salaryNumber = random.randrange(10000,20000)
    salary.send_keys(str(salaryNumber))
    Department.send_keys("TOSCA Automation")
    submit_button = browser.find_element("id","submit")
    submit_button.click()
    time.sleep(1)
    #estou criando uma lista com o email de cada user para identificação na hora de deletar
    #aqui pode ser qualquer campo que tenha identificador unico (user, etc)
    emaillist.append(emailText)
    i = i+1
    

#deletar os usuarios criados
y=0
k=4
while y < i:  
    pesquisaEmail = browser.find_element("id","searchBox")
    pesquisaEmail.send_keys(emaillist[y])
    botaoPesquisar = browser.find_element("css selector","#basic-addon2")
    botaoPesquisar.click()
    aspas = str('"')
    botaoDeletar = browser.find_element("css selector",'#delete-record-'+str(k))
    botaoDeletar.click()
    pesquisaEmail.clear()
    time.sleep(1)
    k=k+1
    y=y+1

time.sleep(10)




    



    

