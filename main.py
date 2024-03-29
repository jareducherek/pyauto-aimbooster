import time
import cv2
import pyautogui
import win32api, win32con
import numpy as np
import keyboard
import config

from target_finder import target_finder_difference, target_finder_naive, target_finder_islands

#pause functions
is_paused = True
located = False

find_loc = target_finder_islands

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.06)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

if __name__ == "__main__":
    region = config.game_window
    im = pyautogui.screenshot('images/region.png', region=region)
    print('Region loaded (check its accurate in images/region.png')
    print('start the bot by pressing s, stop the bot by pressing q')
    while keyboard.is_pressed('s') == False:
        time.sleep(0.1)

    print('starting!')
    prev_frame = cv2.cvtColor(np.array(pyautogui.screenshot(region=region)), cv2.COLOR_RGB2GRAY)
    time.sleep(0.1)
    while keyboard.is_pressed('q') == False:
        cur_frame = cv2.cvtColor(np.array(pyautogui.screenshot(region=region)), cv2.COLOR_RGB2GRAY)
        pairs = find_loc(cur_frame)
        if len(pairs) == 0:
            continue
        for pair in pairs:
            x, y = pair
            click(x+region[0],y+region[1])
        prev_frame = cur_frame

