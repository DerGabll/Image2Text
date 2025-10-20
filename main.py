import pytesseract
from PIL import Image
import keyboard
import glob
import time
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

SCREENSHOT_PATH = r"C:\Users\hudi\Pictures\Screenshots\*"

while True:
    print("READY TO READ IMAGE TEXT")
    keyboard.wait("r")
    time.sleep(0.1)
    screenshot_files = glob.glob(SCREENSHOT_PATH)

    latest_file = max(screenshot_files, key=os.path.getctime)

    image = Image.open(latest_file)

    words: str = pytesseract.image_to_string(image)
    words = words.replace('\n', ' ') 
    words = words.rstrip()
    print(words[:50])
    
    print("READY TO LAUNCH")
    keyboard.wait("enter")

    keyboard.write(words)
    print("DONE")
