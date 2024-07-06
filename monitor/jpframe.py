from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from monitor.jp import Ui_Dialog
from monitor.Video import Video
from PyQt5.QtCore import pyqtSignal

class sonMonitorDialog(QDialog):
    return_thread = pyqtSignal(Video)
    def __init__(self, video_thread):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.video_thread = video_thread
        self.video_thread.send.connect(self.showimg)
        self.video_thread.start()

        self.ui.w1Button.clicked.connect(self.has)
    
    def closeEvent(self, event):
        self.return_thread.emit(self.video_thread)
        super(sonMonitorDialog, self).closeEvent(event)


    def has():
        return
    
    def showimg(self, h, w, c, b, th_id):
        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        if th_id == 1 or th_id == 2:
            # 自动缩放
            width = self.ui.video2.width()
            height = self.ui.video2.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.video2.setPixmap(scale_pix)
            self.ui.label.setText("这是" + str(th_id) + "线程")



