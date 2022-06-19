# -*- coding:utf-8 -*-
import wx
import os
import urllib.request
import random
import time
import sys

class myframe(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,pos=wx.DefaultPosition,style=wx.FRAME_SHAPED|wx.FRAME_NO_TASKBAR, size=(150,150))

        self.bg = wx.Bitmap("images\\iconsmall.png", wx.BITMAP_TYPE_PNG)  # 石膏娘的图片 
        region = wx.Region(self.bg)
        self.SetShape(region)
        path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath()
        path.AddCircle(51, 51, 50)  # 圆形路径，参数x，y，r。通过调整坐标半径来找出合适的图片位置
        self.SetShape(path)
        self.SetToolTip("石膏娘ver1.0")
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClickEvent)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClickDown)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.ResetPosition)
        self.Bind(wx.EVT_ENTER_WINDOW, self.DisplayWindow)
       
        # 鼠标左键按下时控制台输出坐标,屏幕输出诗词弹幕     
    def OnLeftClickDown(self, event):
        #print('左键')
        '''global name'''
        self.pt = event.GetPosition()
        pos = self.GetPosition()
        print((pos.x,pos.y))
        print((-pos.x,-pos.y))
        '''if not os.path.exists('images\\cache'):
            os.makedirs('images\\cache')
        path = "images\\cache\\"
        url = "https://v1.jinrishici.com/all.png"
        number = str(random.randint(1,142857))
        name = path + number +'.png'
        #保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片
        conn = urllib.request.urlopen(url)
        f = open(name,'wb')
        f.write(conn.read())
        f.close()
        print('Pic Saved!') 
        full_path = 'images\\names.txt'  # 也可以创建一个.doc的word文档
        file = open(full_path, 'w')
        path = "cache\\"
        readname = path + str(number)+'.png'
        file.write(readname) 
        file.close() 
        os.popen('images\Danmaku.exe')'''
        


        
        # 鼠标右键退出窗口
    def OnRightClickEvent(self, event):
        wx.Exit()
        
        # 石膏娘拖拽
    def OnMouseMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = self.GetPosition()
            self.pt = event.GetPosition()
            pos = self.ClientToScreen(event.GetPosition())
            self.Move((pos.x-self.pt.x, pos.y-self.pt.y))
        
        # 绘制    
    def OnPaint(self,event):
        mydc=wx.PaintDC(self)
        mydc.DrawBitmap(self.bg,0,0,False)
        #检测状态和位置
        pos = self.GetPosition()
        
        # 离开石膏娘时贴边
    def ResetPosition(self, event):
        if event.LeftIsDown():
            pos = self.GetPosition()
        else:
            pos = self.GetPosition()
            if pos.y<=25:
                self.SetPosition((pos.x,-50))
            if pos.y>=700:
                self.SetPosition((pos.x,800))
            if pos.x<=0:
                self.SetPosition((-40,pos.y))
            if pos.x>=1425:
                self.SetPosition((1510,pos.y))
        
    	# 鼠标放在石膏娘上是弹出
    def DisplayWindow(self, event):
        pos = self.GetPosition()
        if -pos.y >= 0:
            pos = self.GetPosition()
            self.SetPosition((pos.x, 0))
        elif pos.y >=750:
            pos = self.GetPosition()
            self.SetPosition((pos.x, 750))
        elif -pos.x >=0:
            pos = self.GetPosition()
            self.SetPosition((0, pos.y))
        elif pos.x >=1425:
            pos = self.GetPosition()
            self.SetPosition((1425, pos.y))

myapp=wx.App()
frame=myframe()
frame.Show()
myapp.MainLoop()

