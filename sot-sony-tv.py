# coding=utf-8
# 说明：索尼电视

startLevel = (2420, 600)  # 引导码
level = ((618, 595), (1218, 595))  # 0,1对应的电平


def getLevelsByByte(b, length):
    lvls = ()
    for i in range(length - 1, -1, -1):
        lvls += level[((2**i) & b) >> i]
    return lvls


if __name__ == "__main__":
    print("索尼电视编码生成")
    code = startLevel  # 引导码
    code += getLevelsByByte(0b110010010000, 12)  # cmd
    print("电平码：")
    print(code)
