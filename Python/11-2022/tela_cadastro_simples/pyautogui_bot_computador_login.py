import pyautogui
import time

# cada linha de código será executado com diferença de 3 segundos
pyautogui.PAUSE = 3

# abrir a ferramenta/o sistema/o programa #
pyautogui.press("win")

# escrever o que buscar
pyautogui.write("login.xlsx")

# as vezes o arquivo não irá ser reconhecido de primeira, então vamos usar um macete
pyautogui.press("backspace")
pyautogui.press("enter")

# descobrir as posições em que deve clicar
# ----- time.sleep(5)
# ----- print(pyautogui.position())

# clicando para digitar o login
pyautogui.click(x=456, y=286)
pyautogui.write("NathanHlc")

# clicando para digitar a senha
pyautogui.click(x=460, y=330)
pyautogui.write("nathan321")

# clicando no botão login
pyautogui.click(x=350, y=422)
