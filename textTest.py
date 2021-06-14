 def writeText(self,filePath,text):
        with open(filePath, mode='a') as f:
            f.write(text+"\n")

debugFilePath="./Debug/test.txt"
debugLine=''


