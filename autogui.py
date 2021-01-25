import pyautogui as p


def exec():
    with open("log02.txt", "w") as file:
        p.hotkey('win', 'r')
        p.sleep(0.5)
        p.write('notepad')
        p.press('enter')
        p.sleep(0.5)
        p.write('Testestwsztst')
        p.hotkey('alt', 'f4')
        p.press('enter')
        file.write("--- Salvando...")
        p.sleep(1)
        janela = p.getActiveWindow()
        janela.maximize()
        Atual = p.locateOnScreen(r"C:\dev\RPA-Foms\desktop.png", confidence=0.8)
        pesqAtual = p.center(Atual)
        xAtal, yAtual = pesqAtual
        p.click(xAtal, yAtual)
        p.sleep(0.5)
        Input = p.locateOnScreen(r"C:\dev\RPA-Foms\input.png", confidence=0.8)
        pesqInput = p.center(Input)
        xInput, yInput = pesqInput
        p.click(xInput, yInput)
        p.sleep(0.5)
        file.write("--- Escrevendo...")
        p.write('teste')
        p.press('enter')
        file.close()