"""
created on July 11, 2017.
@author: Risasi
"""

import wx

def sayHello():
    print("Yes button got pressed ....")
    

app = wx.App()
win = wx.Frame(None, title = "My app", size = (400, 400))
panel1 = wx.Panel(win)
loadButton = wx.Button(panel1, label = 'Click', pos = (30,70))
loadButton.Bind(wx.EVT_BUTTON, sayHello)
win.Show()
app.MainLoop()
