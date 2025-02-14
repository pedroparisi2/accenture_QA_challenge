import requests
import time
import json

user = "Teste"
#"Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer."}
password = "Teste*1234"

#criar usuario

dataUser = {"userName": user,"password": password}
postUser = requests.post("https://demoqa.com/Account/v1/User", data=dataUser)
mensagemRetorno = postUser.text
mensagemRetornoFormatada = mensagemRetorno[11:47]
userId = mensagemRetornoFormatada
print (mensagemRetornoFormatada)

time.sleep(20)
#coletar user ID


#Gerar Token
dataToken = {"userName": user,"password": password}
postToken = requests.post("https://demoqa.com/Account/v1/GenerateToken", data=dataToken)
print (postToken.text)
mensagemRetorno = postToken.text
if mensagemRetorno.find('"status":"Success","result":"User authorized successfully."') == -1:
    print("Erro, verificar")
else:
    print("Token gerado com sucesso!")

time.sleep(5)

#Confirmar usuario
dataUserConfirmation = {"userName": user,"password": password}
postUserConfirmation = requests.post("https://demoqa.com/Account/v1/Authorized", data=dataUserConfirmation)
time.sleep(1)
mensagemRetorno = postUserConfirmation.text
if "true" in mensagemRetorno:
    print ("Usuário validado!")
else:
    print ("Erro, verificar")

#time.sleep(5)

#listar livros disponiveis
dataGetBooks = requests.get("https://demoqa.com/BookStore/v1/Books")
print(dataGetBooks.text)
mensagemRetorno = dataGetBooks.text
if mensagemRetorno.find('"isbn"') == -1:
    print("Erro, verificar")
else:
    print("Lista gerada com sucesso!")

time.sleep(5)

isbn1 = "9781449331818"
isbn2 = "9781449325862"

#alugar 2 livros de livre escolha 

#***Usuario não está autorizando reservar livro nem pelo site (code 1200), nem por aqui. Talvez seja alguma instabilidade
dataBooking = {"userId":'"'+userId+'"',"isbn":isbn1}
dataBooking2 = {"userId":'"'+userId+'"',"isbn":isbn2}
booking = requests.put("https://demoqa.com/BookStore/v1/Books/"+isbn1, dataBooking)
booking2 = requests.put("https://demoqa.com/BookStore/v1/Books/"+isbn2, dataBooking2)
print (booking.text)
time.sleep(5)


#mostrar usuario com os livros
userDetails = requests.get("https://demoqa.com/Account/v1/User/"+userId)
print (userDetails.text)

#deletar usuario
deleterUser = requests.delete("https://demoqa.com/Account/v1/User/"+userId)
print (deleterUser.text)



