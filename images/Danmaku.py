# -*- coding:utf-8 -*-
import wx
from PIL import Image
from random import randint
from tkinter import Tk
from time import sleep
from sys import exit as esc
import urllib.request
import os

win =Tk()



#print(line)
class myframe(wx.Frame):
    def main():
        global name
        if not os.path.exists('images\\cache'):
                    os.makedirs('images\\cache')
                    path = "images\\cache\\"
                    url = "https://v1.jinrishici.com/all.png"
                    number = str(randint(1,142857))
                    name = path + number +'.png'
                #保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片
                    conn = urllib.request.urlopen(url)
                    f = open(name,'wb')
                    f.write(conn.read())
                    f.close()
                    print('Pic Saved!')
    def __init__(self): 
        global y1
        global x
        x=win.winfo_screenwidth()
        y=win.winfo_screenheight()
        super().__init__(parent=None,pos=wx.DefaultPosition,style=wx.FRAME_SHAPED|wx.FRAME_NO_TASKBAR, size=(x,y))
        img = Image.open(name)
        w = img.width       #图片的宽
        h = img.height      #图片的高
        #print(w)
        #print(h)
        self.bg = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)  # 悬浮框的图片 
        region = wx.Region(self.bg)
        self.SetShape(region)
        y1 = randint(0,win.winfo_screenheight())
        #print(y1)
        path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath()
        path.AddRectangle(20, y1, w, h)  # 通过自动调整图片长宽来找出合适的图片位置
        self.SetShape(path)
        self.SetToolTip("每天进步一点点:)")
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClickEvent)

        
        # 鼠标右键退出窗口
    def OnRightClickEvent(self, event):
        wx.Exit()
        
        # 绘制    
    def OnPaint(self,event):
        mydc=wx.PaintDC(self)
        mydc.DrawBitmap(self.bg,20,y1,True)
        x1 = randint(0,20)
        for i in range(0,x):
            pos = self.GetPosition()
            self.SetPosition((x1*i,pos.y))
            sleeptime=randint(0,100)
            sleeptime=sleeptime/1000
            #print(sleeptime)
            sleep(sleeptime)
            if pos.x>=x-100:
                esc()
            
        
        

        
myapp=wx.App()
frame=myframe()
frame.Show()
myapp.MainLoop()
