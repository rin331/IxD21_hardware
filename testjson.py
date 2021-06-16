import json


#条件を満たしているか判定
def callKey(keymap,callID):
    #型変更とかで例外したら，呼んだやつが悪い
    try:    
        #intで呼んでもいいように
        if(type(callID) is not str):
            callID=str(callID)
        
        #１文字目は1~3である
        if(callID[0] not in ["1","2","3"] ):
            raise Exception
        #2文字目は4~7である
        if(callID[1] not in ["4","5","6","7"] ):
            raise Exception
        #数字にすると11以上37以下である．
        if(10<=int(callID) and int(callID)<=37 ):
            raise Exception
    except :
        print("callKey(keymap,callID)  The callID is invalid.")
        return ""


    return keymap[callID]


with open("keymap.json") as jsonData:
    keymap=json.load(jsonData)

 
#serach "1_4" out ->"k"
print(callKey(keymap,"04"))

