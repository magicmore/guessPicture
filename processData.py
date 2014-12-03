
class RawData(object):
    rawKeys = ['id', 'pic', 'answer', 'option', 'hint']
    def __init__(self, offset):
        fp = open("./rawData/raw.txt", "r")
        self.info = {}
        for i in range(0, offset):
            for i in range(0, len(self.rawKeys)):
                fp.readline()
        for i in range(0,len(self.rawKeys)):
            self.info[self.rawKeys[i]] = fp.readline()
        fp.close()
    def getInfo(self):
        return self.info
class ManageQuestionNumber(object):
    def __init__(self):
        fp = open("./rawData/qnumber.txt", "r")
        self.qNumber = int(fp.read())
        fp.close()
    def getQnumber(self):
        return self.qNumber
    def increaseQnumber(self):
        self.qNumber += 1
        self.writeQnumber()
    def resetQnumber(self):
        self.qNumber = 0
        self.writeQnumber()
    def writeQnumber(self):
        fp = open("./rawData/qnumber.txt", "w")
        fp.write(str(self.qNumber))
        fp.close()
if '__main__' == __name__:
    quest = RawData(0)
    for keys in RawData.rawKeys:
        print quest.getInfo()[keys]
    quest = RawData(1)
    for keys in RawData.rawKeys:
        print quest.getInfo()[keys]
    print len(quest.getInfo()['option'].strip('\n').decode('gbk'))
    qNum = ManageQuestionNumber()
    print qNum.getQnumber()
    qNum.increaseQnumber()
    print qNum.getQnumber()
    qNum.resetQnumber()
    print qNum.getQnumber()
