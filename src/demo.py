import wx;
from urllib import request
from urllib import parse # use to generate the query params

class MyApp(wx.App): # MyApp : wx.App - inheritance
    def __init__(self, title):
        super().__init__(clearSigInt=True) # call the wx.App constructor

        # init frame
        self.InitFrame(title) # self -> this

    def InitFrame(self, title):
        frame = MyFrame(parent=None, title=title, pos= (200, 200))
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos): #constructor (parent, title, pos)
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()
    
    def OnInit(self):
        panel = MyPanel(parent=self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # add a hello message to the panel
        wx.StaticText(self, id=wx.ID_ANY, label="Type Artist name: ", pos = (20, 20))
        # ID_ANY mean thath we don't care about the id

        self.inputBox = wx.TextCtrl(self, pos=(20, 50), size=(100, 20)) # set it as a field to the class 
        self.result = wx.StaticText(self, id=wx.ID_ANY, label="Data will be displayed here", pos=(20, 80))

        button = wx.Button(parent=self, label="Fetch Artist Data", pos = (20, 110))
        button.Bind(wx.EVT_BUTTON, self.onFetch)
    
    def onFetch(self, event):
        input = self.inputBox.GetValue()
        params = {"query": f'artist:{input}'}
        queryString = parse.urlencode(params)
        url = f'http://musicbrainz.org/ws/2/artist/?{queryString}'
        response = request.urlopen(url)
        data = response.read() # returns as bytes 
        html = data.decode("UTF-8") # turn the bytes to string
        artistName = self.getArtistName(html, "name")
        self.result.SetLabel(artistName)

    def getArtistName(self, html, property):
        print(html)
        left = html.find(f'<{property}>')
        right = html.find(f'</{property}>')
        artistName = html[left + len(property) + 2:right]
        return artistName
        

if __name__ == "__main__":
    app = MyApp("F97160")
    app.MainLoop()
