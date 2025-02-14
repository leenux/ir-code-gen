# coding=utf-8
# 说明：索尼电视KDL60-520A

start=(2400,600)
level=((600,600),(1200,600))


def getLevelsByByte(b, length):
    lvls = ()
    for i in range(length - 1, -1, -1):
        lvls += level[((2**i) & b) >> i]
    return lvls


if __name__ == "__main__":
    print("索尼电视KDL60-520A编码生成")
    code = start  # 引导码
    code += getLevelsByByte(0b110010010000, 12)  # cmd
    print("电平码：")
    print(code)
