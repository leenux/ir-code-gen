# coding=utf-8
# 说明：长虹空调

level1 = ((530, 560), (530, 1650))  # 数据1的0,1对应的电平
level2 = ((600, 584), (600, 1734))  # 数据2的0,1对应的电平


def getLevelsByByte(level, b, l):
    lvls = ()
    for i in range(l, -1, -1):
        lvls += level[((2**i) & b) >> i]
    return lvls


def getLevelsByData(level, s):
    lvls = ()
    for i in range(len(s)):
        lvls += getLevelsByByte(level, s[i], 7)
    return lvls


def oc():  # open-cool-26d
    code = (8400, 4200)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b01101010,
            0b01101110,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00000011,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b01100100,
        ],
    )
    code += (556, 76800, 9000, 4500)  # 连接码
    code += getLevelsByData(  # 数据2
        level2,
        [
            0b00110000,
            0b00010000,
            0b00001100,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    return code


def cc():  # open-cool-26d
    code = (8400, 4200)  # 引导码
    code += getLevelsByData(  # 数据4
        level1,
        [
            0b01101010,
            0b01101110,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b01011000,
        ],
    )
    code += (556, 76800, 9000, 4500)  # 连接码
    code += getLevelsByData(  # 数据2
        level2,
        [
            0b00110001,
            0b00010000,
            0b00001100,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    return code


def oh():  # open-cool-26d
    code = (8400, 4200)  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b01101010,
            0b01101110,
            0b00000000,
            0b00000000,
            0b00001000,
            0b00000011,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10100100,
        ],
    )
    code += (556, 76800, 9000, 4500)  # 连接码
    code += getLevelsByData(  # 数据2
        level2,
        [
            0b00111100,
            0b01010000,
            0b00001100,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    return code


def ch():  # open-cool-26d
    code = (8400, 4200)  # 引导码
    code += getLevelsByData(  # 数据4
        level1,
        [
            0b01101010,
            0b01101110,
            0b00000000,
            0b00000000,
            0b00001000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10011000,
        ],
    )
    code += (556, 76800, 9000, 4500)  # 连接码
    code += getLevelsByData(  # 数据2
        level2,
        [
            0b00111101,
            0b01010000,
            0b00001100,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    return code


if __name__ == "__main__":
    print("长虹空调抓码生成")
    print("电平码：")
    code = ch()
    code += getLevelsByByte(level2, 0b1010, 3)
    code += (600, 10000)  # 结束码
    print(code)
