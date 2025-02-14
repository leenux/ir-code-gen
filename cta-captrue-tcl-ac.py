# coding=utf-8
# 说明：TCL空调

start = (3000, 1740)
level = ((450, 384), (450, 1060))
end = (450, 20000)


def getData(c):
    # oc
    if c == "oc":
        data = [
            0b11000100,
            0b11010011,
            0b01100100,
            0b10000000,
            0b00000000,
            0b00100100,
            0b11000000,
            0b10100000,
            0b00000010,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10000001,
        ]
        return data

    if c == "cc":
        # cc
        data = [
            0b11000100,
            0b11010011,
            0b01100100,
            0b10000000,
            0b00000000,
            0b00000100,
            0b11000000,
            0b10100000,
            0b00000010,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10111110,
        ]
        return data

    if c == "oh":
        # oh
        data = [
            0b11000100,
            0b11010011,
            0b01100100,
            0b10000000,
            0b00000000,
            0b00100100,
            0b10000000,
            0b10100000,
            0b00000010,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b11111110,
        ]
        return data

    if c == "ch":
        # ch
        data = [
            0b11000100,
            0b11010011,
            0b01100100,
            0b10000000,
            0b00000000,
            0b00000100,
            0b10000000,
            0b10100000,
            0b00000010,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b11011110,
        ]
        return data


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


def cmd(c):
    data = getData(c)
    code = start
    code += getLevelsByData(
        level,
        data,
    )
    code += end
    return code


if __name__ == "__main__":
    print("TCL空调抓码生成")
    print("电平码：")
    code = cmd("ch")
    print(code)
