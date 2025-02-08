startLevel = (3000,3000,3000,4300)                #引导码
level = ((520,650), (520,1650))         #0,1对应的电平
endLevel = (520,150000)                #结束码

def getLevelsByByte(b):
    lvls = ()
    for i in range(7, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsByData(s):
    lvls = ()
    sum = 0
    for i in range(7):
        sum += s[i]
        lvls += getLevelsByByte(s[i])
    lvls += getLevelsByByte(sum)
    return lvls
    
if __name__ == "__main__":
    code = startLevel                   #引导码
    code += getLevelsByData([0b10100101,
                            0b00011001,
                            0b00000100,
                            0b00000010,
                            0b00000000,
                            0b00000000,
                            0b00000000,
                            0b00000000])       #数据
    code += endLevel                   #结束码
    print("电平码：")
    print(code)