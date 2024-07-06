# opencv 图片
import requests
import base64
import cv2 as cv
import time
from PyQt5.QtCore import QThread
def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    params = {"image": base64_image}
    access_token = '24.aee256274291700b66f9d60e5a73bdd6.2592000.1722738525.282335-90002984'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    
    response = requests.post(request_url, data=params, headers=headers)
    start_time = time.time()
    elapsed_time = (time.time() - start_time) * 1000
    time_to_wait = 500 - elapsed_time
    if time_to_wait > 0:
        QThread.msleep(int(time_to_wait))
    num = 0
    if response:
        data = response.json()
        # 检查响应中是否包含 'vehicle_num' 和 'vehicle_info' 键
        if 'vehicle_num' in data and 'vehicle_info' in data:
            num = data['vehicle_num']['car']
            for item in data['vehicle_info']:
                location = item['location']
                x1 = location['left']
                y1 = location['top']
                x2 = x1 + location['width']
                y2 = y1 + location['height']
                cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # 定义要绘制的文字
                text = item['type']
                position = (x1, y1 - 2)
                font = cv.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                color = (0, 255, 255) 
                thickness = 2
                img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
        else:
            print("Unexpected response format: ", data)
    return img, num


