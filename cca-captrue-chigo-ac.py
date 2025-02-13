# coding=utf-8
# 说明：志高空调

level1 = ((560, 560), (560, 1620))  # 数据的0,1对应的电平


def getLevelsByByte(level, b):
    lvls = ()
    for i in range(7, -1, -1):
        lvls += level[((2**i) & b) >> i]
    return lvls


def getLevelsByData(level, s):
    lvls = ()
    for i in range(len(s)):
        lvls += getLevelsByByte(level, s[i])
    return lvls


def oc():  # open-cool-26d
    code = (6080, 7400)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b11111111,
            0b00000000,
            0b11111111,
            0b00000000,
            0b11111111,
            0b00000000,
            0b10011111,
            0b01100000,
            0b10101011,
            0b01010100,
            0b01010100,
            0b10101011,
        ],
    )
    code += (560,7400,560,10000)  # 连接码
    return code


def cc():  # open-cool-26d
    code = (6080, 7400)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b11111111,
            0b00000000,
            0b11111111,
            0b00000000,
            0b11111111,
            0b00000000,
            0b11011111,
            0b00100000,
            0b10101011,
            0b01010100,
            0b01010100,
            0b10101011,
        ],
    )
    code += (560,7400,560,10000)  # 连接码
    return code


def oh():  # open-cool-26d
    code = (6080, 7400)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b11111111,
            0b00000000,
            0b11111111,
            0b00000000,
            0b11111111,
            0b00000000,
            0b10101001,
            0b01010110,
            0b10101110,
            0b01010001,
            0b01010100,
            0b10101011,
        ],
    )
    code += (560,7400,560,10000)  # 连接码
    return code


def ch():  # open-cool-26d
    code = (6080, 7400)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b11111111,
            0b00000000,
            0b11111111,
            0b00000000,
            0b11111111,
            0b00000000,
            0b11101001,
            0b00010110,
            0b10101110,
            0b01010001,
            0b01010100,
            0b10101011,
        ],
    )
    code += (560,7400,560,10000)  # 连接码
    return code


if __name__ == "__main__":
    print("志高空调抓码生成")
    print("电平码：")
    code = ch()
    print(code)
