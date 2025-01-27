startLevel = (9000,4600)                #引导码
level = ((560,600), (560,1680))         #0,1对应的电平
endLevel = (560,200000)                #结束码

def getLevelsByByte(b):
    lvls = ()
    for i in range(8, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsByData(s):
    lvls = ()
    for i in range(6):
        lvls += getLevelsByByte(s[i])
    return lvls
    
if __name__ == "__main__":
    code = startLevel                   #引导码
    code += getLevelsByData([0b10000011,
                            0b00000110,
                            0b00100100,
                            0b00101000,
                            0b00000001,
                            0b00000000,
                            ])       #数据
    code += endLevel                   #结束码
    print("电平码：")
    print(code)