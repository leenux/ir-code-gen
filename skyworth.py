# coding=utf-8
# 说明：创维电视

start = (4500, 4500)
end = (550, 46000, 4500, 4500, 550, 1682, 550, 96000, 4500, 4500, 550, 1682, 550, 25000)
level1 = ((550, 550), (550, 1682))  # 数据的0,1对应的电平


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


if __name__ == "__main__":
    print("创维电视抓码生成")
    print("电平码：")
    code = start  # 引导码
    code += getLevelsByData(  # 数据1
        level1,
        [
            0b01110000,
            0b01110000,
            0b10101000,
            0b01010111,
        ],
    )
    code += end  # 连接码
    print(code)
