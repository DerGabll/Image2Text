import easyocr
import keyboard
import glob
import time
import os
import pyautogui

print("Loading EasyOCR model...")
reader = easyocr.Reader(['de'], gpu=False)
print("Model loaded!")

SCREENSHOT_PATH = r"C:\Users\Bob\Pictures\Screenshots"
if not os.path.exists(SCREENSHOT_PATH):
    print("ERROR: Du edi dein SCREENSHOT_PATH isch it richtig")
    quit()
SCREENSHOT_PATH += r"\*"

while True:
    print("\n=== READY TO READ IMAGE TEXT ===")
    keyboard.wait("r")
    time.sleep(0.1)

    screenshot_files = glob.glob(SCREENSHOT_PATH)
    if not screenshot_files:
        print("ERROR: No screenshots found!")
        continue

    latest_file = max(screenshot_files, key=os.path.getctime)
    print(f"Reading: {os.path.basename(latest_file)}")

    results = reader.readtext(latest_file, detail=0)
    words = ' '.join(results).strip()

    print("\n--- Extracted Text ---")
    print(words)
    print("----------------------")

    print("\nREADY TO LAUNCH")
    keyboard.wait("enter")
    pyautogui.write(words, interval=0.1)