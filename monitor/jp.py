# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore,  QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1199, 870)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 60, 1091, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.video2 = QtWidgets.QLabel(self.frame)
        self.video2.setGeometry(QtCore.QRect(0, 0, 1091, 581))
        self.video2.setObjectName("video2")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(50, 680, 141, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 141, 41))
        self.label.setObjectName("label")
        self.w1Button = QtWidgets.QPushButton(Dialog)
        self.w1Button.setGeometry(QtCore.QRect(1010, 690, 131, 41))
        self.w1Button.setObjectName("w1Button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.video2.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.w1Button.setText(_translate("Dialog", "PushButton"))
