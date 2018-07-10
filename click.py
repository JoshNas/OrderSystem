import pyautogui
import time

# moves to right hand table open position
pyautogui.moveTo(851, 721)

for i in range(500):
    # opens on rt
    pyautogui.click()

    # moves to rt auto fold position
    pyautogui.moveTo(804, 873, duration=1)
    pyautogui.click()

    # moves to left table 3bet
    pyautogui.moveTo(202, 719, duration=1)
    pyautogui.click()
    time.sleep(11)

    # opens on lt
    pyautogui.click()

    # moves to lt auto fold position
    pyautogui.moveTo(170, 867, duration=1)
    pyautogui.click()

    # moves to rt 3bet
    pyautogui.moveTo(851, 721, duration=1)
    pyautogui.click()
    time.sleep(11)
