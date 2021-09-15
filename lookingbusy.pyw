import pyautogui,time
time.sleep(1)
t = 10
try:
    while True:
        time.sleep(10)
        pyautogui.moveRel(0,t)
        pyautogui.keyDown("ctrl")
        pyautogui.keyUp("ctrl")
        t *= -1
except KeyboardInterrupt:
    print("\nDone")
