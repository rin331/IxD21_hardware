import datetime
import time

def writeText(filePath,text):
    with open(filePath, mode='a') as f:
        f.write(text+"\n")

#create a txt file for debugging (in startup).
#change global inv "debugfilePath"
def createFile():
    global debugFilePath
    nowtime= datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    debugFilePath=debugFilePath+nowtime+".txt"
    print(debugFilePath)
    with open(debugFilePath,mode='x') as f:
        f.write("")


debugFilePath="./Debug/"
debugLine='aaa'


createFile()
writeText(debugFilePath,debugLine)



