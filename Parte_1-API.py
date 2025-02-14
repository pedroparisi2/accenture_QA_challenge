import requests
import time
import json

#criar usuario
urlUser = "https://demoqa.com/Account/v1/User"
dataUser = {
  "userName": "Pedro",
  "password": "senha123"
}
respostaUser = requests.post(urlUser, json=dataUser)
print (respostaUser.json)
fileUser = json.loads(respostaUser)
#coletando userID que é necessário para alugar o livro
UserID = (fileUser["userId"])

time.sleep(2)

#gerar token
urlToken ="https://demoqa.com/Account/v1/GenerateToken"
dataToken = {
  "userName": "Pedro",
  "password": "senha123"
}
respostaToken = requests.post(urlToken, json=dataToken)
print(respostaToken.json)

time.sleep(2)

#Checar criação do usuário

urlAuthorized = "https://demoqa.com/Account/v1/Authorized"
dataAuthorized = {
    "userName": "Pedro",
    "password": "senha123"
}
repostaAuthorized = requests.post(urlAuthorized, json=dataAuthorized)
print(repostaAuthorized.json)

time.sleep(2)

#listar livros disponiveis

urlBookList = "https://demoqa.com/BookStore/v1/Books"
BookList = requests.get(urlBookList)
respostaBookList = BookList.json()
print(respostaBookList.json)

#alugar 2 livros
urlUserBooking =  "https://demoqa.com/BookStore/v1/Books"
dataUserBooking1 = {
  "userId": UserID,
  "isbn": "string"
}
dataUserBooking2 ={
  "userId": UserID,
  "isbn": "string"
}
respostaUserBooking1 = requests.post(urlUserBooking, json=dataUserBooking1)
respostaUserBooking2 = requests.post(urlUserBooking, json=dataUserBooking2)
print (respostaUserBooking1.json)
print (respostaUserBooking2.json)

#mostrar informações do usuário
urlGetAllUserDetails = "https://demoqa.com/Account/v1/User/{UUID}"
getAllUserDetails = requests.get(urlGetAllUserDetails)
respostaAllUserDetails = getAllUserDetails.json()
print(respostaAllUserDetails.json)

#deletar user para poder rodar mais de uma vez 
DeleteUser = requests.delete(urlUser, data ={'UserId':UserID}) 
print(DeleteUser.json)

