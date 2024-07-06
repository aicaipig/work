import cv2 as cv

cap = cv.VideoCapture(0)
# cap 设备状态
while cap.isOpened():
    # ret 是否读取成功
    # frame 一帧图片
    ret, frame = cap.read()
    # 图像转换(被转化的图片,转换模式)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if not ret:
        print("不能获取图片！")
        break
    # frame原照片
    # newframe = 美颜(frame)
    # 显示newframe

    # (窗口名称，图片)
    cv.imshow('img',frame)
    # 关闭判断
    if cv.waitKey(1) == ord('q'):
        break
    # # 释放摄像头资源
cap.release()
cv.destroyAllWindows()