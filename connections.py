from json import load
from random import shuffle, randint



with open('connections.json', 'r') as file:
    data = load(file)

def numMatches(userList, levels):
    count = []
    levelCount = 0
    for level in levels:
        for word in userList:
            if word in level:
                levelCount += 1
        count.append(levelCount)
        levelCount = 0
    return count

def displayWords():
    output = f""
    for index in orderFound:
        if index == 0:
            print(f"\033[103m{groups[index]:^140}")
            for j in range(0,4):
                 print(f"{levels[index][j]:^35}", end="")
            print(f"\033[0m",end="")
        elif index == 1:
            print(f"\033[43m{groups[index]:^140}")
            for j in range(0,4):
                print(f"{levels[index][j]:^35}", end="")
            print(f"\033[0m",end="")
        elif index == 2:
            print(f"\033[104m{groups[index]:^140}")
            for j in range(0,4):
                print(f"{levels[index][j]:^35}", end="")
            print(f"\033[0m",end="")
        elif index == 3:
            print(f"\033[44m{groups[index]:^140}")
            for j in range(0,4):
                print(f"{levels[index][j]:^35}", end="")
            print(f"\033[0m",end="")
        print()



    
    for i in range(0,4-len(orderFound)):
        output += "\n"
        for j in range(0,4):
            output += f"{words[4*i+j]:^35} "
        output += "\n"
    print(output)

def getDay(dayNum):
    global day, levels,groups, words, answerData
    day = data[dayNum]
    levels = [[""]*4]*4
    groups = [""]*4
    words = [""]*16
    answerData = day["answers"]
    for i in range(0,4):
        answer = answerData[i]
        groups[i] = answer["group"]
        levels[i] = answer["members"]
        words[4*i] = (levels[i][0])
        words[4*i+1] = (levels[i][1])
        words[4*i+2] = (levels[i][2])
        words[4*i+3] = (levels[i][3])
    shuffle(words)
pastAttempts = []
def getUserList():
    global pastAttempts
    userString = input("Enter an attempt, seperate different words using commas\n: ")
    userString = userString.upper()
    userList = userString.split(",")
    for index in range(0, len(userList)):
        userList[index] = userList[index].strip()
    
    
    found = [False]*4
    while found != [True]*4:
        while len(userList) != 4:
            userString = input("Too many/few words, please enter 4 words\nEnter an attempt, seperate different words using commas\n: ")
            userString = userString.upper()
            userList = userString.split(",")
            for index in range(0, len(userList)):
                userList[index] = userList[index].strip()
                
        for index in range(0,4):
            if userList[index] in words:
                found[index] = True
                
        if found != [True]*4:
            index = found.index(False)
            userString = input("Cannot find " + userList[index] + "\nEnter an attempt, seperate different words using commas\n: ")
            userString = userString.upper()
            userList = userString.split(",")
            for index in range(0, len(userList)):
                userList[index] = userList[index].strip()

        while userList in pastAttempts:
            userString = input("Already attempted\nEnter an attempt, seperate different words using commas\n: ")
            userString = userString.upper()
            userList = userString.split(",")
            for index in range(0, len(userList)):
                userList[index] = userList[index].strip()

    pastAttempts.append(userList)
    return userList

def checkAnswer(numIncorrect):
    userAttempt = getUserList()
    levelCount = 0
    foundAny = False
    for i in range(0,4):
        levelCount = 0
        for j in range(0,4):
            if userAttempt[j] in levels[i]:
                
                levelCount += 1
        if levelCount == 4:
            foundAny =  True
            levelFound[i] = True
            orderFound.append(i)
            for word in levels[i]:
                words.remove(word)
        elif levelCount == 3:
            foundAny = True
            print("1 off")
            numIncorrect += 1
    if foundAny == False:
        numIncorrect += 1
        print("no matches")
    return numIncorrect
    
orderFound = []
dayNum = randint(1,1000)
getDay(dayNum)
levelFound = [False]*4
attempts = 0
while levelFound != [True]*4 and attempts < 4:
    displayWords()
    attempts = checkAnswer(attempts)

if attempts == 4:
    print("You have run out of attempts for day " + str(dayNum))
    for index in range(0,4):
        if index not in orderFound:
            orderFound.append(index)
            levelFound[index] = True
    displayWords()

else:
    displayWords()
    attempts = checkAnswer(attempts)
    print("congratulations you have completed connections for day " + str(dayNum))


    
