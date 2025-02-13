#coding=utf-8
#说明：nec红外拼码Python脚本程序
 
startLevel = (9000,4500)                #引导码
level = ((560,560), (560,1690))         #0,1对应的电平
endLevel = (560,5625)					#结束码

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
    code = startLevel                   #引导码
    code += getLevelsByCode(0x12)       #address
    code += getLevelsByCode(0x34)       #command
    code += endLevel
    print("电平码：")
    print(code)