import pyautogui
import keyboard
import threading
import time


clicking = False


def click_loop():
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(0.1)  
        else:
            time.sleep(0.1)


def toggle_clicking():
    global clicking
    while True:
        keyboard.wait('F6')  
        clicking = not clicking
        if clicking:
            print("▶️ Autoclicker ATIVADO")
        else:
            print("⏸️ Autoclicker DESATIVADO")
        time.sleep(0.5) 


threading.Thread(target=click_loop, daemon=True).start()
toggle_clicking() 

