# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from Ui_xshell import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import webbrowser
import time
import win32api
import win32con

'审查st字符串中是否都是二进制字符'  
def check_ip(st):  
    a=['1', '0', '2', '3', '4', '5', '6', '7', '8', '9', '.']       #创建一个列表，存放二进制字符  
    for x in st:           #对字符串st进行遍历  
        if x not in a:    #如果字符串st中的元素有不在a列表中的  
            return False #则返回错误  
    return True          #经过遍历，未返回错误，则返回正确
def check_port(st):  
    a=['1', '0', '2', '3', '4', '5', '6', '7', '8', '9']       #创建一个列表，存放二进制字符  
    for x in st:           #对字符串st进行遍历  
        if x not in a:    #如果字符串st中的元素有不在a列表中的  
            return False #则返回错误  
    return True          #经过遍历，未返回错误，则返回正确

def ip(ip, prot, n):
    prot=int(prot)
    n=int(n)
    ip='telnet://'+ip+':'
    end=[]
    nn=0
    while nn<n:
        end.append(ip+str(prot+nn))
        nn=nn+1
    return end
def key():
    win32api.keybd_event(0x0D,0,0,0)
    time.sleep(0.01)
    win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0x0D,0,0,0)
    time.sleep(0.01)
    win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0x10,0,0,0)
    time.sleep(0.01)
    win32api.keybd_event(0x10,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0x4E,0,0,0)
    win32api.keybd_event(0x4E,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0x4F,0,0,0)
    win32api.keybd_event(0x4F,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0x0D,0,0,0)
    time.sleep(0.01)
    win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(str)
    def on_ipadressText_textChanged(self, p0):
        if self.ipadressText.text() != ""  :
            if check_ip(self.ipadressText.text()):
                pass
            else:  
                self.ipadressText.setText(self.ipadressText.text()[:-1])   #将文本框内容的最后一个字符删掉  
    
    @pyqtSlot(str)
    def on_portText_textChanged(self, p0):
        if self.portText.text() != ""  :
            if check_port(self.portText.text()):
                if int(self.portText.text())>65535 or int(self.portText.text())<0:
                    self.portText.setText(self.portText.text()[:-1])
            else:  
                self.portText.setText(self.portText.text()[:-1])   #将文本框内容的最后一个字符删掉  
    
    @pyqtSlot(str)
    def on_NText_textChanged(self, p0):
        if self.NText.text() != ""  :
            if check_port(self.NText.text()):
                if int(self.NText.text())>200 or int(self.NText.text())<0:
                    self.NText.setText(self.NText.text()[:-1])
            else:  
                self.NText.setText(self.NText.text()[:-1])
    @pyqtSlot()
    def on_run_clicked(self):
        if self.NText.text() == "" or self.portText.text() == "" or self.ipadressText.text() == "" or self.tim.text() == "":
            QMessageBox.critical(self,"错误",    self.tr("输入不合法，请检查!"))
        else:
            iip=ip(self.ipadressText.text(), self.portText.text(),self.NText.text())
            for i in iip:
                webbrowser.open(i)
                time.sleep(float(self.tim.text()))
                if self.checkBox.isChecked():
                    key()
    @pyqtSlot(str)
    def on_tim_textChanged(self, p0):
        if self.tim.text() != ""  :
            if check_ip(self.tim.text()):
                pass
            else:  
                self.tim.setText(self.tim.text()[:-1])
                
    @pyqtSlot(str)
    def on_netText_textChanged(self, p0):
        net=self.netText.text().split('/')
        print(net)
        if len(net) <3:
            pass
        else:
            if ':' in net[2]:
                net=net[2].split(':')
                self.portText.setText(net[1])
                self.ipadressText.setText(net[0])
            else:
                self.ipadressText.setText(net[2])
                
if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     ui = MainWindow()
     ui.show()
     sys.exit(app.exec_())
    
   
