# coding=utf-8
# 说明：华凌空调

level12345 = ((580, 566), (580, 1606))  # 数据12345的0,1对应的电平


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
    code = (4426, 4426)  # 引导码
    code += getLevelsByData(  # 数据1
        level12345,
        [
            0b10110010,
            0b01001101,
            0b10111111,
            0b01000000,
            0b11010000,
            0b00101111,
        ],
    )
    code += (580, 5170, 4426, 4426)  # 连接码
    code += getLevelsByData(  # 数据2
        level12345,
        [
            0b10110010,
            0b01001101,
            0b10111111,
            0b01000000,
            0b11010000,
            0b00101111,
        ],
    )
    code += (580, 5170, 4426, 4426)  # 连接码
    code += getLevelsByData(  # 数据3
        level12345,
        [
            0b11010101,
            0b01100110,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00111011,
        ],
    )
    code += (580, 10000)  # 结束码
    return code


def cc():  # open-cool-26d
    code = (4426, 4426)  # 引导码
    code += getLevelsByData(  # 数据4
        level12345,
        [
            0b10110010,
            0b01001101,
            0b01111011,
            0b10000100,
            0b11100000,
            0b00011111,
        ],
    )
    code += (580, 5170, 4426, 4426)  # 连接码
    code += getLevelsByData(  # 数据2
        level12345,
        [
            0b10110010,
            0b01001101,
            0b01111011,
            0b10000100,
            0b11100000,
            0b00011111,
        ],
    )
    code += (580, 10000)  # 结束码
    return code


def oh():  # open-cool-26d
    code = (4426, 4426)  # 引导码
    code += getLevelsByData(  # 数据1
        level12345,
        [
            0b10110010,
            0b01001101,
            0b10111111,
            0b01000000,
            0b11011100,
            0b00100011,
        ],
    )
    code += (580, 5170, 4426, 4426)  # 连接码
    code += getLevelsByData(  # 数据2
        level12345,
        [
            0b10110010,
            0b01001101,
            0b10111111,
            0b01000000,
            0b11011100,
            0b00100011,
        ],
    )
    code += (580, 5170, 4426, 4426)  # 连接码
    code += getLevelsByData(  # 数据3
        level12345,
        [
            0b11010101,
            0b01100110,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00111011,
        ],
    )
    code += (580, 10000)  # 结束码
    return code


def ch():  # open-cool-26d
    code = (4426, 4426)  # 引导码
    code += getLevelsByData(  # 数据4
        level12345,
        [
            0b10110010,
            0b01001101,
            0b01111011,
            0b10000100,
            0b11100000,
            0b00011111,
        ],
    )
    code += (580, 5170, 4426, 4426)  # 连接码
    code += getLevelsByData(  # 数据2
        level12345,
        [
            0b10110010,
            0b01001101,
            0b01111011,
            0b10000100,
            0b11100000,
            0b00011111,
        ],
    )
    code += (580, 10000)  # 结束码
    return code


if __name__ == "__main__":
    print("华凌空调抓码生成")
    print("电平码：")
    code = ch()
    print(code)
