# coding=utf-8
# 说明：海信空调

start = (9000, 4500)
connect1 = (580, 7900)
connect2 = (580, 7900)
connect3 = (580, 77300, 3400, 1700)
end = (380, 20000)
level1 = ((580, 510), (580, 1650))
level2 = ((580, 510), (580, 1650))
level3 = ((580, 510), (580, 1650))
level4 = ((420, 420), (420, 1260))


def getData(c):
    # oc
    if c == "oc":
        data1 = [
            0b11000001,
            0b01100000,
            0b00100000,
            0b01000001,
            0b00000000,
            0b00000000,
        ]
        data2 = [
            0b00000001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00000000,
            0b00000100,
            0b01100000,
        ]
        data3 = [
            0b00000000,
            0b10100100,
            0b00000000,
            0b00000000,
            0b00001100,
            0b00101000,
            0b10000000,
        ]
        data4 = [
            0b00000010,
            0b00000000,
            0b00101000,
            0b00000001,
            0b11000010,
            0b01000001,
            0b00110100,
            0b00101111,
            0b11000100,
            0b00000000,
            0b00010110,
            0b00000000,
            0b00000000,
            0b10000000,
            0b00000000,
            0b00000000,
            0b11110010,
        ]
        return data1, data2, data3, data4

    if c == "cc":
        # cc
        data1 = [
            0b11000001,
            0b01100000,
            0b00100000,
            0b01000001,
            0b00000000,
            0b00000000,
        ]
        data2 = [
            0b00000001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00000000,
            0b00000100,
            0b01100000,
        ]
        data3 = [
            0b00000000,
            0b10100100,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00101000,
            0b10001000,
        ]
        data4 = [
            0b00000010,
            0b00000000,
            0b00101000,
            0b00000001,
            0b11000010,
            0b10000001,
            0b00110100,
            0b00101111,
            0b11000000,
            0b00000000,
            0b00010110,
            0b00000000,
            0b00000000,
            0b10000000,
            0b00000000,
            0b00000000,
            0b00110010,
        ]
        return data1, data2, data3, data4

    if c == "oh":
        # oh
        data1 = [
            0b11000001,
            0b01100000,
            0b00100000,
            0b00000001,
            0b00000000,
            0b00000000,
        ]
        data2 = [
            0b00000001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00000000,
            0b01001000,
            0b01101100,
        ]
        data3 = [
            0b00000000,
            0b10100100,
            0b00000000,
            0b00000000,
            0b00001100,
            0b00101000,
            0b10000000,
        ]
        data4 = [
            0b00000010,
            0b00000000,
            0b00101000,
            0b00000001,
            0b11000010,
            0b01000010,
            0b00110100,
            0b00011011,
            0b11000100,
            0b00000000,
            0b00010110,
            0b00000000,
            0b00000000,
            0b10000000,
            0b00000000,
            0b00000000,
            0b10110010,
        ]
        return data1, data2, data3, data4

    if c=="ch":
        # ch
        data1 = [
            0b11000001,
            0b01100000,
            0b00100000,
            0b00000001,
            0b00000000,
            0b00000000,
        ]
        data2 = [
            0b00000001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00000000,
            0b01001000,
            0b01101100,
        ]
        data3 = [
            0b00000000,
            0b10100100,
            0b00000000,
            0b00000000,
            0b00000100,
            0b00101000,
            0b10001000,
        ]
        data4 = [
            0b00000010,
            0b00000000,
            0b00101000,
            0b00000001,
            0b11000010,
            0b10000010,
            0b00110100,
            0b00011011,
            0b11000000,
            0b00000000,
            0b00010110,
            0b00000000,
            0b00000000,
            0b10000000,
            0b00000000,
            0b00000000,
            0b01010010,
        ]
        return data1, data2, data3, data4

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
    data1, data2, data3, data4 = getData(c)
    code = start
    code += getLevelsByData(
        level1,
        data1,
    )
    code += connect1
    code += getLevelsByData(
        level2,
        data2,
    )
    code += connect2
    code += getLevelsByData(
        level3,
        data3,
    )
    code += connect3
    code += getLevelsByData(
        level4,
        data4,
    )
    code += end
    return code


if __name__ == "__main__":
    print("海信空调抓码生成")
    print("电平码：")
    code = cmd("ch")
    print(code)
