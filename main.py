import time
import json
import random
import keyboard
import os

color = {
    "end": "\x1b[0m",
    "red": "\x1b[1;31;40m",
    "green": "\x1b[1;32;40m",
    "yellow": "\x1b[1;33;40m",
    "blue": "\x1b[1;34;40m",
    "violet": "\x1b[1;35;40m",
    "cyan": "\x1b[1;36;40m"

}

def helpMenu():
    print(f'''
[{ color['cyan'] } KeyMap { color['end'] }]

r - remove a selected solution
2 - add two seconds to a last solution
alt - start a time measurment
space - end a time measurment
h - display this menu
esc - quit 
    ''')
    return 
helpMenu()


def scrambleTheCube():
    side = ['U', 'D', 'F', 'B', 'R', 'L']
    possiblitie = ["'", '2']
    scramble = []
    randomIndex = random.randint(0, 5)
    scramble.append(side[randomIndex])
    i = 0
    for i in range(1, 20):
        ran = random.randint(0, 5)
        nextMove = side[ran]
        scramble.append(nextMove)
        while scramble[i] == scramble[i-1]:
            scramble[i] = side[random.randint(0, 5)]

    for i in range(1, 20):
        scramble[i] += possiblitie[random.randint(0, 1)]
    return scramble


def calculateAvg():
    with open('data.json', 'r+') as f:
        data = json.load(f)
        count = data['count']
        if count >= 3:
            data['averages']['avg3'] = round((data['times'][str(
                count)]+data['times'][str(count-1)]+data['times'][str(count-2)])/3, 3)

        if count >= 5:
            data['averages']['avg5'] = round((data['times'][str(count)]+data['times'][str(
                count-1)]+data['times'][str(count-2)]+data['times'][str(count-3)]+data['times'][str(count-4)])/5, 3)

        if data['averages']['bavg3'] == 0:
            data['averages']['bavg3'] = data['averages']['avg3']
        if data['averages']['bavg5'] == 0:
            data['averages']['bavg5'] = data['averages']['avg5']

        if data['averages']['avg3'] < data['averages']['bavg3']:
            data['averages']['bavg3'] = data['averages']['avg3']
        if data['averages']['avg5'] < data['averages']['bavg5']:
            data['averages']['bavg5'] = data['averages']['avg5']

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


def remove():
    with open('data.json', 'r+') as f:
        data = json.load(f)
        for i in data['times']:
            print(i, "  ", data['times'][i])

        print('Which solution is going out:')
        index = int(keyboard.read_key())
        data['best'] = 1000000
        data['worst'] = 0 
        for i in range(index, int(data['count'])):
            data['times'][str(i)] = data['times'][str(i+1)]

        del data['times'][str(data['count'])]

        data['count'] -= 1
        for i in range(1,int(data['count']+1)):
            if data['times'][str(i)]< data['best']:
                data['best']=data['times'][str(i)]
            elif data['times'][str(i)]> data['worst']:
                data['worst']=data['times'][str(i)]
        
        data['averages']['bavg3'] = 0
        data['averages']['avg3'] = 0
        data['averages']['bavg5'] = 0
        data['averages']['avg5'] = 0
        

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        calculateAvg()


def addTime():
    if keyboard.read_key() == "alt":
        startTime = time.time()
        while True:

            if keyboard.read_key() == "space":

                endTime = time.time()
                yourTime = round(endTime - startTime, 3)
                print("Your time: ", yourTime)

                with open('data.json', 'r+') as f:
                    data = json.load(f)
                    data["count"] += 1
                    data["times"][data["count"]] = yourTime

                    if data['best'] == 0:
                        data['best'] = yourTime

                    elif yourTime < data['best']:
                        data['best'] = yourTime

                    if yourTime > data['worst']:
                        data['worst'] = yourTime

                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                calculateAvg()
                return
    if keyboard.read_key() == 'r':
        remove()
        return
    if keyboard.read_key()=='h':
        helpMenu()
        return
    if keyboard.read_key() == 'esc':
        exit()


def main():
    while(True):

        print(
            f'''\n[{ color["violet"] } scrmbl { color["end"] }]: {' '.join(scrambleTheCube())}''')

        with open('data.json', 'r') as f:
            data = json.load(f)
            print(f"[{ color['green'] } best { color['end']}]   {data['best']}")
            print(f"[{ color['red'] } worst { color['end'] }]  {data['worst']}")
            print(
                f"[{ color['yellow'] } avg3 { color['end'] }]   {data['averages']['avg3']}")
            print(
                f"[{ color['yellow'] } avg5 { color['end'] }]   {data['averages']['avg5']}")
            print(
                f"[{ color['blue'] } bavg3 { color['end'] }]  {data['averages']['bavg3']}")
            print(
                f"[{ color['blue'] } bavg5 { color['end'] }]  {data['averages']['bavg5']}")
            print(f"[{ color['blue'] } count { color['end'] }]  {data['count']}")
        addTime()
        time.sleep(3)
        os.system("cls")


if __name__ == '__main__':
    
    main()
