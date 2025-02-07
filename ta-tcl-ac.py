startLevel = (3000,1650)                #引导码
level = ((500,325), (500,1050))         #0,1对应的电平
endLevel = (500,100000)                #结束码

def getLevelsByByte(b):
    lvls = ()
    for i in range(8, -1, -1):
        lvls += level[((2 ** i) & b) >> i]
    return lvls

def getLevelsByData(s):
    lvls = ()
    sum = 0
    for i in range(13):
        sum += s[i]
        lvls += getLevelsByByte(s[i])
    lsb = swap_msb_lsb(0xF + sum)
    lvls += getLevelsByByte(lsb)
    return lvls
    
def swap_msb_lsb(n):
    binary_str = bin(n)[2:]
    binary_str = binary_str.zfill(8)
    swapped_binary_str = binary_str[-1] + binary_str[1:-1] + binary_str[0]
    result = int(swapped_binary_str, 2)
    return result
    
if __name__ == "__main__":
    code = startLevel                   #引导码
    code += getLevelsByData([0b11000100,    #0
                            0b11010011,     #1
                            0b01100100,     #2
                            0b01000000,     #3
                            0b00000000,     #4
                            0b00100000,     #5
                            0b11000000,     #6
                            0b10100000,     #7
                            0b00000000,     #8
                            0b00000000,     #9
                            0b00000000,     #10
                            0b00000000,     #11
                            0b00000001])    #12
    code += endLevel                   #结束码
    print("电平码：")
    print(code)