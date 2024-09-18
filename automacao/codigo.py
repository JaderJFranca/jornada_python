# Cadastrar produtos: passo-a-passo
# Passo 1 - Entrar no sistema da empresa
# Passo 2 - Fazer login
# Passo 3 - Importar dados para cadastro
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir os cadastros até o fim da lista (loop)

# Importação de bibliotecas
import pyautogui
import pandas as pd
import time

# Passo 1

# abrir o navegador
pyautogui.press("win")
pyautogui.write("opera gx")
pyautogui.press("enter")

# entrar no link
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2

pyautogui.click(x=726, y=491) # selecionar o campo e-mail
pyautogui.write("pythonimpressionador@gmail.com") # escreve e-mail
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("senha1234") # escreve a senha
pyautogui.click(x=941, y=684) # clique no botão de login
time.sleep(3)

# Passo 3

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4 e 5

for linha in tabela.index:
    pyautogui.click(x=660, y=343) # clicar no campo de código
    codigo = tabela.loc[linha, "codigo"] # pegar da tabela o valor do campo que a gente quer preencher

    # preencher o campos

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
    pyautogui.press("enter") # cadastra o produto (clique no botão enviar)
    pyautogui.scroll(5000) # dar scroll de tudo pra cima