import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

# passo 1: Abrir sistema da empresa
pyautogui.press("win")
pyautogui.write("opera gx")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# passo 2: Fazer login
pyautogui.click(x=999, y=458)
pyautogui.write("saopaulo852@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
time.sleep(3)

# passo 3: importar a base de produtos para cadastro
tabela = pd.read_csv("produtos.csv")

print(tabela)

# passo 4: cadastrar os produtos

for linha in tabela.index:
    pyautogui.click(x=987, y=302)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
         pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # enviar o cadastro
    # voltar para cima
    pyautogui.hotkey("ctrl", "home")