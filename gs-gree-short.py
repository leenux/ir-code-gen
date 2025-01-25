startLevel = (9000,4500)                #引导码
level = ((550,550), (550,1660))         #0,1对应的电平
endLevel = (5500,20000)                #结束码

def getLevelsByByte(b):
    lvls = ()
    for i in range(8, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsBy3bits(b):
    lvls = ()
    for i in range(3, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

if __name__ == "__main__":
    code = startLevel                   #引导码
    code += getLevelsByByte(0b00010000)       #数据1
    code += getLevelsByByte(0b10010000)       #数据2
    code += getLevelsByByte(0b00000000)       #数据3
    code += getLevelsByByte(0b00001010)       #数据4
    code += getLevelsBy3bits(0b010)       #fixed code
    code += endLevel                   #结束码
    print("电平码：")
    print(code)