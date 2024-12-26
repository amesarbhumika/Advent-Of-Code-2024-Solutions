MapList = []
OrderList = ""
InputState = 0
with open("input15.txt", "r") as data:
    for t in data:
        Line = t.strip()
        if Line == "":
            InputState = 1
        elif InputState == 0:
            MapList.append(Line)
        elif InputState == 1:
            OrderList += Line

WallSet = set()
OpenSet = set()
BoxSet = set()
for y, i in enumerate(MapList):
    for x, c in enumerate(i):
        if c == ".":
            OpenSet.add((x,y))
        elif c == "O":
            BoxSet.add((x,y))
            OpenSet.add((x,y))
        elif c == "#":
            WallSet.add((x,y))
        elif c == "@":
            OpenSet.add((x,y))
            RobotStart = (x,y)

DirectionDict = {"^": (0,-1), "v": (0,1), ">": (1,0), "<": (-1,0)}

RobotPosition = RobotStart
for m in OrderList:
    DX, DY = DirectionDict[m]
    RX, RY = RobotPosition
    NX, NY = RX+DX, RY+DY
    NewLoc = (NX,NY)
    if NewLoc in WallSet:
        continue
    elif NewLoc in OpenSet and NewLoc not in BoxSet:
        RobotPosition = NewLoc
        continue
    elif NewLoc in BoxSet:
        BX, BY = NX+DX, NY+DY
        while True:
            if (BX,BY) in WallSet:
                break
            elif (BX,BY) in BoxSet:
                BX,BY = BX+DX,BY+DY
                continue
            elif (BX,BY) in OpenSet:
                RobotPosition = NewLoc
                BoxSet.remove(NewLoc)
                BoxSet.add((BX,BY))
                break
            
Part1Answer = 0
for X,Y in BoxSet:
    Part1Answer += (100*Y + X)



def BoxMove (DX, DY, BoxIndex):
    ReturnList = [BoxIndex]
    A, B = BoxList[BoxIndex]
    AX, AY = A
    BX, BY = B
    NewA, NewB = (AX+DX,AY+DY), (BX+DX,BY+DY)
    if NewA in WallSet or NewB in WallSet:
        return False, None
    elif NewA in OpenSet and NewB in OpenSet and NewA not in CurrentBoxSet and NewB not in CurrentBoxSet:
        return True, ReturnList
    CheckBoxList = []
    for v, Box in enumerate(BoxList):
        if v == BoxIndex:
            continue
        if NewA in Box or NewB in Box:
            CheckBoxList.append(v)
    for v in CheckBoxList:
        Bool, NewList = BoxMove(DX, DY, v)
        if not(Bool):
            return False, None
        ReturnList += NewList
    return True, ReturnList

WallSet = set()
OpenSet = set()
BoxList = []
for y, i in enumerate(MapList):
    for x, c in enumerate(i):
        if c == ".":
            OpenSet.add((2*x,y))
            OpenSet.add((2*x+1,y))
        elif c == "O":
            BoxList.append(((2*x,y),(2*x+1,y)))
            OpenSet.add((2*x,y))
            OpenSet.add((2*x+1,y))
        elif c == "#":
            WallSet.add((2*x,y))
            WallSet.add((2*x+1,y))
        elif c == "@":
            OpenSet.add((2*x,y))
            OpenSet.add((2*x+1,y))
            RobotStart = (2*x,y)

RobotPosition = RobotStart
CurrentBoxSet = set()
for A, B in BoxList:
    CurrentBoxSet.add(A)
    CurrentBoxSet.add(B)

for m in OrderList:
    DX, DY = DirectionDict[m]
    RX, RY = RobotPosition
    NX, NY = RX+DX, RY+DY
    NewLoc = (NX,NY)
    if NewLoc in WallSet:
        continue
    elif NewLoc in OpenSet and NewLoc not in CurrentBoxSet:
        RobotPosition = NewLoc
        continue
    elif NewLoc in CurrentBoxSet:
        for v, Box in enumerate(BoxList):
            A, B = Box
            if A == NewLoc or B == NewLoc:
                Moved, MoveList = BoxMove(DX, DY, v)
                break
        if Moved:
            RobotPosition = NewLoc
            MoveSet = set(MoveList)
            for v in MoveSet:
                A, B = BoxList[v]
                AX, AY = A
                BX, BY = B
                BoxList[v] = ((AX+DX,AY+DY),(BX+DX,BY+DY))
            CurrentBoxSet = set()
            for A, B in BoxList:
                CurrentBoxSet.add(A)
                CurrentBoxSet.add(B)
        

Part2Answer = 0
for A,B in BoxList:
    AX, AY = A
    Part2Answer += (100*AY + AX)

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")