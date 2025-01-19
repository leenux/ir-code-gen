startLevel = (3000,3000)                #引导码
level = ((520,1480), (562,2510))         #0,1对应的电平
endLevel = (520,4000,520,23000)

def getLevelsByByte(b):
    lvls = ()
    for i in range(8, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsByCode(a):
    lvlString = ()
    lvlString += getLevelsByByte(a)
    return lvlString

if __name__ == "__main__":
    code = startLevel                   #引导码
    code += getLevelsByCode(0x02)       #address
    code += getLevelsByCode(0x12)       #command
    code += endLevel                     #结束码
    print("电平码：")
    print(code)