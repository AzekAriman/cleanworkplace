import os

import requests
from requests.auth import HTTPDigestAuth
from PIL import Image
from ultralytics import YOLO
import io
import schedule
import time

camera = [0, 1, 2, 3, 9, 11, 12, 13, 14, 15]  # 1 , 2, 3, 9, 11, 12, 13, 14, 15
counter = [0] * len(camera)


def img_detection1(image):
    model = YOLO("../YOLO-Weights/best.pt")
    image = Image.open(io.BytesIO(image))
    results = model(image)
    boxes = results[0].boxes
    for box in boxes:
        cls = (int(box.cls))
        if cls == 2:
            return True
    return False


def get_image():
    params = {
        "keep_aspect_ratio": 1,
        "resolution": "640x480"
    }
    headers = {
        "Accept": "image/*"
    }
    for index, c in enumerate(camera):
        url = f"http://45.138.163.92:7502/cameras/{c}/image"
        username = "test"
        password = "Rtest3"

        response = requests.get(url, auth=HTTPDigestAuth(username, password), params=params, headers=headers)

        if response.status_code == 200:
            # Access the image content or save it to a file
            image_content = response.content

            # Create an image object from the binary data
            image = Image.open(io.BytesIO(image_content))

            # Create folder if not exists
            if img_detection1(image_content):
                counter[index] += 1
            else:
                counter[index] = 0
            if counter[index] == 3:
                counter[index] = 0
                if not os.path.exists(f'predictions/image_{c}'):
                    os.makedirs(f'predictions/image_{c}')
                # Save the image to a file with a unique name
                image.save(f"predictions/image_{c}/{int(time.time())}.jpg")
        else:
            print("Failed to access the image:", response.status_code)
    print(counter)
    time.sleep(120)

# # Запуск функции get_image каждые 3 минут
# schedule.every(1).minutes.do(get_image)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
