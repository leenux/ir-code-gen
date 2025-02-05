startLevel = (9166,4470)                #引导码
level = ((646,547), (646,1647))         #0,1对应的电平
endLevel = (646,100000)                #结束码

def getLevelsByByte(b):
    lvls = ()
    for i in range(8, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsByData(s):
    lvls = ()
    sum = 0
    for i in range(12):
        sum += s[i]
        lvls += getLevelsByByte(s[i])
    lvls += getLevelsByByte(sum)
    return lvls
    
if __name__ == "__main__":
    code = startLevel                   #引导码
    code += getLevelsByData([0b11000011,
                            0b11110010,
                            0b00000111,
                            0b00000000,
                            0b00000101,
                            0b00000000,
                            0b00000000,
                            0b01001010,
                            0b00000000,
                            0b00000000,
                            0b00000100,
                            0b00000000,
                            0b00010101])       #数据
    code += endLevel                   #结束码
    print("电平码：")
    print(code)