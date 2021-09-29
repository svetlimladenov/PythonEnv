import wx;

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # init frame
        self.InitFrame()

    def InitFrame(self):
        frame = MyFrame(parent=None, title="My Frame", pos= (100, 100))
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()
    
    def OnInit(self):
        panel = MyPanel(parent=self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # add a hello message to the panel
        welcomeText = wx.StaticText(self, id=wx.ID_ANY, label="Hello World!!!", pos = (20, 20))
        # ID_ANY mean thath we don't care about the id


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
