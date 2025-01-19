def r05d_encode(address, command1, command2):
    """
    生成美的空调R05D红外编码数据序列
    :param address: 地址码（8位）
    :param command1: 命令码1（8位）
    :param command2: 命令码2（8位）
    :return: R05D红外编码数据序列
    """
    # R05D红外编码参数（单位：微秒）
    header_mark = 4400
    header_space = 4400
    bit_mark = 540
    zero_space = 540
    one_space = 1620
    interval_mark = 540
    interval_space = 5220
    end_space = 20000

    # 初始化数据序列
    data_sequence = []

    # 添加引导码
    data_sequence.append((header_mark))
    data_sequence.append((header_space))

    # 添加地址码和地址反码
    for i in range(8):
        bit = (address >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))
    address_inv = ~address & 0xFF
    for i in range(8):
        bit = (address_inv >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))

    # 添加命令码1和命令码1反码
    for i in range(8):
        bit = (command1 >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))
    command1_inv = ~command1 & 0xFF
    for i in range(8):
        bit = (command1_inv >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))

    # 添加命令码2和命令码2反码
    for i in range(8):
        bit = (command2 >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))
    command2_inv = ~command2 & 0xFF
    for i in range(8):
        bit = (command2_inv >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))

    # 添加间隔码
    data_sequence.append((interval_mark))
    data_sequence.append((interval_space))

    # 重复上述过程
    data_sequence.append((header_mark))
    data_sequence.append((header_space))

    for i in range(8):
        bit = (address >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))
    for i in range(8):
        bit = (address_inv >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))

    for i in range(8):
        bit = (command1 >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))
    for i in range(8):
        bit = (command1_inv >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))

    for i in range(8):
        bit = (command2 >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))
    for i in range(8):
        bit = (command2_inv >> (7 - i)) & 1
        data_sequence.append((bit_mark))
        data_sequence.append((one_space if bit else zero_space))

    # 添加结束脉冲
    data_sequence.append((end_space))

    return data_sequence

if __name__ == "__main__":
    address = 0b01001101
    command1 = 0b10111111
    command2 = 0b00110100
    data_sequence = r05d_encode(address, command1, command2)
    print(data_sequence)

