from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep

chromedrive_path = "C:/Users/jessi/Downloads/chromedriver_win32/chromedriver.exe" # caminho do chromedriver

webdrive = webdriver.Chrome(executable_path=chromedrive_path) # variavel que amarzena o PATH do chromedrive

sleep(2)

webdrive.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1657565493&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d1ef1bb96-2b2b-f0c4-a64b-21f24fec1b8e&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015") # link da página que queremos entrar
sleep(10)

login = webdrive.find_element(By.ID, 'i0116') # procurar pelo ID para preencher o login
login.send_keys("SeuEmail@outlook.com") # escreve no login
sleep(5)

btn_proximo = webdrive.find_element(By.ID, 'idSIButton9').click() # procura pelo ID o botão, e clica nele
sleep(15)

senha = webdrive.find_element(By.ID, 'i0118') # procurar pelo ID para preencher a senha
senha.send_keys("SuaSenha") # escreve na senha
sleep(5)

btn_entrar = webdrive.find_element(By.ID, 'idSIButton9').click() # procura pelo ID o botão, e clica nele 
sleep(60)

