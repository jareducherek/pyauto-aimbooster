# pyauto-aimbooster
Using pyautogui to play aimbooster using a variety of techniques.
- naive method, just click a random pixel that matches bullseye color
- frame differencing, click a random pixel of a shrinking target
- island method, create bullseye mask and click random pixel from each bullseye present

## Installation instructions
- clone this repo
- navigate to this repo and install required packages
- anaconda instructions:
```
make create_environment
conda activate pyauto-aimbooster
make requirements
```
