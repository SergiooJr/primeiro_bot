from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep

chromedrive_path = "C:/Users/jessi/Downloads/chromedriver_win32/chromedriver.exe" # caminho do chromedriver

webdrive = webdriver.Chrome(executable_path=chromedrive_path) # variavel que amarzena o PATH do chromedrive

sleep(2)

webdrive.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1657565493&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d1ef1bb96-2b2b-f0c4-a64b-21f24fec1b8e&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015") # link da página que queremos entrar

while len(webdrive.find_elements(By.ID, 'signup')) < 1: # esperando carregar a tela de login
    sleep(1)

login = webdrive.find_element(By.ID, 'i0116') # procurar pelo ID para preencher o login
login.send_keys("marisafaria67@hotmail.com") # escreve no login
sleep(2)
btn_proximo = webdrive.find_element(By.ID, 'idSIButton9').click() # procura pelo ID o botão, e clica nele

while len(webdrive.find_elements(By.ID, 'idA_PWD_ForgotPassword')) < 1: # esperando carregar a tela da senha
    sleep(1)

senha = webdrive.find_element(By.ID, 'i0118') # procurar pelo ID para preencher a senha
senha.send_keys("ma020320") # escreve na senha
sleep(2)

btn_entrar = webdrive.find_element(By.ID, 'idSIButton9').click() # procura pelo ID o botão, e clica nele 


naoConect = webdrive.find_element(By.ID, 'idBtn_Back').click()


sleep(60)

