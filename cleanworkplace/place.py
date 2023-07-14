from ultralytics import YOLO
import cv2
import math
import datetime
import os


def img_detection(path_x, count):
    model = YOLO("../YOLO-Weights/best.pt")
    classNames = ["clean", "person", "unclean"]
    # classNamesdigital = ["0", "1", "2"]
    img = cv2.imread(path_x)
    results = model(img)
    boxes = results[0].boxes
    for box in boxes:
        cls = int(box.cls[0])
        if cls == 2:
            print("+")
    # detections = {}  # Словарь для сохранения значений
    # for box in boxes:
    #     x1, y1, x2, y2 = box.xyxy[0]
    #     x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    #     print(x1, y1, x2, y2)
    #     conf = math.ceil((box.conf[0] * 100)) / 100
    #     cls = int(box.cls[0])
    #     class_name = classNames[cls]
    #     print(class_name)
    #     label = f'{class_name}{conf}'
    #     t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
    #     print(t_size)
    #     c2 = x1 + t_size[0], y1 - t_size[1] - 3
    #     detections[x1] = cls  # Добавляем значения в словарь
    #     if conf > 0.7:
    #         color = (0, 0, 0)
    #         if cls == 0:
    #             color = (145, 104, 255)
    #         cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
    #         cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)  # filled
    #         cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
    #         detections[x1] = cls  # Добавляем значения в словарь
    #
    # sorted_detections = sorted(detections.items(), key=lambda x: x[0])  # Сортировка словаря по ключу x1(координатам)
    #
    # for x1, class_name in sorted_detections:
    #     print(f'x1: {x1}, class_name: {class_name}')
    #
    # cv2.imshow("result", img)
    # while True:
    #     key = cv2.waitKey(1)
    #     if key == ord('1'):
    #         break
    #
    # cv2.destroyAllWindows()


img_detection('club/static/club/images/image2.jpg', 5)  # Пример использования с count = 10
