from PySide6 import QtCore, QtWidgets, QtGui
import sys 
import cv2 as cv
import matplotlib.pyplot as plt

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        w = 1000
        h = 500

        self.img = cv.imread("resources/baboon.png")
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        self.saved_img = self.img.copy()

        self.img_label = QtWidgets.QLabel(self)
        pixmap = self.cvtToPixmap(self.img)
        self.img_label.setPixmap(pixmap)
        self.img_label.setScaledContents(True)
        self.img_label.resize(300, 300)
        self.img_label.move(w/2 - self.img_label.width()/2, h/2 - self.img_label.height()/2)
        self.img_label.show()
        
        self.cmb_color_space = QtWidgets.QComboBox(self)
        self.cmb_color_space.addItems(["RGB", "CMY", "HSV"])
        self.cmb_color_space.resize(100,25)
        self.cmb_color_space.move(w/2 - self.cmb_color_space.width()/2, 50)
        self.cmb_color_space.currentIndexChanged.connect(lambda: self.changeColorSpace(cmb=self.cmb_color_space, ckbA=self.ckb_compoentA, ckbB=self.ckb_compoentB, ckbC=self.ckb_compoentC, ))
        self.cmb_color_space.show()

        self.ckb_compoentA = QtWidgets.QCheckBox(self)
        self.ckb_compoentB = QtWidgets.QCheckBox(self)
        self.ckb_compoentC = QtWidgets.QCheckBox(self)

        self.ckb_compoentA.move(w/2 - 110, 450)
        self.ckb_compoentB.move(w/2 - 10, 450)
        self.ckb_compoentC.move(w/2 + 90, 450)

        self.ckb_compoentA.setChecked(True)
        self.ckb_compoentB.setChecked(True)
        self.ckb_compoentC.setChecked(True)

        self.ckb_compoentA.setText("R")
        self.ckb_compoentB.setText("G")
        self.ckb_compoentC.setText("B")

        self.ckb_compoentA.stateChanged.connect(self.updateChannels)
        self.ckb_compoentB.stateChanged.connect(self.updateChannels)
        self.ckb_compoentC.stateChanged.connect(self.updateChannels)
       
        self.resize(w, h)

    def changeColorSpace(self, cmb: QtWidgets.QComboBox, ckbA: QtWidgets.QCheckBox, ckbB: QtWidgets.QCheckBox, ckbC: QtWidgets.QCheckBox):
        if (cmb.currentText() == "RGB"):
            self.img = self.saved_img.copy()   

            ckbA.setText("R")
            ckbB.setText("G")
            ckbC.setText("B")
            ckbA.setChecked(True)
            ckbB.setChecked(True)
            ckbC.setChecked(True)

        elif (cmb.currentText() == "CMY"):
            self.img = 255 - self.saved_img

            ckbA.setText("C")
            ckbB.setText("M")
            ckbC.setText("Y")
            ckbA.setChecked(True)
            ckbB.setChecked(True)
            ckbC.setChecked(True)

        elif (cmb.currentText() == "HSV"):
            self.img = cv.cvtColor(self.saved_img, cv.COLOR_RGB2HSV)

            ckbA.setText("H")
            ckbB.setText("S")
            ckbC.setText("V")
            ckbA.setChecked(True)
            ckbB.setChecked(True)
            ckbC.setChecked(True)

        self.updateChannels()

    def cvtToPixmap(self, img):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QtGui.QImage(img.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(qimg)
    
    def updateChannels(self):
        self.channels = cv.split(self.img)
        print(self.channels)
        ch = list(self.channels)

        if not self.ckb_compoentA.isChecked():
            ch[0][:] = 0
        if not self.ckb_compoentB.isChecked():
            ch[1][:] = 0
        if not self.ckb_compoentC.isChecked():
            ch[2][:] = 0

        merged = cv.merge(ch)

        if self.cmb_color_space.currentText() == "HSV":
            merged = cv.cvtColor(merged, cv.COLOR_HSV2RGB)

        elif self.cmb_color_space.currentText() == "CMY":
            merged = 255 - merged

        pixmap = self.cvtToPixmap(merged)
        self.img_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())