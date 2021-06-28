import cv2
import numpy as np
import time
import pyautogui

target_color = (255, 219, 195)

def target_finder(img):
    ys, xs = np.where(img[:, :, 2] == target_color[2])
    if len(xs) == 0:
        return None
    x = xs[0]
    y = ys[0]

    return [(x, y)]

if __name__ == "__main__":
    img = cv2.imread('images/single_target.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #cv2.imshow('image',img)
    #cv2.waitKey(0)

    """
    while 1:
        x, y = pyautogui.position()
        im = pyautogui.screenshot()
        px = im.getpixel((x, y))
        print(px)
        time.sleep(1)
        """
    target_finder(img)
