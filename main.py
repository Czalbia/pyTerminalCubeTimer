import time
import json
import random
import keyboard
import os


color={
    "end": "\x1b[0m",
    "red": "\x1b[1;31;40m",
    "green": "\x1b[1;32;40m",
    "yellow": "\x1b[1;33;40m",
    "blue": "\x1b[1;34;40m",
    "violet": "\x1b[1;35;40m"

}
while(True):

    def toString(s): 
        str1 = "" 
        
        for ele in s: 
            str1 += " "+ele  
        return str1 

    
    def scrambleTheCube():
        side = ['U','D','F','B','R','L']
        possiblitie=["'",'2']
        scramble=[]
        randomIndex=random.randint(0,5)
        scramble.append(side[randomIndex])
        i=0
        for i in range(1,20):
            ran=random.randint(0,5)
            nextMove=side[ran]
            scramble.append(nextMove)
            while scramble[i]==scramble[i-1]:
                scramble[i]=side[random.randint(0,5)]

        for i in range(1,20):
            scramble[i]+=possiblitie[random.randint(0,1)]
        return scramble

    def calculateAvg():
        with open('data.json', 'r+') as f:
            data = json.load(f)
            count=data['count']
            if count>=3:
                data['averages']['avg3']=round((data['times'][str(count)]+data['times'][str(count-1)]+data['times'][str(count-2)])/3,3)
            
            if count>=5:
                data['averages']['avg5']=round((data['times'][str(count)]+data['times'][str(count-1)]+data['times'][str(count-2)]+data['times'][str(count-3)]+data['times'][str(count-4)])/5,3)
            
            if data['averages']['bavg3']==0:
                data['averages']['bavg3']=data['averages']['avg3']
            if data['averages']['bavg5']==0:
                data['averages']['bavg5']=data['averages']['avg5']
             
            if data['averages']['avg3']<data['averages']['bavg3']:
                data['averages']['bavg3']=data['averages']['avg3']
            if data['averages']['avg5']<data['averages']['bavg5']:
                data['averages']['bavg5']=data['averages']['avg5']

            f.seek(0)  
            json.dump(data, f, indent=4)
            f.truncate()

    def addTime():
        print("Press alt to start, space to end, esc to end the program")
        if keyboard.read_key()=="alt":
            startTime=time.time()

            while True:

                if keyboard.read_key()=="space":

                    endTime=time.time()
                    yourTime=round(endTime - startTime,3)
                    print("Your time: ",yourTime)
                    
                    with open('data.json', 'r+') as f:
                        data = json.load(f)
                        data["count"]+=1
                        data["times"][data["count"]]=yourTime
                        
                        if data['best']==0:
                            data['best']=yourTime
                            
                        elif yourTime<data['best']:
                            data['best']=yourTime

                        if yourTime>data['worst']:
                            data['worst']=yourTime
                        
                        f.seek(0)  
                        json.dump(data, f, indent=4)
                        f.truncate()
                    calculateAvg()
                    return 
        if keyboard.read_key()=='esc':
            exit()    

   


    print(f'''\n[{ color["violet"] } scrmbl { color["end"] }]:{toString(scrambleTheCube())}''')


    with open('data.json', 'r') as f:
        data = json.load(f)
        print(f"[{ color['green'] } best { color['end']}]   {data['best']}")
        print(f"[{ color['red'] } worst { color['end'] }]  {data['worst']}")
        print(f"[{ color['yellow'] } avg3 { color['end'] }]   {data['averages']['avg3']}")
        print(f"[{ color['yellow'] } avg5 { color['end'] }]   {data['averages']['avg5']}")
        print(f"[{ color['blue'] } bavg3 { color['end'] }]  {data['averages']['bavg3']}")
        print(f"[{ color['blue'] } bavg5 { color['end'] }]  {data['averages']['bavg5']}")
        
    addTime()
    time.sleep(1)
    os.system("cls")
