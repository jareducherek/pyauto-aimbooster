import time
import cv2
import pyautogui
import win32api, win32con
import numpy as np
import keyboard

from target_finder import target_finder_frame_diff, target_finder

#pause functions
is_paused = True
located = False

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.06)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

if __name__ == "__main__":
    region = (1061, 447, 759, 533)
    im = pyautogui.screenshot('images/region.png', region=region)
    print('Region loaded (check its accurate in images/region.png')
    print('start the bot by pressing s, stop the bot by pressing q')
    while keyboard.is_pressed('s') == False:
        time.sleep(0.1)

    print('starting!')
    prev_frame = np.array(pyautogui.screenshot(region=region))
    time.sleep(0.1)
    while keyboard.is_pressed('q') == False:
        cur_frame = np.array(pyautogui.screenshot(region=region))
        pairs = target_finder(cur_frame)
        if pairs is not None:
            for pair in pairs:
                x, y = pair
                click(x+region[0],y+region[1])
                #pyautogui.click(x=x+region[0], y=y+region[1])
        #prev_frame = cur_frame

