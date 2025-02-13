# coding=utf-8
# 说明：格力空调

level12345 = ((636, 560), (636, 1636))  # 数据12345的0,1对应的电平


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
    code = (9000, 4500)  # 引导码
    code += getLevelsByData(  # 数据1
        level12345,
        [
            0b10010000,
            0b01010000,
            0b00000000,
            0b00001010,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)  # 连接码
    code += getLevelsByData(  # 数据2
        level12345,
        [
            0b00000000,
            0b00000100,
            0b00000000,
            0b00001111,
        ],
    )
    code += (636, 40000, 9000, 4500)  # 连接码
    code += getLevelsByData(  # 数据3
        level12345,
        [
            0b10010000,
            0b01010000,
            0b00000000,
            0b00001110,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)
    code += getLevelsByData(  # 数据4
        level12345,
        [
            0b00000000,
            0b00000000,
            0b00000000,
            0b00001011,
        ],
    )
    code += (636, 76900, 8989, 4419)
    code += getLevelsByData(  # 数据5
        level12345,
        [
            0b10010000,
            0b01010000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)  # 结束码
    return code


def cc():  # open-cool-26d
    code = (9000, 4500)  # 引导码
    code += getLevelsByData(  # 数据1
        level12345,
        [
            0b10000000,
            0b01010000,
            0b00000000,
            0b00001010,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)  # 连接码
    code += getLevelsByData(  # 数据2
        level12345,
        [
            0b00000000,
            0b00000100,
            0b00000000,
            0b00001110,
        ],
    )
    code += (636, 40000, 9000, 4500)  # 连接码
    code += getLevelsByData(  # 数据3
        level12345,
        [
            0b10000000,
            0b01010000,
            0b00000000,
            0b00001110,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)
    code += getLevelsByData(  # 数据4
        level12345,
        [
            0b00000000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    code += (636, 76900, 8989, 4419)
    code += getLevelsByData(  # 数据5
        level12345,
        [
            0b10000000,
            0b01010000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)  # 结束码
    return code


def oh():  # open-cool-26d
    code = (9000, 4500)  # 引导码
    code += getLevelsByData(  # 数据1
        level12345,
        [
            0b00110000,
            0b01010000,
            0b00000000,
            0b00001010,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)  # 连接码
    code += getLevelsByData(  # 数据2
        level12345,
        [
            0b00000000,
            0b00000100,
            0b00000000,
            0b00000100,
        ],
    )
    code += (636, 40000, 9000, 4500)  # 连接码
    code += getLevelsByData(  # 数据3
        level12345,
        [
            0b00110000,
            0b01010000,
            0b00000000,
            0b00001110,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)
    code += getLevelsByData(  # 数据4
        level12345,
        [
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
        ],
    )
    code += (636, 76900, 8989, 4419)
    code += getLevelsByData(  # 数据5
        level12345,
        [
            0b00110000,
            0b01010000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)  # 结束码
    return code


def ch():  # open-cool-26d
    code = (9000, 4500)  # 引导码
    code += getLevelsByData(  # 数据1
        level12345,
        [
            0b00100000,
            0b01010000,
            0b00000000,
            0b00001010,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)  # 连接码
    code += getLevelsByData(  # 数据2
        level12345,
        [
            0b00000000,
            0b00000100,
            0b00000000,
            0b00000101,
        ],
    )
    code += (636, 40000, 9000, 4500)  # 连接码
    code += getLevelsByData(  # 数据3
        level12345,
        [
            0b00100000,
            0b01010000,
            0b00000000,
            0b00001110,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)
    code += getLevelsByData(  # 数据4
        level12345,
        [
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000001,
        ],
    )
    code += (636, 76900, 8989, 4419)
    code += getLevelsByData(  # 数据5
        level12345,
        [
            0b00100000,
            0b01010000,
            0b00000000,
            0b00000000,
            0b00001010,
        ],
    )
    code += getLevelsByByte(level12345, 0b010, 2)
    code += (636, 20000)  # 结束码
    return code


if __name__ == "__main__":
    print("格力空调抓码生成")
    print("电平码：")
    code = ch()
    print(code)
