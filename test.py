import pyautogui
import time

print("Starting in 5 seconds...")
time.sleep(5)

print("Screen Size:", pyautogui.size())
print("Mouse Position:", pyautogui.position())

pyautogui.moveTo(500, 300, duration=2)
pyautogui.click()
pyautogui.write("Hello from PyAutoGUI!", interval=0.1)