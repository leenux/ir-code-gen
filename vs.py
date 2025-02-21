import pandas as pd

deviation = 0.3


def clean(f):
    df = pd.read_csv(f)

    df_modified = df.iloc[1:-1]  # 使用 iloc 切片，跳过第一行和最后一行

    # df_modified.to_csv(f, index=False)  # 保存时不保留索引
    return df_modified, len(df_modified) - 1


def vs2nd(df1, df2):
    comparison = df1["Channel 0"] == df2["Channel 0"]
    if len(comparison) != comparison.sum():
        return False
    return True


def vs1st(df1, df2):
    df_diff1 = (df1["Time [s]"].diff() * 1000000).round().iloc[1:]
    df_diff2 = (df2["Time [s]"].diff() * 1000000).round().iloc[1:]
    # print("差值:", (df_diff1 - df_diff2).abs())
    # print("分母:", df_diff1)

    comp1 = (df_diff1 - df_diff2).abs() / df_diff1 > deviation
    comp2 = (df_diff1 - df_diff2).abs() / df_diff2 > deviation
    if comp1.sum() > 0:
        print(
            f"电平宽度偏差超{deviation}的:",
            [i for i, value in enumerate(comp1.tolist()) if value],
        )
        return False
    if comp2.sum() > 0:
        print(
            f"电平宽度偏差超{deviation}的:",
            [i for i, value in enumerate(comp2.tolist()) if value],
        )
        return False
    return True


if __name__ == "__main__":
    df1, len1 = clean("app/digital.csv")
    df2, len2 = clean("sal/digital.csv")
    if len1 != len2:
        raise ValueError("数据长度不一致")
    if vs2nd(df1, df2) == False:
        raise ValueError("电平高低不一致")
    if vs1st(df1, df2) == False:
        err = f"电平宽度偏差超{deviation}"
        raise ValueError(err)

    print("app与sal数据一致")
