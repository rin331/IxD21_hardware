import json


#条件を満たしているか判定
def callKey(keymap,callID):
    #型変更とかで例外したら，呼んだやつが悪い
    try:    
        #intで呼んでもいいように
        if(type(callID) is not str):
            callID=str(callID)
        
    except :
        print("callKey(keymap,callID)  The callID is invalid.")
        return ""


    return keymap[callID]


with open("keymap.json") as jsonData:
    keymap=json.load(jsonData)

 
#serach "1_4" out ->"k"
print(callKey(keymap,"5"))

