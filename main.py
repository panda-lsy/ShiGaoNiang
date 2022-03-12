import wx

class myframe(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,pos=wx.DefaultPosition,style=wx.FRAME_SHAPED|wx.FRAME_NO_TASKBAR, size=(150,150))

        self.bg = wx.Bitmap("images/2.png", wx.BITMAP_TYPE_PNG)  # 石膏娘的图片 
        region = wx.Region(self.bg)
        self.SetShape(region)
        path = wx.GraphicsRenderer.GetDefaultRenderer().CreatePath()
        path.AddCircle(70, 68, 68)  # 圆形路径，参数x，y，r。通过调整坐标半径来找出合适的图片位置
        self.SetShape(path)
        self.SetToolTip("提示字符串")
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightClickEvent)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClickDown)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.ResetPosition)
        self.Bind(wx.EVT_ENTER_WINDOW, self.DisplayWindow)
       
        # 鼠标左键按下时获取位置
    def OnLeftClickDown(self, event):
        self.pt = event.GetPosition()
        
        # 鼠标右键退出窗口
    def OnRightClickEvent(self, event):
        wx.Exit()
        
        # 石膏娘拖拽
    def OnMouseMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = self.ClientToScreen(event.GetPosition())
            self.Move((pos.x-self.pt.x, pos.y-self.pt.y))
        
        # 绘制    
    def OnPaint(self,event):
        mydc=wx.PaintDC(self)
        mydc.DrawBitmap(self.bg,0,0,True)
        
        # 离开石膏娘时贴边
    def ResetPosition(self, event):
        if event.LeftIsDown():
            pos = self.ClientToScreen(event.GetPosition())
        else:
            pos = self.GetPosition()
        self.SetPosition((pos.x,-120))
        
    	# 鼠标放在石膏娘上是弹出
    def DisplayWindow(self, event):
        pos = self.GetPosition()
        self.SetPosition((pos.x, 0))
        
myapp=wx.App()
frame=myframe()
frame.Show()
myapp.MainLoop()
