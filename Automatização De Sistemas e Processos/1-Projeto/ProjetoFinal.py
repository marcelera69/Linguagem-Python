import pyautogui
import pandas as pd
import pyperclip
import time


# PARTE 1
pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.write(
    "file:///C:/Users/Ceelo/OneDrive/Documentos/Python/Intensiv%C3%A3o%20de%20python/teste/index.html"
)
pyautogui.press("enter")
pyautogui.hotkey("win", "up")
time.sleep(0.5)
pyautogui.click(x=161, y=122)
pyautogui.write("Marcelera69")
pyautogui.click(x=127, y=142)
pyautogui.write("Vicini123")
pyautogui.click(x=39, y=166)
time.sleep(2)
pyautogui.click(x=446, y=132)
pyautogui.write("compras.csv")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.click(x=1000, y=342)
pyautogui.click(x=1707, y=342)


# PARTE 2
time.sleep(4)
pyautogui.click(x=1896, y=12)
compras_df = pd.read_csv("compras.csv", sep=";")
print(compras_df)
print("============================================================================")
print(compras_df.describe())
print("============================================================================")
totalVendas = compras_df["ValorFinal"].sum()
vendaAlta = compras_df["ValorFinal"].std()
vendaBaixa = compras_df["ValorFinal"].min()
mediaQtd = compras_df["Quantidade"].mean()


# PARTE 3
pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("chrome")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.hotkey("win", "up")
time.sleep(0.5)
pyautogui.hotkey("ctrl", "shift", "n")
time.sleep(0.5)
pyautogui.write("https://www.google.com/intl/pt-BR/gmail/about/")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=1420, y=141)
time.sleep(4)
pyautogui.write("ceeloalves.curso@gmail.com")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("vicini123")
pyautogui.press("enter")
pyautogui.click(x=826, y=837)
time.sleep(4)
pyautogui.click(x=37, y=195)
time.sleep(1)
pyautogui.write("simonesoaresdoamaral@gmail.com")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.write("Teste automação 1")
pyautogui.press("tab")
time.sleep(0.5)
texto = f"""Bom dia Sr. Presidente, segue as informações do dia: 
Total de vendas:R${totalVendas:.2f}
O valor da venda mais alta foi: R${vendaAlta:.2f}
O valor da venda mais baixa foi: R${vendaBaixa:.2f}
A quantidade média de produtos vendidos por compra foram de: {mediaQtd:.2f}
"""
pyperclip.copy(texto)
pyautogui.hotkey("Ctrl", "v")
pyautogui.click(x=1319, y=1008)


# PARTE 4 / fechar tudo
time.sleep(1)
pyautogui.click(x=1906, y=13)
time.sleep(0.5)
pyautogui.click(x=1906, y=13)
