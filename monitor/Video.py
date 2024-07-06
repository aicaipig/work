from PyQt5.QtCore import QThread
import cv2 as cv
from PyQt5.QtCore import pyqtSignal
from ai.car import vehicle_detect
import time
# 重写run()方法: 线程执行的内容
# Thread的实例对象.start()  run()就会自动执行
class Video(QThread):
    send = pyqtSignal(int, int, int, bytes, int, int)

    def __init__(self, video_id):
        super().__init__()
        self.th_id = 0
        if video_id == 'data/vd1.mp4':
            self.th_id = 1
        if video_id == 'data/vd2.mp4':
            self.th_id = 2
        self.video_id = video_id
        self.dev = cv.VideoCapture(video_id)
        self.dev.open(video_id)
        self.running = False

    def run(self):
        print(self.video_id)
        self.running = True
        while self.running:
            ret, frame = self.dev.read()
            if not ret:
                print(f'No frame from {self.video_id}')
                break

            frame, num = vehicle_detect(frame)
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes, self.th_id, num)

    def stop(self):
        self.running = False
        self.wait()