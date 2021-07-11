import cv2
import numpy as np
from scipy import ndimage
import time
import pyautogui
import config

target_color = (255, 219, 195)
target_gray_color = 227
img_width = config.game_window[2]

def target_finder_naive(cur):
    """
    naive implementation of target finder.
    input: numpy array, grayscale image
    output: [(x,y)], single pixel that matches the color of an inner target bullseye
    """
    ys, xs = np.where(cur == target_gray_color)
    if len(xs) == 0:
        return None
    x = xs[0]
    y = ys[0]

    return [(x, y)]

def target_finder_difference(prev, cur):
    """

    """
    prev[prev != target_gray_color] = 0
    cur[cur != target_gray_color] = 0
    prev[(prev - cur) < 10] = 0
    ys, xs = np.where(prev == target_gray_color)
    if len(xs) == 0:
        return None
    x = xs[0]
    y = ys[0]

    return [(x, y)]

def target_finder_islands(cur):
    cur[cur != target_gray_color] = 0
    labeled_array, num_features = ndimage.label(cur)

    temp = []
    for val in range(1, num_features+1):
        loc = np.argmax(labeled_array == val)
        temp += [(loc % img_width, loc // img_width)]
    return temp

def find_colors():
    #grayscale color of center of target: 227
    #rgb color of center: (255, 219, 195)
    while 1:
        x, y = pyautogui.position()
        im = pyautogui.screenshot().convert('RGB')
        im = np.array(im)
        im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        px = im[y, x]
        print(px)
        time.sleep(1)

def show_single_target_analyze():
    img = cv2.imread('images/single_target.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img[img != target_gray_color] = 0
    cv2.imshow('image', img)
    cv2.waitKey(0)

def test_region():
    """
    made to test your chosen region to ensure the game is in the screen
    """
    prev = pyautogui.screenshot('images/prev_sample.png', region=config.game_window)
    time.sleep(0.01)
    cur = pyautogui.screenshot('images/cur_sample.png', region=config.game_window)

def test_differencing():
    """
    made to test image differencing from two consecutive screenshots
    """
    prev = cv2.cvtColor(cv2.imread('images/prev_sample.png'), cv2.COLOR_BGR2GRAY)
    cur = cv2.cvtColor(cv2.imread('images/cur_sample.png'), cv2.COLOR_BGR2GRAY)
    prev[prev != target_gray_color] = 0
    labeled_array, num_features = ndimage.label(prev, np.ones((3,3)))
    labeled_array = labeled_array.astype('uint8') * 20
    print(num_features)
    #cur[cur != target_gray_color] = 0
    #prev[(prev - cur) <= 0] = 0
    print(np.unique(labeled_array))
    cv2.imshow('diffed image', labeled_array)
    cv2.waitKey(0)

if __name__ == "__main__":
    #find_colors()
    #show_single_target_analyze()
    #target_finder(img)
    #test_region()
    test_differencing()
