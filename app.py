# import cv2
import pyautogui
from time import sleep

while True:
    try:
        for i in range(1, 5):
            print("start in ", 5-i)
            sleep(1)
        # Refresh the screen
        print("Refresh screen")
        pyautogui.moveTo(85, 85)
        pyautogui.click()
        pyautogui.click()

        sleep(5)
        # Login to the game
        # click on the CONNECT WALLET button.
        print("Click CONNECT WALLET")
        pyautogui.moveTo(653, 577)
        sleep(1)
        pyautogui.click()

        # wait wallet to load
        print("wait wallet to load")
        sleep(10)

        # click Sign button Point(x=1345, y=594)
        print("click Sign button Point")
        pyautogui.moveTo(1181, 591)
        sleep(1)
        pyautogui.click()

        # wait game to load
        print("wait game to load 10 sec.")
        sleep(15)

        # go to Treasure hunt mode Point(x=749, y=435)
        print("go to Treasure hunt mode")
        pyautogui.moveTo(641, 413)
        pyautogui.click()

        # open heroes list.
        pyautogui.moveTo(656, 667, 1)  # move to arrowup
        sleep(1)
        pyautogui.click()
        sleep(1)
        pyautogui.click()

        # drag mouse to scroll to the bottom of list
        pyautogui.moveTo(659, 605, 1)  # move to bottom
        sleep(1)
        pyautogui.click()
        sleep(0.5)
        pyautogui.drag(0, -500, 1, button='left')

        # Point(x=665, y=625) wake button
        # wake all heroes
        pyautogui.moveTo(587, 594, 1)  # move to wake button
        for i in range(0, 12):
            sleep(1)
            pyautogui.click()

        # exit heroes list Point(x=1100, y=492)
        pyautogui.moveTo(1057, 430, 1)  # move to edge of winndow
        sleep(1)
        pyautogui.click()
        sleep(1)
        pyautogui.click()

        # do it every 30 minutes

        waitTime = 30
        for i in range(0, waitTime):
            print("wait ", waitTime-i, " minutes for run bot again.")
            sleep(60)

    except:
        print("error try again in 5 seconds")
        for i in range(0, 5):
            print(i-5)
