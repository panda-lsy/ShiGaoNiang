import wx
from PIL import Image
import random
import tkinter

win = tkinter.Tk()

f = open("images/cache/names.txt","r")   #设置文件对象

line = f.readline()

f.close() #关闭文件
print(line)
class myframe(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,pos=wx.DefaultPosition,style=wx.FRAME_SHAPED|wx.FRAME_NO_TASKBAR, size=(150,150))
        img = Image.open(line)
        w = img.width       #图片的宽
        h = img.height      #图片的高
        x1 = random.randint(0,win.winfo_screenwidth())
        y1 = random.randint(0,win.winfo_screenheight())
        self.bg = wx.Bitmap(line, wx.BITMAP_TYPE_PNG)  # 悬浮球的图片 
        region = wx.Region(self.bg)
        self.SetShape(region)
        path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath()
        path.AddRectangle(20, 20, w, h)  # 通过自动调整图片长宽来找出合适的图片位置
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
        mydc.DrawBitmap(self.bg,0,0,True)
        
        

        
myapp=wx.App()
frame=myframe()
frame.Show()
myapp.MainLoop()
