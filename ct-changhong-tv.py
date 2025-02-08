#coding=utf-8
#说明：长虹电视红外拼码Python脚本程序
 
startLevel = (9000,4500)                    #引导码
level = ((550,580),(550,1700))              #0,1对应的电平
endLevel = (550,39400,9000,2290,550,20000)  #结束码

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
    print("长虹电视编码生成")
    code = startLevel                       #引导码
    code += getLevelsByCode(0x02)           #address
    code += getLevelsByCode(0b01111000)     #command
    code += endLevel                        #结束码
    print("电平码：")
    print(code)