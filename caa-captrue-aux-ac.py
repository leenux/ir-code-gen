# coding=utf-8
# 说明：奥克斯空调

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
    code = (9000, 4500)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b11000011,
            0b11101001,
            0b00000111,
            0b00000000,
            0b00000100,
            0b00000010,
            0b00000100,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00000000,
            0b10100000,
            0b11111011,
        ],
    )
    code += (530, 10000)  # 连接码
    return code


def cc():  # open-cool-26d
    code = (9000, 4500)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b11000011,
            0b11101001,
            0b00000111,
            0b00000000,
            0b00000100,
            0b00000010,
            0b00000100,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10100000,
            0b11111101,
        ],
    )
    code += (530, 10000)  # 连接码
    return code


def oh():  # open-cool-26d
    code = (9000, 4500)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b11000011,
            0b11101001,
            0b00000111,
            0b00000000,
            0b00000100,
            0b00000010,
            0b00000001,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00000000,
            0b10100000,
            0b11111100,
        ],
    )
    code += (530, 10000)  # 连接码
    return code


def ch():  # open-cool-26d
    code = (9000, 4500)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b11000011,
            0b11101001,
            0b00000111,
            0b00000000,
            0b00000100,
            0b00000010,
            0b00000001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10100000,
            0b11111000,
        ],
    )
    code += (530, 10000)  # 连接码
    return code


if __name__ == "__main__":
    print("奥克斯空调抓码生成")
    print("电平码：")
    code = ch()
    print(code)
