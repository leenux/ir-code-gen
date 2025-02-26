#TCL电视

startLevel = (4000,4000)                #引导码
level = ((500,1010), (500,2020))         #0,1对应的电平
endLevel = (500,8850)                #结束码

def getLevelsByByte(b):
    lvls = ()
    for i in range(7, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsBy4bits(b):
    lvls = ()
    for i in range(3, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

if __name__ == "__main__":
    print("TCL电视编码")
    cmd = 0x2F
    code = startLevel                   #引导码
    code += getLevelsBy4bits(0xF)       #address
    code += getLevelsByByte(cmd)       #command
    code += getLevelsBy4bits(0x0)       #fixed 0
    code += getLevelsByByte(255-cmd)       #reverse
    code += endLevel                   #结束码
    print("电平码：")
    print(code)