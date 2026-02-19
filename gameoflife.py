from pyscript import web, when, window
import math
import random
import copy

gameArray = [[0]]

def isAlive(x,y):
    if y >= len(gameArray) or x >= len(gameArray[y]) or x < 0 or y < 0:
        return False
    return gameArray[y][x] == 1

def setDead(x,y,l=gameArray):
    l[y][x] = 0

def setAlive(x,y,l=gameArray):
    l[y][x] = 1

def createGrid(length, width):
    return [([0] * width) for x in range(length)]

def prettyprint():
    for y in gameArray:
        for x in y:
            if x == 1:
                print("▮", end="")
            else:
                print("▯", end="")
        print()


def populate():
    for x in gameArray:
        for y in range(0,len(x)): #Get the index of each item rather than the value
            if random.randint(1,3) == 1:
                x[y] = 1

def numNeighbors(x,y):
    number = 0
    if isAlive(x-1,y-1):
        number+=1
    if isAlive(x-1,y):
        number+=1
    if isAlive(x-1,y+1):
        number+=1
    if isAlive(x,y-1):
        number+=1
    if isAlive(x,y+1):
        number+=1
    if isAlive(x+1,y-1):
        number+=1
    if isAlive(x+1,y):
        number+=1
    if isAlive(x+1,y+1):
        number+=1

    return number


def step():
    gameArrayCopy = copy.deepcopy(gameArray)
    for y in range(len(gameArray)):
        for x in range(len(gameArray[y])):
            if isAlive(x,y):
                if not (1 < numNeighbors(x,y) < 4):
                    setDead(x,y,gameArrayCopy)
            else:
                if numNeighbors(x,y) == 3:
                    setAlive(x,y,gameArrayCopy)
    return gameArrayCopy

def createPage():
    grid = web.page["#gamegrid"]
    grid.innerHTML = ""
    for y in range(len(gameArray)):
        row = web.div(classes=["row"])
        for x in range(len(gameArray[y])):
            if gameArray[y][x] == 1:
                row.append(web.div(classes=["cell","alive"],id=f"a{y}_{x}"))
            else:
                row.append(web.div(classes=["cell","dead"],id=f"a{y}_{x}"))
        grid.append(row)

def updatePage():
    grid = web.page["#gamegrid"]
    for y in range(len(gameArray)):
        row = web.div(classes=["row"])
        for x in range(len(gameArray[y])):
            target = web.page[f"a{y}_{x}"]
            if gameArray[y][x] == 1:
                #row.append(web.div(classes=["cell","alive"],id=f"{y}_{x}"))
                if "dead" in target.classList:
                    target.classList.add("alive")
                    target.classList.remove("dead")
            else:
                #row.append(web.div(classes=["cell","dead"],id=f"{y}_{x}"))
                if "alive" in target.classList:
                    target.classList.add("dead")
                    target.classList.remove("alive")
        grid.append(row)

gameArray = createGrid(
    math.floor(window.screen.availHeight/60),
    math.floor(window.screen.availWidth/60)
)

#populate()


createPage()

@when("click","#advance")
def advance():
    global gameArray
    gameArray = step()
    updatePage()

@when("click",".cell")
def cellclick(event):
    print("clicked")
    target = event.target
    y,x = ((target.id)[1:]).split("_")
    x = int(x)
    y = int(y)

    if "alive" in target.classList:
        target.classList.add("dead")
        target.classList.remove("alive")
        gameArray[y][x] = 0
    elif "dead" in target.classList:
        target.classList.add("alive")
        target.classList.remove("dead")
        gameArray[y][x] = 1

@when("click","#reset")
def reset():
    global gameArray
    for y in range(len(gameArray)):
        for x in range(len(gameArray[y])):
            gameArray[y][x] = 0
    updatePage()

@when("click","#randomize")
def randomize():
    reset()
    populate()
    updatePage()

#for y in range(len(gameArray)):
#    for x in range(len(gameArray)):
#        print(numNeighbors(x,y), end="")
#    print()

#print("\nWelcome to Conway's game of life!")
#
#validinput = False
#while not validinput:
#    try:
#        y = int(await input("\nEnter the length of the grid: "))
#        x = int(await input("Enter the width of the grid: "))
#        validinput = True
#    except KeyboardInterrupt:
#        quit()
#    except:
#        print("\ninvalid input, try again")
#
#gameArray = createGrid(y,x)
#
#populate()
#
#while True:
#    print()
#    prettyprint()
#    value = (await input("\nPress enter to advance a step or type q to quit: ")).strip()
#    if value == "":
#        gameArray = step()
#    elif value in ("q", "Q"):
#        break
#    else:
#        print(f"Unknown input: '{value}'. Accepted values are: <blank>, 'q', or 'Q'")
#


