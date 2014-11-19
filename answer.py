class AnswerStr(object):
    def __init__(self, andswerStrSum):
        self.answer = "#"*andswerStrSum
        self.answerLimit = andswerStrSum
        self.inputStrSum = 0
    def isLegal(self):
        if self.inputStrSum < self.answerLimit:
            return True
        else:
            return False
    def appendNewStr(self, newStr):
        if True == self.isLegal():
            self.answer = self.answer.replace("#", newStr, 1)
            self.inputStrSum += 1
    def removeStr(self, newStr):
        self.answer = self.answer.replace(newStr, "#", 1)
        self.inputStrSum -= 1
    def getValue(self):
        return self.answer
if __name__=="__main__":
    a=AnswerStr(3)
    print a.getValue()
    print a.isLegal()
    a.appendNewStr("x")
    print a.getValue()
    a.appendNewStr("x")
    a.appendNewStr("x")
    print a.getValue()
    print a.isLegal()
    a.appendNewStr("x")
    print a.getValue()
