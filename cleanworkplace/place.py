import os
import traceback

import requests
from django.core.files import File
from django.utils import timezone
from requests.auth import HTTPDigestAuth
from PIL import Image
from ultralytics import YOLO
import io
import time
from club.models import *

camera = [0, 1, 2, 3, 9, 11, 12, 13, 14, 15]  # 1 , 2, 3, 9, 11, 12, 13, 14, 15
counter = [0]


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
    global counter
    while True:
        try:
            params = {
                "keep_aspect_ratio": 1,
                "resolution": "640x480"
            }
            headers = {
                "Accept": "image/*"
            }

            cameras = Camera.objects.all()
            count = Camera.objects.count()
            if len(counter) != count:
                counter = [0] * count

            for index, camera in enumerate(cameras):
                url = f"http://45.138.163.92:7502/cameras/{camera.ip}/image"
                username = "test"
                password = "Rtest3"

                response = requests.get(url, auth=HTTPDigestAuth(username, password), params=params, headers=headers)

                if response.status_code == 200:
                    # Access the image content or save it to a file
                    image_content = response.content

                    # Create an image object from the binary data
                    image = Image.open(io.BytesIO(image_content))
                    buffer = io.BytesIO()
                    image.save(buffer, format='JPEG')

                    # Create folder if not exists
                    if img_detection1(image_content):
                        counter[index] += 1
                    else:
                        counter[index] = 0
                    if counter[index] == 3:
                        counter[index] = 0
                        picture = Picture()

                        picture.photo = File(buffer, name=f'{camera.ip}_{time.time()}.jpg')
                        picture.camera = camera
                        picture.save()
                else:
                    print("Failed to access the image:", response.status_code)
            print(counter)
        except Exception as e:
            traceback.print_exc()
        time.sleep(150)


# # Запуск функции get_image каждые 3 минут
# schedule.every(1).minutes.do(get_image)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
