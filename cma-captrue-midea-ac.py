# coding=utf-8
# 说明：美的空调
start = (4500, 4500)
end = (510, 20000)
level1 = (630, 482), (630, 1610)
level2 = (630, 482), (630, 1610)
level3 = (550, 520), (550, 1576)
level4 = (510, 530), (510, 1600)
connect1 = (630, 5200, 4500, 4500)
connect2 = (630, 85000, 4500, 4500)
connect3 = (550, 5200, 4500, 4500)


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
    code = start
    code += getLevelsByData(
        level1,
        [
            0b10110010,
            0b01001101,
            0b10111111,
            0b01000000,
            0b11010000,
            0b00101111,
        ],
    )
    code += connect1
    code += getLevelsByData(
        level2,
        [
            0b10110010,
            0b01001101,
            0b10111111,
            0b01000000,
            0b11010000,
            0b00101111,
        ],
    )
    code += connect2
    code += getLevelsByData(
        level3,
        [
            0b10100001,
            0b10100000,
            0b00001001,
            0b11111111,
            0b11111111,
            0b00010111,
        ],
    )
    code += connect3
    code += getLevelsByData(
        level4,
        [
            0b01011110,
            0b01011111,
            0b11110110,
            0b00000000,
            0b00000000,
            0b11101000,
        ],
    )
    code += end
    return code


def cc():  # close-cool-26d
    code = start
    code += getLevelsByData(
        level1,
        [
            0b10110010,
            0b01001101,
            0b01111011,
            0b10000100,
            0b11100000,
            0b00011111,
        ],
    )
    code += connect1
    code += getLevelsByData(
        level2,
        [
            0b10110010,
            0b01001101,
            0b01111011,
            0b10000100,
            0b11100000,
            0b00011111,
        ],
    )
    code += connect2
    code += getLevelsByData(
        level3,
        [
            0b10100001,
            0b00100000,
            0b00001001,
            0b11111111,
            0b11111111,
            0b10010111,
        ],
    )
    code += connect3
    code += getLevelsByData(
        level4,
        [
            0b01011110,
            0b11011111,
            0b11110110,
            0b00000000,
            0b00000000,
            0b01101000,
        ],
    )
    code += end
    return code


def oh():  # open-heat-26d
    code = start
    code += getLevelsByData(
        level1,
        [
            0b10110010,
            0b01001101,
            0b10111111,
            0b01000000,
            0b11011100,
            0b00100011,
        ],
    )
    code += connect1
    code += getLevelsByData(
        level2,
        [
            0b10110010,
            0b01001101,
            0b10111111,
            0b01000000,
            0b11011100,
            0b00100011,
        ],
    )
    code += connect2
    code += getLevelsByData(
        level3,
        [
            0b10100001,
            0b10100011,
            0b00001001,
            0b11111111,
            0b11111111,
            0b00010100,
        ],
    )
    code += connect3
    code += getLevelsByData(
        level4,
        [
            0b01011110,
            0b01011100,
            0b11110110,
            0b00000000,
            0b00000000,
            0b11101011,
        ],
    )
    code += end
    return code


def ch():  # close-heat-26d
    code = start
    code += getLevelsByData(
        level1,
        [
            0b10110010,
            0b01001101,
            0b01111011,
            0b10000100,
            0b11100000,
            0b00011111,
        ],
    )
    code += connect1
    code += getLevelsByData(
        level2,
        [
            0b10110010,
            0b01001101,
            0b01111011,
            0b10000100,
            0b11100000,
            0b00011111,
        ],
    )
    code += connect2
    code += getLevelsByData(
        level3,
        [
            0b10100001,
            0b00100011,
            0b00001001,
            0b11111111,
            0b11111111,
            0b10010100,
        ],
    )
    code += connect3
    code += getLevelsByData(
        level4,
        [
            0b01011110,
            0b11011100,
            0b11110110,
            0b00000000,
            0b00000000,
            0b01101011,
        ],
    )
    code += end
    return code


if __name__ == "__main__":
    print("美的空调抓码生成")
    print("电平码：")
    code = cc()
    print(code)
