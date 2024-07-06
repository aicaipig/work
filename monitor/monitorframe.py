from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QFileDialog, QPushButton,QLabel
from monitor.mfui import Ui_Dialog
from monitor.Video import Video
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis

from monitor.jpframe import sonMonitorDialog
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QRadioButton, QButtonGroup, QPushButton
from PyQt5.QtCore import Qt


class MonitorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # # 创建并启动视频线程
        # self.th1 = Video('data/vd1.mp4')  # 确保路径正确
        # self.th1.send.connect(self.showimg)
        # self.th1.start()
        
        self.video_thread_1 = Video('data/vd1.mp4')
        self.video_thread_2 = Video('data/vd2.mp4')

        self.video_thread_1.send.connect(self.showimg)
        self.video_thread_2.send.connect(self.showimg)

        self.ui.swButton_1.clicked.connect(self.switch_to_video_1)
        self.ui.swButton_2.clicked.connect(self.switch_to_video_2)


        self.current_video_thread = None
        self.switch_to_video_2()

        # 初始化图表
        self.chart = QChart()
        self.series = QLineSeries()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Number of Cars Over Time")

        # 设置纵坐标范围为0到20
        self.axisY = QValueAxis()
        self.axisY.setRange(0, 20)
        self.chart.setAxisY(self.axisY, self.series)
        
        # 设置横坐标范围
        self.axisX = QValueAxis()
        self.axisX.setRange(0, 100)
        self.chart.setAxisX(self.axisX, self.series)
        
        # 创建 QChartView 并添加到 QGroupBox 中
        self.chart_view = QChartView(self.chart)
        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)
        self.ui.groupBox.setLayout(layout)
        
        # 初始化数据
        self.data = []
        self.max_points = 100
        self.current_x = 0

        self.ui.screenshotButton.clicked.connect(self.take_screenshot)

        # self.ui.nwButton.clicked.connect(self.open_new_window)

        self.ui.video1.clicked.connect(self.changeframe)
    
    # def changeframe(self):
    #     self.current_video_thread.wait()
    #     self.sonframe = sonMonitorDialog(self.current_video_thread)
    #     self.sonframe.show()
    
    def changeframe(self):
        self.sonframe = sonMonitorDialog(self.current_video_thread)
        self.sonframe.return_thread.connect(self.handle_returned_thread)
        self.sonframe.show()
        self.close()

    def handle_returned_thread(self, video_thread):
        self.current_video_thread = video_thread
        self.current_video_thread.send.connect(self.showimg)
        self.current_video_thread.start()
        self.show()
        
    def update_chart(self, num):
        # 更新折线图
        if len(self.data) >= self.max_points:
            self.data.pop(0)  # 保持数据点数量不变
        self.data.append((self.current_x, num))
        self.current_x += 1
        
        # 更新 QLineSeries 数据
        self.series.clear()
        for point in self.data:
            self.series.append(point[0], point[1])
        
        # 更新 X 轴范围
        self.axisX.setRange(max(0, self.current_x - self.max_points), self.current_x)

    def showimg(self, h, w, c, b, th_id, num):
        image = QImage(b, w, h, w * c, QImage.Format_BGR888)
        if image.isNull():
            print("Error: Null image received")
            return
        pix = QPixmap.fromImage(image)
        if th_id == 1 or th_id==2:
            # 自动缩放
            width = self.ui.video1.width()
            height = self.ui.video1.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.video1.setPixmap(scale_pix)
            # str(num) 类型转换
            self.ui.carnum.setText(str(num))
            # 更新折线图
            self.update_chart(num)

    def take_screenshot(self):
        # 截图当前显示的图像
        pixmap = self.ui.video1.pixmap()
        if pixmap:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Screenshot", "", "PNG Files (*.png);;All Files (*)")
            if file_path:
                pixmap.save(file_path, "PNG")
    
    # def open_new_window(self):
    #     self.new_window = NewWindow()
    #     self.new_window.show()
    #     self.th1

    # def closeEvent(self, event):
    #     self.th1.stop()  # 停止视频线程
    #     super().closeEvent(event)

    def switch_to_video_1(self):
        print("Switching to video 1")
        if self.current_video_thread:
            self.current_video_thread.stop()
            self.current_video_thread.wait()
        self.current_video_thread = self.video_thread_1
        self.video_thread_1.start()

    def switch_to_video_2(self):
        print("Switching to video 2")
        if self.current_video_thread:
            self.current_video_thread.stop()
            self.current_video_thread.wait()
        self.current_video_thread = self.video_thread_2
        self.video_thread_2.start()

