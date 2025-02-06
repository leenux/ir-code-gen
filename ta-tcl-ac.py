startLevel = (3000,1650)                #引导码
level = ((500,325), (500,1050))         #0,1对应的电平
endLevel = (500,100000)                #结束码

def getLevelsByByte(b):
    lvls = ()
    for i in range(8, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsByData(s):
    lvls = ()
    sum = 0
    for i in range(13):
        sum += s[i]
        lvls += getLevelsByByte(s[i])
    lvls += getLevelsByByte(0xF + sum)
    return lvls
    
if __name__ == "__main__":
    code = startLevel                   #引导码
    code += getLevelsByData([0b00100011,    #0
                            0b11001011,     #1
                            0b00100110,     #2
                            0b00000010,     #3
                            0b00000000,     #4
                            0b00000100,     #5
                            0b00001000,     #6
                            0b00000101,     #7
                            0b00000000,     #8
                            0b00000000,     #9
                            0b00000000,     #10
                            0b00000000,     #11
                            0b10000000])    #12
    code += endLevel                   #结束码
    print("电平码：")
    print(code)