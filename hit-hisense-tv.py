#coding=utf-8
#说明：海信电视
 
startLevel = (9000,4500)                    #引导码
level = ((600,530),(600,1630))              #0,1对应的电平
endLevel = (600,20000)                      #结束码

def getLevelsByByte(b):
    lvls = ()
    for i in range(7, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsByCode(a):
    lvlString = ()
    lvlString += getLevelsByByte(a)
    reverse = 255 - a
    lvlString += getLevelsByByte(reverse)
    return lvlString

if __name__ == "__main__":
    print("NEC编码生成")
    code = startLevel                           #引导码
    code += getLevelsByByte(0x00)               #address1
    code += getLevelsByByte(0b11111101)         #address2
    code += getLevelsByCode(0b00100010)         #command
    code += endLevel                            #结束码
    print("电平码：")
    print(code)