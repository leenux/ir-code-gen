# 康佳电视

startLevel = (3000, 3000)  # 引导码
level = ((520, 1480), (520, 2510))  # 0,1对应的电平
endLevel = (520, 4000, 520, 23000)


def getLevelsByByte(b):
    lvls = ()
    for i in range(7, -1, -1):
        lvls += level[((2**i) & b) >> i]
    return lvls


def getLevelsByCode(a):
    lvlString = ()
    lvlString += getLevelsByByte(a)
    return lvlString


if __name__ == "__main__":
    print("康佳电视")
    code =()
    for i in range(6):
        code += startLevel  # 引导码
        code += getLevelsByCode(0x02)  # address
        code += getLevelsByCode(0x13)  # command
        code += endLevel  # 结束码
        print("---", i)
    print("电平码：")
    print(code)
