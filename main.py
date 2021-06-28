import time
import cv2
import pyautogui
import numpy as np
import keyboard

from target_finder import target_finder

#pause functions
is_paused = True
located = False

if __name__ == "__main__":
    region = (1061, 447, 759, 533)
    im = pyautogui.screenshot('images/region.png', region=region)
    print('Region loaded (check its accurate in images/region.png')
    print('start the bot by pressing s, stop the bot by pressing q')
    while keyboard.is_pressed('s') == False:
        time.sleep(0.1)

    while keyboard.is_pressed('q') == False:
        im = pyautogui.screenshot(region=region)
        im = np.array(im)
        pairs = target_finder(im)
        if pairs is not None:
            for pair in pairs:
                print(pair)
                x, y = pair
                pyautogui.click(x=x+region[0], y=y+region[1])

