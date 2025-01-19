def nec_encode(address, command):
    """
    生成NEC红外编码数据序列
    :param address: 地址码（8位）
    :param command: 命令码（8位）
    :return: NEC红外编码数据序列
    """
    # NEC红外编码参数（单位：微秒）
    header_mark = 9000
    header_space = 4500
    bit_mark = 560
    zero_space = 560
    one_space = 1690
    end_space = 5625

    # 初始化数据序列
    data_sequence = []

    # 添加引导码
    data_sequence.append(('mark', header_mark))
    data_sequence.append(('space', header_space))

    # 添加地址码和地址反码
    for i in range(8):
        bit = (address >> (7 - i)) & 1
        data_sequence.append(('mark', bit_mark))
        data_sequence.append(('space', one_space if bit else zero_space))
    address_inv = ~address & 0xFF
    for i in range(8):
        bit = (address_inv >> (7 - i)) & 1
        data_sequence.append(('mark', bit_mark))
        data_sequence.append(('space', one_space if bit else zero_space))

    # 添加命令码和命令反码
    for i in range(8):
        bit = (command >> (7 - i)) & 1
        data_sequence.append(('mark', bit_mark))
        data_sequence.append(('space', one_space if bit else zero_space))
    command_inv = ~command & 0xFF
    for i in range(8):
        bit = (command_inv >> (7 - i)) & 1
        data_sequence.append(('mark', bit_mark))
        data_sequence.append(('space', one_space if bit else zero_space))

    # 添加结束脉冲
    data_sequence.append(('space', end_space))

    return data_sequence

# 示例：生成地址码为0x12，命令码为0x34的NEC红外编码数据序列
address = 0x12
command = 0x34
data_sequence = nec_encode(address, command)

# 打印数据序列
for item in data_sequence:
    print(f"{item[0]}: {item[1]}us")