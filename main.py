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
    def scrambleTheCube():
        notation=["F", "F2", "F'", "R", "R2", "R'", "U", "U2", "U'", "B", "B2", "B'", "L", "L2", "L'", "D", "D2", "D'"]

        scramble=[]
        scrambleWithoutAdditions=[]
        for i in range(0,20):
            randomNotation=random.randint(0,17)
            scramble.append(notation[randomNotation])
            scrambleWithoutAdditions.append(notation[randomNotation][0])
        for i in range(1,20):
            if scrambleWithoutAdditions[i] == scrambleWithoutAdditions[i-1]:
                randomNotation=random.randint(0,17)
                scrambleWithoutAdditions.insert(i,notation[randomNotation][0])
                scramble.insert(i,notation[randomNotation])
                i=1
        return scramble


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
                        data["times"][str(data["count"])]=yourTime
                        f.seek(0)  
                        json.dump(data, f, indent=4)
                        f.truncate()
                    return 
        if keyboard.read_key()=='esc':
            exit()    

            

    print(f'''\n[{ color["violet"] } scrmbl { color["end"] }]:{str(scrambleTheCube())}''')


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
