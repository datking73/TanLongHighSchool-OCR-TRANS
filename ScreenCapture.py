import sys
from tkinter import *
from PIL import Image, ImageGrab, ImageTk, Image
from PyQt5 import QtCore, QtGui, QtWidgets

class Snippy(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle('ScreenShot')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.15)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('red'), 1))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        image.save("Capture.jpg")
        print("Screen is captured!")

def showWindow():
    app = Tk()
    app.geometry("500x500")
    app.attributes("-topmost", True)
    app.title("Translate Screen")
    app.mainloop()

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Snippy()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())

    showWindow()
