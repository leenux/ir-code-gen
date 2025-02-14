# coding=utf-8
# 说明：海尔空调

start = (3000, 3000, 3000, 4450)
data = ((550, 560), (550, 1650))
end = (550, 20000)


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
        data,
        [
            0b10100110,
            0b10100010,
            0b00000000,
            0b00000000,
            0b01000000,
            0b10100000,
            0b00000000,
            0b00100000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000101,
            0b01001101,
        ],
    )
    code += end
    return code


def cc():  # open-cool-26d
    code = start
    code += getLevelsByData(
        data,
        [
            0b10100110,
            0b10100000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10100000,
            0b00000000,
            0b00100000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000101,
            0b00001011,
        ],
    )
    code += end
    return code


def oh():  # open-cool-26d
    code = start
    code += getLevelsByData(
        data,
        [
            0b10100110,
            0b10100010,
            0b00000000,
            0b00000000,
            0b11000000,
            0b01100000,
            0b00000000,
            0b10000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000101,
            0b11101101,
        ],
    )
    code += end
    return code


def ch():  # open-cool-26d
    code = start
    code += getLevelsByData(
        data,
        [
            0b10100110,
            0b10100000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b01100000,
            0b00000000,
            0b10000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000101,
            0b00101011,
        ],
    )
    code += end
    return code


if __name__ == "__main__":
    print("海尔空调抓码生成")
    print("电平码：")
    code = ch()
    print(code)
