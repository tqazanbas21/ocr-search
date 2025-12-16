import os
import keyboard
import io
import pyautogui
from ppadb.client import Client as AdbClient
from PIL import Image


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'THE CREDENTIALS HERE'
client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]
screenshot = device.screencap()
name = ''
image = ''



with open(r"C:\Users\moneyshop\Desktop\operation\counter.txt", "+r") as counter:
    name = str(int(counter.read()) + 1)
    image = Image.open(io.BytesIO(screenshot))
    counter.truncate()
    counter.seek(0)
    counter.write(name)


pos = (0, 250, image.size[0], image.size[1] - 300)

image = image.crop(pos)
image.save(f"{name.replace('.jpg', '')}_cropped.png")

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

    return texts[0].description.split()


req = detect_text(f"{name.replace('.jpg', '')}_cropped.png")
req2 = ' '.join(req) 

chat_gpt_pos = (442, 552)
enter_pos = (837, 978)
mouse_pos = (1281, 1005)
pyautogui.moveTo(chat_gpt_pos)
pyautogui.click()
keyboard.write(req2)
pyautogui.hotkey('ctrl', 'enter')
pyautogui.moveTo(mouse_pos)
pyautogui.click()
pyautogui.press('up')
