# coding=utf-8
# 说明：夏普电视

startLevel = (280, 1850)  # 引导码
level = ((280, 790), (280, 1850))  # 0,1对应的电平
endLevel = (280, 20000)  # 结束码
sepLevel = (280, 44000)


def getLevelsByByte(b, length):
    lvls = ()
    for i in range(length - 1, -1, -1):
        lvls += level[((2**i) & b) >> i]
    return lvls


def getLevelsByCode(a):
    lvlString = ()
    lvlString += getLevelsByByte(a, 8)
    reverse = 255 - a
    lvlString += getLevelsByByte(reverse, 8)
    return lvlString


def getLevelsByReverse(a):
    reverse = 255 - a
    lvlString += getLevelsByByte(reverse, 8)
    return lvlString


if __name__ == "__main__":
    print("夏普电视编码生成")
    code = startLevel  # 引导码
    code += getLevelsByByte(0b0000, 4)  # address1
    cmd = 0b01101000  # command
    code += getLevelsByByte(cmd, 8)
    code += getLevelsByByte(0b10, 2)  # fix code
    code += sepLevel
    code += startLevel
    code += getLevelsByByte(255 - cmd, 8)  # command code reverse
    code += getLevelsByByte(0b01, 2)  # fix code reverse
    code += endLevel  # 结束码
    print("电平码：")
    print(code)
