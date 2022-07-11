import pyautogui as pa
import time

# abrir a ferramenta/ o sistema/ o programa
pa.PAUSE = 2
pa.press("win")
pa.write("login.xlsx")
pa.press("backspace")
pa.press("enter")
time.sleep(5)
# descobrir a posição do login
# time.sleep(3)
# print(pa.position()) # mostra a posição do mouse em pixels

# preencher o login
pa.click(x=419, y=210) # clicando no login
pa.write("Usuario")

# preencher a senha
pa.click(x=429, y=260) # clicando na senha
pa.write("123")

# clicar em fazer login
pa.click(x=401, y=385)

# clicar em voltar
time.sleep(5)
pa.click(x=518, y=525)