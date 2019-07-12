"""
created on July 11, 2017.
@author: Risasi

"""

import wx

class Myclass(wx.Frame):
    def __init__(self, msg):
        wx.Frame.__init__(self, msg)

        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label = "Click", pos = (150, 300))
        self.textfield = wx.TextCtrl(self.panel)

if __name__== "__main__":
    app = wx.App()
    frame = Myclass(None)
    frame.Show()
    app.MainLoop()
    
