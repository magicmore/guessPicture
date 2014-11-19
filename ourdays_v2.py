# -*- coding: cp936 -*-
import wx
from time import sleep
from answer import AnswerStr
from processData import RawData
from processData import ManageQuestionNumber

def AddLinearSpacer( boxsizer, pixelSpacing ) :
    """ A one-dimensional spacer for use with any BoxSizer """

    orientation = boxsizer.GetOrientation()
    if   (orientation == wx.HORIZONTAL) :
        boxsizer.Add( (pixelSpacing, 0) )

    elif (orientation == wx.VERTICAL) :
        boxsizer.Add( (0, pixelSpacing) )
        
class mainFrame(wx.Frame):
    recLocationDict = {2:[80, 260], 3:[80, 170, 260], 4:[80, 140, 200, 260], 5:[80, 125, 170, 215, 260]}
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Ourdays", size=(390, 700))
        self.MainPanel = wx.Panel(self, -1)
        self.MainPanel.BackgroundColour=(255,255,230)
        self.PicPanel = wx.Panel(self.MainPanel, -1)
        self.PicPanel.BackgroundColour=(200,240,200)
        self.QuestionPanel = wx.Panel(self.MainPanel, -1)
        self.QuestionPanel.BackgroundColour=(200,230,250)
        self.AnswerPanel = wx.Panel(self.MainPanel, -1)
        self.AnswerPanel.BackgroundColour=(200,240,200)
        self.ButtonPanel = wx.Panel(self.MainPanel, -1)
        self.ButtonPanel.BackgroundColour=(200,230,250)
        self.Show()
        self.Refresh()
        self.qNumber = ManageQuestionNumber().getQnumber()      
        self.initData()
        #imageTulips = wx.Image("Tulips.jpg", wx.BITMAP_TYPE_ANY)
        #imagePengui = wx.Image("Penguins.jpg", wx.BITMAP_TYPE_ANY)
        self.helpPic = wx.Image("./rawPic/help.png", wx.BITMAP_TYPE_ANY)
        self.markPic = wx.Image("./rawPic/mark.png", wx.BITMAP_TYPE_ANY)
        self.crossPic = wx.Image("./rawPic/cross.png", wx.BITMAP_TYPE_ANY)
        self.showPic = self.helpPic 
        #self.imageTulips = self.resize(imageTulips)
        #self.imagePengui = self.resize(imagePengui)
        #self.currentImage = self.imageTulips


        buttonSizer = wx.GridSizer(rows=3, cols=9, hgap=0, vgap=0)
        self.bt=[]
        for i in range(0, len(self.options)):
            #print self.options.decode('gbk')[i]
            self.bt.append(wx.ToggleButton(self.ButtonPanel, label=self.options[i], size=(30,30)))
            buttonSizer.Add(self.bt[i], 0, wx.ALL, 1)
            self.bt[i].Bind(wx.EVT_TOGGLEBUTTON, self.ChangeAnswer)
        self.ButtonPanel.SetSizer(buttonSizer)

        self.nextButton = wx.Button(self.QuestionPanel, label=">>>", size=(50,30), pos=(250,20))
        self.nextButton.Bind(wx.EVT_BUTTON, self.getNextSheet)
        self.nextButton.Disable()
        buttonSpaceSizer = wx.BoxSizer(wx.VERTICAL)
        buttonSpaceSizer.Add((0,20))
        buttonSpaceSizer.Add(self.ButtonPanel)
        buttonSpaceSizer.Add((0,20))
        self.ButtonPanel.Layout()
        
        topSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer.Add(self.PicPanel,proportion=6, flag=wx.EXPAND)
        topSizer.Add(self.QuestionPanel,proportion=1, flag=wx.EXPAND)
        topSizer.Add(self.AnswerPanel,proportion=1, flag=wx.EXPAND)
        topSizer.Add(buttonSpaceSizer,proportion=3, flag=wx.ALIGN_CENTER)
        
        #spaceBoxSizer = wx.BoxSizer(wx.VERTICAL)
        #spaceBoxSizer.Add((0,300))

        #points = question.GetFont().GetPointSize()
        #f = wx.Font(points+5,  wx.ROMAN, wx.ITALIC, wx.BOLD, True)
        
        self.MainPanel.SetSizer(topSizer)
        self.MainPanel.Layout()
        self.Layout()
        #self.DrawTopicPic(self.currentImage, 60,20)
        #self.DrawSeqRec(3, [80, 170, 260])
        
        #self.pointList = [80, 170, 260]
        #self.inputStr = "###"
        self.AnswerPanel.Bind(wx.EVT_PAINT, self.OnPaint)
        self.QuestionPanel.Bind(wx.EVT_PAINT, self.OnPaintQues)
        self.PicPanel.Bind(wx.EVT_PAINT, self.OnPaintMainPic)
    def getDataFromConfiguration(self):
        self.qInfo = RawData(self.qNumber).getInfo()
        self.options = self.qInfo['option'].strip('\n').decode('gbk')
        self.question = self.qInfo['question'].strip('\n').decode('gbk')
        self.answer = self.qInfo['answer'].strip('\n').decode('gbk')
        self.picName = self.qInfo['pic'].strip('\n').decode('gbk')
        self.recSum = len(self.answer)
        self.ChangeMainPic("./themePic/" + self.picName +'.jpg')
        self.answerSheet = AnswerStr(len(self.answer))
    def initData(self):
        #self.recSum = answerSum;
        #print self.qNumber
        self.getDataFromConfiguration()
        self.pointList = self.recLocationDict[self.recSum ]
        #print self.pointList
        self.answerSheet = AnswerStr(self.recSum )
        
        
        self.ChangeMainPic("./themePic/" + self.picName +'.jpg')
    def DrawTopicPic(self, image, x, y):
        dc = wx.ClientDC(self.PicPanel)
        #dc.DrawTopicPic(50, 60, 190, 60)
        #dc.DrawBitmap(wx.BitmapFromImage(image), 60,20, True)
        dc.DrawBitmap(wx.BitmapFromImage(image), x,y, True)
    def DrawRec(self, x, y, inputStr):
        dc = wx.PaintDC(self.AnswerPanel)
        dc.DrawRectangle(x, y, 30, 30)
        dc.DrawText(inputStr, x+10, y+10)
        dc.DrawBitmap(wx.BitmapFromImage(self.showPic), 300, 10, True)
    def OnPaint(self, evt):
        self.DrawSeqRec(self.recSum, self.pointList, self.answerSheet.getValue())
    def OnPaintQues(self, evt):
        dc = wx.PaintDC(self.QuestionPanel)
        dc.DrawText(self.question, 100, 25)
        #dc.Draw
    def OnPaintMainPic(self, evt):
        dc = wx.PaintDC(self.PicPanel)
        dc.DrawBitmap(wx.BitmapFromImage(self.currentImage), 60, 20, True)
    def ChangeMainPic(self, image):
        self.currentImage = self.resize(wx.Image(image, wx.BITMAP_TYPE_ANY))

    def resize(self, image):
        w = image.GetWidth()
        h = image.GetHeight()
        image2 = image.Scale(w/16*4, h/9*4)
        return image2
    def DrawSeqRec(self, recSum, pointList, inputStr):
        for i in range(0, recSum):
            self.DrawRec(pointList[i], 10, inputStr[i])
    def ChangeAnswer(self, evt):
        currentObj = evt.GetEventObject()
        currentState = currentObj.GetValue()
        if False == self.answerSheet.isLegal():
            currentObj.SetValue(False)
            #beep
        if True == currentState:
            self.answerSheet.appendNewStr(currentObj.GetLabel())
            userInput = self.answerSheet.getValue()
            if userInput.count('#') == 0:
                if self.answerSheet.getValue() == self.answer:
                    self.showPic = self.markPic
                    self.QuestionPanel.Refresh()
                    #wait some time then move to next
                    self.nextButton.Enable()
                else:
                    self.showPic = self.crossPic
                    #print "false"
        else:
            self.answerSheet.removeStr(currentObj.GetLabel())
        self.AnswerPanel.Refresh()
    def refreshButtion(self, optionLabel):
        i = 0
        for button in self.bt:
            button.SetValue(False)
            button.SetLabel(optionLabel[i])
            i+=1
    def getNextSheet(self, evt):
        self.showPic = self.helpPic
        self.qNumber += 1
        self.initData()
        self.refreshButtion(self.options)
        self.ButtonPanel.Refresh()
        self.QuestionPanel.Refresh()
        self.AnswerPanel.Refresh()
        self.PicPanel.Refresh()
if "__main__" == __name__: 
    app = wx.PySimpleApp(redirect=True)
    mainFrame().Show()
    app.MainLoop()
