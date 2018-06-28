import sys
sys.path.append('../')
from PyQt5.QtWidgets import QWidget
from ui import Ui_mainWidget
from data.imageList import imageList
from data.posList import posList
from .recognition import recognize
from .calauation import calc
from .regularcheck import re_check
import cv2

class mainWidget(QWidget,  Ui_mainWidget.Ui_Form):
    
    def __init__(self, parent = None):
        super(mainWidget, self).__init__(parent)
        self.setupUi(self)
        #self.basepoint = []
        self.imagelist = imageList()
        self.poslist = posList()
        self.finallist = []
        self.equation = []
        self.strlist = ""
        #self.paintWidget.value_changed.connect(self.get_result)
    
    def recognize(self):
        if(self.paintWidget.save_image() == False):
            return
        image = cv2.imread("tmp.png", 0)
        #切分字符
        if(self.imagelist.deivde_image(image) == False):
            return
        lineimage = self.imagelist.get_lineimage()
        #切割图像
        self.poslist.divide_pos(lineimage)
        #填充字符
        self.finallist = self.imagelist.set_position(self.poslist)
        #修改坐标
        #self.set_point(self.finallist)
        #识别
        #print(self.finallist)
        recognize(self.finallist)
        #得到算式
        #print(self.finallist)
        self.get_result()
        #设置标签
        #self.paintWidget.set_label(self.finallist)

    def get_result(self):
        self.equation.clear()
        for i in self.finallist:
            if(isinstance(i, dict)):
                self.equation.append(i["char"])
            else:
                self.equation.append(i)
        self.strlist = re_check(self.equation)#正则表达式检查
        self.textEdit.setPlainText(str(self.strlist))
                
    def clear_all(self):
        self.imagelist.clear()
        self.poslist.clear()
        self.paintWidget.clear()
        self.textEdit.clear()
        self.finallist.clear()
        self.equation.clear()
        self.strlist = ""
        
    def calculate(self):
        res = calc(self.strlist)
        if(res == "INPUT ERROR"):
            self.textEdit.setPlainText(str(self.strlist) + ": " + str(res))
        else:
            self.textEdit.setPlainText(str(self.strlist) + "=" + str(res))
        
        
