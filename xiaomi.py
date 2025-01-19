def xiaomi_aircon_encode(command):
    """
    生成小米空调红外编码数据序列
    :param command: 命令码（16进制字符串）
    :return: 红外编码数据序列
    """
    # 小米空调红外编码参数（单位：微秒）
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

    # 将命令码转换为二进制字符串
    binary_command = bin(int(command, 16))[2:].zfill(32)

    # 添加命令码
    for bit in binary_command:
        data_sequence.append(('mark', bit_mark))
        if bit == '1':
            data_sequence.append(('space', one_space))
        else:
            data_sequence.append(('space', zero_space))

    # 添加结束脉冲
    data_sequence.append(('space', end_space))

    return data_sequence

# 示例：生成命令码为0x0100010727的红外编码数据序列
command = "0100010727"
data_sequence = xiaomi_aircon_encode(command)

# 打印数据序列
for item in data_sequence:
    print(f"{item[0]}: {item[1]}us")